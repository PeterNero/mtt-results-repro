<template>
    <div ref="shellRef" class="dot-war">
        <canvas ref="canvasRef" class="world" :class="{ dragging: pointerState.dragging }" @wheel.prevent="handleWheel" @pointerdown="handlePointerDown" @pointermove="handlePointerMove" @pointerup="handlePointerUp" @pointerleave="handlePointerUp"></canvas>

        <aside class="panel left-panel">
            <div class="panel-header">
                <div>
                    <p class="eyebrow">Agent ecology</p>
                    <h1>Dot War</h1>
                </div>
                <div class="sim-state" :class="{ active: running }">
                    {{ running ? 'Live' : 'Paused' }}
                </div>
            </div>

            <div class="toolbar">
                <button class="primary" type="button" @click="running = !running">
                    <span :class="running ? 'i-tabler-player-pause' : 'i-tabler-player-play'"></span>
                    {{ running ? 'Pause' : 'Run' }}
                </button>
                <button type="button" @click="resetWorld()">
                    <span class="i-tabler-refresh"></span>
                    Reset
                </button>
                <button type="button" @click="stepOnce()">
                    <span class="i-tabler-player-track-next"></span>
                    Step
                </button>
            </div>

            <section>
                <h2>Camera</h2>
                <div class="camera-controls">
                    <button type="button" title="Zoom out" aria-label="Zoom out" @click="zoomBy(0.84)">
                        <span class="i-tabler-minus"></span>
                    </button>
                    <div class="camera-readout">{{ Math.round(camera.zoom * 100) }}%</div>
                    <button type="button" title="Zoom in" aria-label="Zoom in" @click="zoomBy(1.19)">
                        <span class="i-tabler-plus"></span>
                    </button>
                    <button type="button" @click="fitCamera()">
                        <span class="i-tabler-arrows-maximize"></span>
                        Fit
                    </button>
                    <button type="button" @click="centerCamera()">
                        <span class="i-tabler-focus-centered"></span>
                        Center
                    </button>
                </div>
                <p class="hint">Wheel zooms around the cursor. Drag the arena to pan.</p>
            </section>

            <section>
                <h2>Map</h2>
                <div class="segmented">
                    <button v-for="map in maps" :key="map.id" type="button" :class="{ selected: selectedMap === map.id }" @click="setMap(map.id)">
                        {{ map.label }}
                    </button>
                </div>
            </section>

            <section class="controls">
                <label>
                    <span>Tribes</span>
                    <output>{{ tribeCount }}</output>
                    <input v-model.number="tribeCount" min="2" max="4" step="1" type="range" @change="resetWorld()">
                </label>
                <label>
                    <span>Dots per tribe</span>
                    <output>{{ initialDotsPerTribe }}</output>
                    <input v-model.number="initialDotsPerTribe" min="12" max="72" step="4" type="range" @change="resetWorld()">
                </label>
                <label>
                    <span>Food pressure</span>
                    <output>{{ foodRate.toFixed(2) }}</output>
                    <input v-model.number="foodRate" min="0.15" max="1.2" step="0.01" type="range">
                </label>
                <label>
                    <span>Aggression bias</span>
                    <output>{{ aggressionBias.toFixed(2) }}</output>
                    <input v-model.number="aggressionBias" min="0.05" max="1" step="0.01" type="range" @change="nudgeTribeTraits()">
                </label>
                <label>
                    <span>Builder bias</span>
                    <output>{{ buildBias.toFixed(2) }}</output>
                    <input v-model.number="buildBias" min="0.05" max="1" step="0.01" type="range" @change="nudgeTribeTraits()">
                </label>
                <label>
                    <span>Speed</span>
                    <output>{{ selectedSpeed.toFixed(1) }}x</output>
                    <input v-model.number="selectedSpeed" min="0.3" max="2.4" step="0.1" type="range">
                </label>
            </section>

            <section>
                <h2>View</h2>
                <div class="toggle-grid">
                    <button type="button" :class="{ selected: showVision }" @click="showVision = !showVision">
                        <span class="i-tabler-eye"></span>
                        Vision
                    </button>
                    <button type="button" :class="{ selected: showHearing }" @click="showHearing = !showHearing">
                        <span class="i-tabler-ear"></span>
                        Hearing
                    </button>
                    <button type="button" :class="{ selected: showMemory }" @click="showMemory = !showMemory">
                        <span class="i-tabler-brain"></span>
                        Memory
                    </button>
                    <button type="button" :class="{ selected: showRoles }" @click="showRoles = !showRoles">
                        <span class="i-tabler-badge"></span>
                        Roles
                    </button>
                    <button type="button" :class="{ selected: showBuildings }" @click="showBuildings = !showBuildings">
                        <span class="i-tabler-building-fortress"></span>
                        Buildings
                    </button>
                    <button type="button" :class="{ selected: showTrails }" @click="showTrails = !showTrails">
                        <span class="i-tabler-route"></span>
                        Trails
                    </button>
                </div>
            </section>

            <section class="legend">
                <h2>Legend</h2>
                <div><i class="dot food"></i> Food grows when left alone</div>
                <div><i class="dot fight"></i> Combat / recent enemy contact</div>
                <div><i class="building spawn"></i> Spawn place: needs two builders</div>
                <div><i class="building fort"></i> Fortress: protection radius</div>
                <div><i class="building tower"></i> Tower: wider shared sight</div>
            </section>
        </aside>

        <aside class="panel right-panel">
            <div class="metric-row">
                <div>
                    <p>Alive</p>
                    <strong>{{ metrics.alive }}</strong>
                </div>
                <div>
                    <p>Food</p>
                    <strong>{{ metrics.food }}</strong>
                </div>
                <div>
                    <p>Builds</p>
                    <strong>{{ metrics.buildings }}</strong>
                </div>
            </div>
            <div class="metric-row">
                <div>
                    <p>Births</p>
                    <strong>{{ metrics.births }}</strong>
                </div>
                <div>
                    <p>Deaths</p>
                    <strong>{{ metrics.deaths }}</strong>
                </div>
                <div>
                    <p>Fights</p>
                    <strong>{{ metrics.fights }}</strong>
                </div>
            </div>

            <section>
                <h2>Priorities</h2>
                <div class="role-mix">
                    <div v-for="entry in roleStats" :key="entry.role">
                        <span :style="{ background: entry.color }"></span>
                        <b>{{ entry.count }}</b>
                        <em>{{ entry.role }}</em>
                    </div>
                </div>
            </section>

            <section>
                <h2>Tribes</h2>
                <div v-for="tribe in tribeStats" :key="tribe.id" class="tribe-card">
                    <div class="tribe-title">
                        <span class="tribe-chip" :style="{ background: tribe.color }"></span>
                        <strong>{{ tribe.name }}</strong>
                        <span>{{ tribe.alive }} dots</span>
                    </div>
                    <div class="bar-track">
                        <div class="bar-fill" :style="{ width: `${tribe.health * 100}%`, background: tribe.color }"></div>
                    </div>
                    <div class="tribe-sub">
                        <span>Health {{ Math.round(tribe.health * 100) }}%</span>
                        <span>Kills {{ tribe.kills }}</span>
                        <span>Builds {{ tribe.buildings }}</span>
                    </div>
                </div>
            </section>

            <section>
                <h2>Selection</h2>
                <div v-if="selectedDot" class="selected-dot">
                    <div class="tribe-title">
                        <span class="tribe-chip" :style="{ background: tribePalette[selectedDot.tribe].color }"></span>
                        <strong>Dot {{ selectedDot.id }}</strong>
                        <span>{{ selectedDot.role }}</span>
                    </div>
                    <div class="info-grid">
                        <span>Health</span><b>{{ Math.round(selectedDot.health) }}</b>
                        <span>Fight</span><b>{{ selectedDot.skills.fight.toFixed(2) }}</b>
                        <span>Forage</span><b>{{ selectedDot.skills.forage.toFixed(2) }}</b>
                        <span>Build</span><b>{{ selectedDot.skills.build.toFixed(2) }}</b>
                        <span>Aggro</span><b>{{ selectedDot.traits.aggression.toFixed(2) }}</b>
                        <span>Team</span><b>{{ selectedDot.traits.teamplay.toFixed(2) }}</b>
                        <span>Known food</span><b>{{ selectedDot.memory.foods.length }}</b>
                        <span>Known enemies</span><b>{{ selectedDot.memory.enemies.length }}</b>
                    </div>
                </div>
                <p v-else class="empty">Click a dot to inspect its skills, traits, health, and memories.</p>
            </section>
        </aside>
    </div>
</template>

<script setup lang="ts">
type TribeId = 0 | 1 | 2 | 3
type MapId = 'open' | 'maze' | 'islands' | 'fortress'
type DotRole = 'forage' | 'hunt' | 'build' | 'spawn' | 'scout' | 'fight' | 'rest'
type BuildingKind = 'spawn' | 'fortress' | 'tower'

interface Skills {
    fight: number
    forage: number
    hunt: number
    build: number
    scout: number
}

interface Traits {
    aggression: number
    cowardice: number
    egoism: number
    teamplay: number
    curiosity: number
}

interface MemoryPoint {
    x: number
    y: number
    age: number
    certainty: number
}

interface Dot {
    id: number
    tribe: TribeId
    x: number
    y: number
    vx: number
    vy: number
    health: number
    hunger: number
    age: number
    cooldown: number
    spawnCooldown: number
    role: DotRole
    skills: Skills
    traits: Traits
    vision: number
    hearing: number
    memory: {
        foods: MemoryPoint[]
        enemies: MemoryPoint[]
    }
    targetX: number
    targetY: number
    selected: boolean
    trail: Array<{ x: number, y: number }>
}

interface Food {
    id: number
    x: number
    y: number
    energy: number
    growth: number
    undisturbed: number
}

interface Building {
    id: number
    kind: BuildingKind
    tribe: TribeId
    x: number
    y: number
    progress: number
    health: number
    radius: number
    workers: number[]
    spawnClock: number
}

interface Wall {
    x: number
    y: number
    w: number
    h: number
}

interface Flash {
    x: number
    y: number
    life: number
    color: string
}

const shellRef = ref<HTMLElement | null>(null)
const canvasRef = ref<HTMLCanvasElement | null>(null)

const running = ref(true)
const selectedMap = ref<MapId>('open')
const selectedSpeed = ref(1)
const tribeCount = ref(3)
const initialDotsPerTribe = ref(36)
const foodRate = ref(0.68)
const aggressionBias = ref(0.52)
const buildBias = ref(0.42)
const showVision = ref(false)
const showHearing = ref(false)
const showMemory = ref(true)
const showRoles = ref(true)
const showBuildings = ref(true)
const showTrails = ref(false)

const maps: Array<{ id: MapId, label: string }> = [
    { id: 'open', label: 'Open' },
    { id: 'maze', label: 'Maze' },
    { id: 'islands', label: 'Islands' },
    { id: 'fortress', label: 'Fortress' },
]

const tribePalette = [
    { name: 'Amber', color: '#f59e0b', soft: 'rgba(245,158,11,.16)' },
    { name: 'Cyan', color: '#22d3ee', soft: 'rgba(34,211,238,.16)' },
    { name: 'Rose', color: '#fb7185', soft: 'rgba(251,113,133,.16)' },
    { name: 'Violet', color: '#a78bfa', soft: 'rgba(167,139,250,.16)' },
] as const

const metrics = reactive({
    alive: 0,
    food: 0,
    buildings: 0,
    births: 0,
    deaths: 0,
    fights: 0,
})
const tribeKills = reactive([0, 0, 0, 0])

const tribeStats = ref<Array<{ id: TribeId, name: string, color: string, alive: number, health: number, kills: number, buildings: number }>>([])
const roleStats = ref<Array<{ role: DotRole, count: number, color: string }>>([])
const selectedDot = shallowRef<Dot | null>(null)

let dots: Dot[] = []
let foods: Food[] = []
let buildings: Building[] = []
let walls: Wall[] = []
let flashes: Flash[] = []
let nextDotId = 1
let nextFoodId = 1
let nextBuildingId = 1
let frameHandle = 0
let lastTime = 0
let viewportWidth = 1280
let viewportHeight = 720
let width = 1280
let height = 720
let rngSeed = 18271
let pixelRatio = 1
const camera = reactive({
    x: 0,
    y: 0,
    zoom: 0.72,
})
const pointerState = reactive({
    down: false,
    dragging: false,
    startX: 0,
    startY: 0,
    lastX: 0,
    lastY: 0,
})

const random = () => {
    rngSeed = (rngSeed * 1664525 + 1013904223) >>> 0
    return rngSeed / 4294967296
}

const clamp = (value: number, min: number, max: number) => Math.max(min, Math.min(max, value))
const lerp = (a: number, b: number, t: number) => a + (b - a) * t
const dist2 = (ax: number, ay: number, bx: number, by: number) => {
    const dx = ax - bx
    const dy = ay - by
    return dx * dx + dy * dy
}

const len = (x: number, y: number) => Math.sqrt(x * x + y * y) || 1

const randRange = (min: number, max: number) => min + random() * (max - min)

const trait = (bias = 0.5, spread = 0.34) => clamp(bias + (random() - 0.5) * spread, 0.05, 1)

const minZoom = () => Math.max(0.24, Math.min(viewportWidth / width, viewportHeight / height) * 0.82)

const clampCamera = () => {
    camera.zoom = clamp(camera.zoom, minZoom(), 2.8)
    const viewW = viewportWidth / camera.zoom
    const viewH = viewportHeight / camera.zoom

    if (viewW >= width)
        camera.x = (width - viewW) / 2
    else
        camera.x = clamp(camera.x, 0, width - viewW)

    if (viewH >= height)
        camera.y = (height - viewH) / 2
    else
        camera.y = clamp(camera.y, 0, height - viewH)
}

const fitCamera = () => {
    camera.zoom = minZoom()
    camera.x = (width - viewportWidth / camera.zoom) / 2
    camera.y = (height - viewportHeight / camera.zoom) / 2
    clampCamera()
}

const centerCamera = () => {
    camera.x = width / 2 - viewportWidth / (camera.zoom * 2)
    camera.y = height / 2 - viewportHeight / (camera.zoom * 2)
    clampCamera()
}

const zoomTo = (zoom: number, focalX = viewportWidth / 2, focalY = viewportHeight / 2) => {
    const before = {
        x: camera.x + focalX / camera.zoom,
        y: camera.y + focalY / camera.zoom,
    }
    camera.zoom = clamp(zoom, minZoom(), 2.8)
    camera.x = before.x - focalX / camera.zoom
    camera.y = before.y - focalY / camera.zoom
    clampCamera()
}

const zoomBy = (factor: number) => {
    zoomTo(camera.zoom * factor)
}

const canvasPoint = (event: PointerEvent | WheelEvent) => {
    const rect = canvasRef.value?.getBoundingClientRect()
    return {
        x: event.clientX - (rect?.left ?? 0),
        y: event.clientY - (rect?.top ?? 0),
    }
}

const screenToWorld = (x: number, y: number) => ({
    x: camera.x + x / camera.zoom,
    y: camera.y + y / camera.zoom,
})

const insideWall = (x: number, y: number, margin = 0) => walls.some(wall => x > wall.x - margin && x < wall.x + wall.w + margin && y > wall.y - margin && y < wall.y + wall.h + margin)

const randomFreePoint = (padding = 40) => {
    for (let i = 0; i < 120; i += 1) {
        const x = randRange(padding, width - padding)
        const y = randRange(padding, height - padding)
        if (!insideWall(x, y, 16))
            return { x, y }
    }
    return { x: width / 2, y: height / 2 }
}

const homePoint = (tribe: TribeId, total: number) => {
    const ring = Math.min(width, height) * 0.34
    const angle = (-Math.PI / 2) + tribe * ((Math.PI * 2) / total)
    return {
        x: width / 2 + Math.cos(angle) * ring,
        y: height / 2 + Math.sin(angle) * ring,
    }
}

const mutate = (value: number, amount = 0.12) => clamp(value + (random() - 0.5) * amount, 0.03, 1)

const mixSkills = (a: Skills, b: Skills): Skills => ({
    fight: mutate((a.fight + b.fight) / 2),
    forage: mutate((a.forage + b.forage) / 2),
    hunt: mutate((a.hunt + b.hunt) / 2),
    build: mutate((a.build + b.build) / 2),
    scout: mutate((a.scout + b.scout) / 2),
})

const mixTraits = (a: Traits, b: Traits): Traits => ({
    aggression: mutate((a.aggression + b.aggression) / 2),
    cowardice: mutate((a.cowardice + b.cowardice) / 2),
    egoism: mutate((a.egoism + b.egoism) / 2),
    teamplay: mutate((a.teamplay + b.teamplay) / 2),
    curiosity: mutate((a.curiosity + b.curiosity) / 2),
})

const randomSkills = (): Skills => ({
    fight: trait(0.45 + aggressionBias.value * 0.2),
    forage: trait(0.52),
    hunt: trait(0.44 + aggressionBias.value * 0.16),
    build: trait(0.28 + buildBias.value * 0.48),
    scout: trait(0.48),
})

const randomTraits = (): Traits => ({
    aggression: trait(aggressionBias.value, 0.5),
    cowardice: trait(0.52 - aggressionBias.value * 0.18, 0.48),
    egoism: trait(0.42, 0.42),
    teamplay: trait(0.58, 0.42),
    curiosity: trait(0.52, 0.46),
})

const createDot = (tribe: TribeId, x: number, y: number, skills = randomSkills(), traits = randomTraits()): Dot => {
    const scoutBoost = skills.scout * 34
    const teamBoost = traits.teamplay * 10
    const angle = random() * Math.PI * 2
    return {
        id: nextDotId++,
        tribe,
        x,
        y,
        vx: Math.cos(angle) * randRange(0.2, 0.9),
        vy: Math.sin(angle) * randRange(0.2, 0.9),
        health: randRange(86, 112),
        hunger: randRange(0.05, 0.28),
        age: 0,
        cooldown: 0,
        spawnCooldown: randRange(80, 320),
        role: 'scout',
        skills,
        traits,
        vision: 66 + scoutBoost + teamBoost,
        hearing: 42 + skills.scout * 28,
        memory: { foods: [], enemies: [] },
        targetX: x,
        targetY: y,
        selected: false,
        trail: [],
    }
}

const seedWalls = () => {
    walls = []
    if (selectedMap.value === 'maze') {
        const gap = 96
        for (let i = 1; i < 7; i += 1) {
            const x = (width / 7) * i
            const hole = randRange(height * 0.18, height * 0.82)
            walls.push({ x: x - 7, y: 80, w: 14, h: Math.max(30, hole - gap / 2 - 80) })
            walls.push({ x: x - 7, y: hole + gap / 2, w: 14, h: Math.max(30, height - hole - gap / 2 - 80) })
        }
        for (let i = 1; i < 4; i += 1) {
            const y = (height / 4) * i
            const hole = randRange(width * 0.16, width * 0.84)
            walls.push({ x: 110, y: y - 6, w: Math.max(30, hole - gap / 2 - 110), h: 12 })
            walls.push({ x: hole + gap / 2, y: y - 6, w: Math.max(30, width - hole - gap / 2 - 110), h: 12 })
        }
    }
    else if (selectedMap.value === 'islands') {
        const band = Math.min(width, height) * 0.1
        walls.push({ x: width * 0.33 - 9, y: height * 0.08, w: 18, h: height * 0.36 })
        walls.push({ x: width * 0.33 - 9, y: height * 0.58, w: 18, h: height * 0.34 })
        walls.push({ x: width * 0.66 - 9, y: height * 0.08, w: 18, h: height * 0.28 })
        walls.push({ x: width * 0.66 - 9, y: height * 0.52, w: 18, h: height * 0.4 })
        walls.push({ x: width * 0.18, y: height * 0.5 - 7, w: width * 0.28, h: 14 })
        walls.push({ x: width * 0.54, y: height * 0.5 - 7, w: width * 0.28, h: 14 })
        walls.push({ x: width / 2 - band, y: height / 2 - band / 2, w: band * 2, h: band })
    }
    else if (selectedMap.value === 'fortress') {
        const cx = width / 2
        const cy = height / 2
        const s = Math.min(width, height) * 0.2
        walls.push({ x: cx - s, y: cy - s, w: s * 0.74, h: 16 })
        walls.push({ x: cx + s * 0.26, y: cy - s, w: s * 0.74, h: 16 })
        walls.push({ x: cx - s, y: cy + s, w: s * 0.7, h: 16 })
        walls.push({ x: cx + s * 0.3, y: cy + s, w: s * 0.7, h: 16 })
        walls.push({ x: cx - s, y: cy - s, w: 16, h: s * 0.74 })
        walls.push({ x: cx - s, y: cy + s * 0.28, w: 16, h: s * 0.72 })
        walls.push({ x: cx + s, y: cy - s, w: 16, h: s * 0.74 })
        walls.push({ x: cx + s, y: cy + s * 0.28, w: 16, h: s * 0.72 })
        walls.push({ x: cx - 55, y: cy - 10, w: 110, h: 20 })
    }
}

const seedWorld = () => {
    dots = []
    foods = []
    buildings = []
    walls = []
    flashes = []
    selectedDot.value = null
    nextDotId = 1
    nextFoodId = 1
    nextBuildingId = 1
    metrics.births = 0
    metrics.deaths = 0
    metrics.fights = 0
    tribeKills.fill(0)
    rngSeed = Math.floor(Date.now() % 100000) + selectedMap.value.length * 997

    seedWalls()

    for (let tribe = 0; tribe < tribeCount.value; tribe += 1) {
        const home = homePoint(tribe as TribeId, tribeCount.value)
        const spawn = createBuilding('spawn', tribe as TribeId, home.x, home.y)
        spawn.progress = 1
        buildings.push(spawn)

        for (let i = 0; i < initialDotsPerTribe.value; i += 1) {
            const angle = random() * Math.PI * 2
            const radius = randRange(6, 58)
            const x = clamp(home.x + Math.cos(angle) * radius, 24, width - 24)
            const y = clamp(home.y + Math.sin(angle) * radius, 24, height - 24)
            if (!insideWall(x, y, 12))
                dots.push(createDot(tribe as TribeId, x, y))
        }
    }

    const startFood = Math.floor((width * height) / 12500)
    for (let i = 0; i < startFood; i += 1)
        spawnFood(randRange(14, 32))

    updateMetrics()
}

const resizeCanvas = () => {
    const canvas = canvasRef.value
    if (!canvas)
        return

    pixelRatio = window.devicePixelRatio || 1
    viewportWidth = Math.max(920, Math.floor(window.innerWidth))
    viewportHeight = Math.max(620, Math.floor(window.innerHeight))
    width = Math.max(1800, Math.floor(viewportWidth * 1.85))
    height = Math.max(1120, Math.floor(viewportHeight * 1.85))
    canvas.width = Math.floor(viewportWidth * pixelRatio)
    canvas.height = Math.floor(viewportHeight * pixelRatio)
    canvas.style.width = `${viewportWidth}px`
    canvas.style.height = `${viewportHeight}px`
    const ctx = canvas.getContext('2d')
    if (ctx)
        ctx.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0)
}

const createBuilding = (kind: BuildingKind, tribe: TribeId, x: number, y: number): Building => {
    const radius = kind === 'spawn' ? 34 : kind === 'fortress' ? 52 : 78
    return {
        id: nextBuildingId++,
        kind,
        tribe,
        x,
        y,
        progress: 0,
        health: kind === 'fortress' ? 260 : 170,
        radius,
        workers: [],
        spawnClock: randRange(180, 420),
    }
}

const spawnFood = (energy = randRange(10, 28), near?: { x: number, y: number }) => {
    const point = near
        ? { x: clamp(near.x + randRange(-90, 90), 18, width - 18), y: clamp(near.y + randRange(-90, 90), 18, height - 18) }
        : randomFreePoint(22)
    if (insideWall(point.x, point.y, 16))
        return

    foods.push({
        id: nextFoodId++,
        x: point.x,
        y: point.y,
        energy,
        growth: randRange(0.02, 0.07),
        undisturbed: randRange(0, 160),
    })
}

const setMap = (map: MapId) => {
    selectedMap.value = map
    resetWorld()
}

const resetWorld = () => {
    resizeCanvas()
    seedWorld()
    camera.zoom = clamp(Math.max(minZoom() * 1.26, 0.68), minZoom(), 1.1)
    centerCamera()
    render()
}

const nudgeTribeTraits = () => {
    dots.forEach((dot) => {
        dot.traits.aggression = clamp(lerp(dot.traits.aggression, aggressionBias.value, 0.12), 0.04, 1)
        dot.skills.build = clamp(lerp(dot.skills.build, 0.28 + buildBias.value * 0.48, 0.12), 0.04, 1)
    })
}

const remember = (list: MemoryPoint[], x: number, y: number, certainty = 1) => {
    const existing = list.find(point => dist2(point.x, point.y, x, y) < 32 * 32)
    if (existing) {
        existing.x = lerp(existing.x, x, 0.35)
        existing.y = lerp(existing.y, y, 0.35)
        existing.age = 0
        existing.certainty = clamp(Math.max(existing.certainty, certainty), 0, 1)
    }
    else {
        list.push({ x, y, age: 0, certainty })
    }
    list.sort((a, b) => (b.certainty - b.age * 0.002) - (a.certainty - a.age * 0.002))
    if (list.length > 12)
        list.length = 12
}

const shareMemory = (a: Dot, b: Dot) => {
    if (a.tribe !== b.tribe)
        return
    const selfishDrag = 1 - ((a.traits.egoism + b.traits.egoism) / 2) * 0.48
    const share = Math.max(a.traits.teamplay, b.traits.teamplay) * selfishDrag
    if (share < 0.28)
        return

    for (const food of b.memory.foods.slice(0, 5))
        remember(a.memory.foods, food.x, food.y, food.certainty * 0.82 * share)
    for (const enemy of b.memory.enemies.slice(0, 5))
        remember(a.memory.enemies, enemy.x, enemy.y, enemy.certainty * 0.82 * share)
    for (const food of a.memory.foods.slice(0, 5))
        remember(b.memory.foods, food.x, food.y, food.certainty * 0.82 * share)
    for (const enemy of a.memory.enemies.slice(0, 5))
        remember(b.memory.enemies, enemy.x, enemy.y, enemy.certainty * 0.82 * share)
}

const decayMemory = (dot: Dot, dt: number) => {
    dot.memory.foods.forEach((point) => {
        point.age += dt
        point.certainty *= 1 - 0.0007 * dt
    })
    dot.memory.enemies.forEach((point) => {
        point.age += dt
        point.certainty *= 1 - 0.001 * dt
    })
    dot.memory.foods = dot.memory.foods.filter(point => point.certainty > 0.12 && point.age < 2400)
    dot.memory.enemies = dot.memory.enemies.filter(point => point.certainty > 0.12 && point.age < 1800)
}

const visibleFoods = (dot: Dot) => {
    const vision = effectiveVision(dot) * (1 + dot.skills.forage * 0.55 + dot.hunger * 0.18)
    const v2 = vision * vision
    return foods.filter(food => dist2(dot.x, dot.y, food.x, food.y) <= v2)
}

const visibleEnemies = (dot: Dot) => {
    const vision = effectiveVision(dot)
    const hearing = dot.hearing
    const v2 = vision * vision
    const h2 = hearing * hearing
    return dots.filter(other => other.tribe !== dot.tribe && (dist2(dot.x, dot.y, other.x, other.y) <= v2 || dist2(dot.x, dot.y, other.x, other.y) <= h2))
}

const survivalNeed = (dot: Dot) => clamp(dot.hunger * 0.78 + clamp((62 - dot.health) / 62, 0, 1) * 0.72, 0, 1.5)

const foodTargetPressure = (x: number, y: number, seeker: Dot) => dots.filter((other) => {
    if (other === seeker)
        return false
    if (other.role !== 'forage' && other.role !== 'hunt' && other.role !== 'scout')
        return false
    return dist2(other.targetX, other.targetY, x, y) < 42 * 42
}).length

const tribeFoodHints = (tribe: TribeId, seeker: Dot) => dots
    .filter(dot => dot.tribe === tribe && dot !== seeker)
    .flatMap(dot => dot.memory.foods.slice(0, 3))
    .sort((a, b) => (b.certainty - b.age * 0.001) - (a.certainty - a.age * 0.001))
    .slice(0, 10)

const targetNear = (x: number, y: number, radius: number, seed: number) => {
    const angle = (seed * 2.399963229728653 + rngSeed * 0.00017) % (Math.PI * 2)
    const r = radius * (0.72 + ((seed * 37) % 23) / 70)
    return {
        x: clamp(x + Math.cos(angle) * r, 18, width - 18),
        y: clamp(y + Math.sin(angle) * r, 18, height - 18),
    }
}

const bestFoodTarget = (dot: Dot, foodsInSight = visibleFoods(dot)) => {
    const need = survivalNeed(dot)
    const candidates = [
        ...foodsInSight.map(food => ({
            x: food.x,
            y: food.y,
            energy: food.energy,
            certainty: 1,
            visible: true,
        })),
        ...dot.memory.foods.map(food => ({
            x: food.x,
            y: food.y,
            energy: 18,
            certainty: food.certainty,
            visible: false,
        })),
        ...(need > 0.62 ? tribeFoodHints(dot.tribe, dot).map(food => ({
            x: food.x,
            y: food.y,
            energy: 14,
            certainty: food.certainty * 0.82,
            visible: false,
        })) : []),
    ].filter(candidate => !insideWall(candidate.x, candidate.y, 12))

    if (!candidates.length)
        return null

    return candidates
        .map((candidate) => {
            const d = Math.sqrt(dist2(dot.x, dot.y, candidate.x, candidate.y))
            const pressure = foodTargetPressure(candidate.x, candidate.y, dot)
            const skillReach = 0.75 + dot.skills.forage * 0.75 + dot.skills.scout * 0.28
            const score = d / skillReach + pressure * (need > 0.95 ? 22 : 76) - candidate.energy * (1.35 + dot.skills.forage * 0.7) - candidate.certainty * 42 - (candidate.visible ? 36 : 0)
            return { ...candidate, score }
        })
        .sort((a, b) => a.score - b.score)[0]
}

const completedSpawnFor = (tribe: TribeId, dot?: Dot) => buildings
    .filter(building => building.tribe === tribe && building.kind === 'spawn' && building.progress >= 1)
    .sort((a, b) => dot ? dist2(dot.x, dot.y, a.x, a.y) - dist2(dot.x, dot.y, b.x, b.y) : a.id - b.id)[0]

const tribeSpawnNeed = (tribe: TribeId) => {
    const tribeAlive = dots.filter(dot => dot.tribe === tribe).length
    const foodPerDot = foods.length / Math.max(1, dots.length)
    const sustainableTarget = initialDotsPerTribe.value * clamp(1.02 + foodPerDot * 0.18, 1.04, 1.42)
    return clamp((sustainableTarget - tribeAlive) / Math.max(1, sustainableTarget), 0, 1)
}

const effectiveVision = (dot: Dot) => {
    let vision = dot.vision
    for (const building of buildings) {
        if (building.tribe === dot.tribe && building.kind === 'tower' && building.progress >= 1 && dist2(dot.x, dot.y, building.x, building.y) < building.radius * building.radius)
            vision += 70
    }
    return vision
}

const nearestBuildingNeed = (dot: Dot) => {
    const tribeBuildings = buildings.filter(building => building.tribe === dot.tribe)
    const incomplete = tribeBuildings
        .filter(building => building.progress < 1)
        .sort((a, b) => dist2(dot.x, dot.y, a.x, a.y) - dist2(dot.x, dot.y, b.x, b.y))[0]
    if (incomplete)
        return incomplete

    const spawnCount = tribeBuildings.filter(building => building.kind === 'spawn' && building.progress >= 1).length
    const fortressCount = tribeBuildings.filter(building => building.kind === 'fortress' && building.progress >= 1).length
    const towerCount = tribeBuildings.filter(building => building.kind === 'tower' && building.progress >= 1).length
    const tribeAlive = dots.filter(other => other.tribe === dot.tribe).length

    if (spawnCount < Math.max(1, Math.floor(tribeAlive / 34)) && dot.skills.build > 0.42)
        return planBuilding(dot, 'spawn')
    if (fortressCount < Math.max(1, Math.floor(tribeAlive / 42)) && dot.skills.build > 0.48 && dot.memory.enemies.length > 0)
        return planBuilding(dot, 'fortress')
    if (towerCount < Math.max(1, Math.floor(tribeAlive / 46)) && dot.skills.build > 0.56)
        return planBuilding(dot, 'tower')
    return null
}

const planBuilding = (dot: Dot, kind: BuildingKind) => {
    const home = homePoint(dot.tribe, tribeCount.value)
    const targetMemory = kind === 'fortress' && dot.memory.enemies[0]
    const anchor = targetMemory || home
    const point = {
        x: clamp(lerp(dot.x, anchor.x, 0.55) + randRange(-60, 60), 45, width - 45),
        y: clamp(lerp(dot.y, anchor.y, 0.55) + randRange(-60, 60), 45, height - 45),
    }
    if (insideWall(point.x, point.y, 28))
        return null

    const duplicate = buildings.find(building => building.tribe === dot.tribe && building.kind === kind && dist2(point.x, point.y, building.x, building.y) < 120 * 120)
    if (duplicate)
        return duplicate

    const building = createBuilding(kind, dot.tribe, point.x, point.y)
    buildings.push(building)
    return building
}

const chooseBehavior = (dot: Dot) => {
    const foodsInSight = visibleFoods(dot)
    const enemiesInSight = visibleEnemies(dot)

    for (const food of foodsInSight)
        remember(dot.memory.foods, food.x, food.y, 1)
    for (const enemy of enemiesInSight)
        remember(dot.memory.enemies, enemy.x, enemy.y, 1)

    const need = survivalNeed(dot)
    const foodTarget = bestFoodTarget(dot, foodsInSight)
    const weak = dot.health < 34 || dot.hunger > 0.72 || need > 0.92
    const threat = enemiesInSight.sort((a, b) => dist2(dot.x, dot.y, a.x, a.y) - dist2(dot.x, dot.y, b.x, b.y))[0]
    const threatDistance = threat ? Math.sqrt(dist2(dot.x, dot.y, threat.x, threat.y)) : Infinity
    const nearbyAllies = dots.filter(other => other.tribe === dot.tribe && other !== dot && dist2(dot.x, dot.y, other.x, other.y) < 74 * 74).length
    const groupCourage = clamp(nearbyAllies / 5, 0, 1) * dot.traits.teamplay * 0.18
    const loneSelfPreservation = nearbyAllies === 0 ? dot.traits.egoism * 0.16 : 0
    const fightReadiness = dot.skills.fight * 0.55 + dot.traits.aggression * 0.45 + dot.health / 260 + groupCourage - dot.traits.cowardice * 0.38 - loneSelfPreservation

    if (foodTarget && (need > 0.58 || dot.health < 58)) {
        dot.role = 'forage'
        const target = need > 1.05 ? foodTarget : targetNear(foodTarget.x, foodTarget.y, Math.min(10, 5 + foodTargetPressure(foodTarget.x, foodTarget.y, dot) * 2), dot.id)
        dot.targetX = target.x
        dot.targetY = target.y
        return
    }

    if (threat && threatDistance < 34 && (weak || fightReadiness < 0.46)) {
        dot.role = 'rest'
        const dx = dot.x - threat.x
        const dy = dot.y - threat.y
        const length = len(dx, dy)
        dot.targetX = clamp(dot.x + (dx / length) * 170, 24, width - 24)
        dot.targetY = clamp(dot.y + (dy / length) * 170, 24, height - 24)
        return
    }

    if (weak) {
        dot.role = 'forage'
        const spread = 240 + dot.skills.scout * 190
        dot.targetX = clamp(dot.x + randRange(-spread, spread), 24, width - 24)
        dot.targetY = clamp(dot.y + randRange(-spread, spread), 24, height - 24)
        return
    }

    const spawn = completedSpawnFor(dot.tribe, dot)
    const spawnNeed = tribeSpawnNeed(dot.tribe)
    const wantsToSpawn = !!spawn
        && spawnNeed > 0.08
        && dot.health > 72
        && dot.hunger < 0.46
        && dot.spawnCooldown <= 0
        && dot.traits.teamplay + dot.skills.forage * 0.24 > dot.traits.egoism * 0.62
        && random() < 0.34 + spawnNeed * 0.5 + dot.traits.teamplay * 0.18
    if (wantsToSpawn) {
        dot.role = 'spawn'
        const target = targetNear(spawn.x, spawn.y, spawn.radius * 0.82, dot.id)
        dot.targetX = target.x
        dot.targetY = target.y
        return
    }

    const shouldBuild = dot.skills.build * buildBias.value > 0.42 && dot.health > 62 && dot.hunger < 0.54 && random() < 0.018 + dot.skills.build * 0.018 + dot.traits.teamplay * 0.012
    if (shouldBuild) {
        const building = nearestBuildingNeed(dot)
        if (building) {
            dot.role = 'build'
            const target = targetNear(building.x, building.y, building.radius * 0.42, dot.id)
            dot.targetX = target.x
            dot.targetY = target.y
            return
        }
    }

    if (foodTarget && (dot.hunger > 0.34 || dot.skills.forage + dot.traits.curiosity > 0.96 || foodsInSight.length > 0)) {
        dot.role = dot.skills.forage >= dot.skills.scout || dot.hunger > 0.42 ? 'forage' : 'scout'
        const target = targetNear(foodTarget.x, foodTarget.y, Math.min(11, 6 + foodTargetPressure(foodTarget.x, foodTarget.y, dot) * 2), dot.id)
        dot.targetX = target.x
        dot.targetY = target.y
        return
    }

    if (threat && fightReadiness >= 0.66 && dot.health > 66 && dot.hunger < 0.48) {
        dot.role = 'fight'
        dot.targetX = threat.x
        dot.targetY = threat.y
        return
    }

    const enemyMemory = dot.memory.enemies[0]
    if (enemyMemory && dot.traits.aggression + dot.skills.hunt > 1.34 && dot.health > 74 && dot.hunger < 0.42) {
        dot.role = 'hunt'
        dot.targetX = enemyMemory.x
        dot.targetY = enemyMemory.y
        return
    }

    if (dot.age % 160 < 2 || dist2(dot.x, dot.y, dot.targetX, dot.targetY) < 42 * 42) {
        const spread = dot.traits.curiosity > 0.56 ? 310 : 150
        dot.role = dot.skills.scout + dot.traits.curiosity > 1.08 ? 'scout' : 'forage'
        dot.targetX = clamp(dot.x + randRange(-spread, spread), 24, width - 24)
        dot.targetY = clamp(dot.y + randRange(-spread, spread), 24, height - 24)
    }
}

const steerDot = (dot: Dot, dt: number) => {
    const dx = dot.targetX - dot.x
    const dy = dot.targetY - dot.y
    const distance = len(dx, dy)
    const need = survivalNeed(dot)
    const roleBoost = dot.role === 'forage'
        ? 0.34 + need * 0.45 + dot.skills.forage * 0.34
        : dot.role === 'fight'
            ? dot.skills.fight * 0.24
            : dot.role === 'scout'
                ? dot.skills.scout * 0.28
                : dot.role === 'build' || dot.role === 'spawn'
                    ? -0.08
                    : 0.1
    const speed = 0.6 + dot.skills.scout * 0.34 + roleBoost - dot.hunger * 0.18
    let ax = (dx / distance) * speed * 0.045 * dt
    let ay = (dy / distance) * speed * 0.045 * dt

    for (const other of dots) {
        if (other === dot)
            continue
        const d2 = dist2(dot.x, dot.y, other.x, other.y)
        const sameTribe = other.tribe === dot.tribe
        const desiredSpacing = sameTribe
            ? (dot.role === 'build' || dot.role === 'spawn' || other.role === 'build' || other.role === 'spawn' ? 32 : 25)
            : 20
        if (d2 < desiredSpacing * desiredSpacing && d2 > 0.1) {
            const d = Math.sqrt(d2)
            const overlap = (desiredSpacing - d) / desiredSpacing
            const teamPatience = sameTribe ? 1 - dot.traits.teamplay * 0.28 : 1
            const force = (sameTribe ? 0.07 : 0.085) * overlap * teamPatience
            ax += ((dot.x - other.x) / d) * force * dt
            ay += ((dot.y - other.y) / d) * force * dt
        }
    }

    for (const wall of walls) {
        const nearestX = clamp(dot.x, wall.x, wall.x + wall.w)
        const nearestY = clamp(dot.y, wall.y, wall.y + wall.h)
        const d2 = dist2(dot.x, dot.y, nearestX, nearestY)
        if (d2 < 26 * 26) {
            const d = Math.sqrt(d2) || 1
            ax += ((dot.x - nearestX) / d) * 0.08 * dt
            ay += ((dot.y - nearestY) / d) * 0.08 * dt
        }
    }

    const drag = dot.role === 'build' || dot.role === 'spawn' ? 0.9 : 0.925
    dot.vx = clamp((dot.vx + ax) * drag, -3.4, 3.4)
    dot.vy = clamp((dot.vy + ay) * drag, -3.4, 3.4)
    dot.x += dot.vx * dt
    dot.y += dot.vy * dt

    if (dot.x < 12 || dot.x > width - 12) {
        dot.x = clamp(dot.x, 12, width - 12)
        dot.vx *= -0.62
    }
    if (dot.y < 12 || dot.y > height - 12) {
        dot.y = clamp(dot.y, 12, height - 12)
        dot.vy *= -0.62
    }

    for (const wall of walls) {
        if (dot.x > wall.x - 8 && dot.x < wall.x + wall.w + 8 && dot.y > wall.y - 8 && dot.y < wall.y + wall.h + 8) {
            const left = Math.abs(dot.x - wall.x)
            const right = Math.abs(dot.x - (wall.x + wall.w))
            const top = Math.abs(dot.y - wall.y)
            const bottom = Math.abs(dot.y - (wall.y + wall.h))
            const minSide = Math.min(left, right, top, bottom)
            if (minSide === left) {
                dot.x = wall.x - 9
                dot.vx = -Math.abs(dot.vx) * 0.45
            }
            else if (minSide === right) {
                dot.x = wall.x + wall.w + 9
                dot.vx = Math.abs(dot.vx) * 0.45
            }
            else if (minSide === top) {
                dot.y = wall.y - 9
                dot.vy = -Math.abs(dot.vy) * 0.45
            }
            else {
                dot.y = wall.y + wall.h + 9
                dot.vy = Math.abs(dot.vy) * 0.45
            }
        }
    }

    if (showTrails.value && dot.age % 4 < dt) {
        dot.trail.push({ x: dot.x, y: dot.y })
        if (dot.trail.length > 24)
            dot.trail.shift()
    }
    else if (!showTrails.value && dot.trail.length) {
        dot.trail.length = 0
    }
}

const eatFood = (dot: Dot) => {
    let eaten = false
    foods = foods.filter((food) => {
        const eatRadius = 15 + dot.skills.forage * 4
        if (dist2(dot.x, dot.y, food.x, food.y) < eatRadius * eatRadius) {
            const intake = Math.min(food.energy, 38 + dot.skills.forage * 34)
            dot.health = clamp(dot.health + intake * 0.82, 0, 120)
            dot.hunger = clamp(dot.hunger - intake / 48, 0, 1)
            food.energy -= intake
            food.undisturbed = 0
            eaten = true
            flashes.push({ x: food.x, y: food.y, life: 22, color: 'rgba(74,222,128,.75)' })
        }
        return food.energy > 2
    })
    if (eaten)
        dot.memory.foods = dot.memory.foods.filter(point => dist2(point.x, point.y, dot.x, dot.y) > 34 * 34)
}

const buildingProtection = (dot: Dot) => {
    let protection = 0
    for (const building of buildings) {
        if (building.tribe === dot.tribe && building.kind === 'fortress' && building.progress >= 1 && dist2(dot.x, dot.y, building.x, building.y) < building.radius * building.radius)
            protection = Math.max(protection, 0.42)
    }
    return protection
}

const resolveCombat = (dt: number) => {
    for (const dot of dots) {
        dot.cooldown = Math.max(0, dot.cooldown - dt)
        if (dot.cooldown > 0 || dot.role !== 'fight')
            continue
        const enemy = dots
            .filter(other => other.tribe !== dot.tribe && dist2(dot.x, dot.y, other.x, other.y) < 14 * 14)
            .sort((a, b) => a.health - b.health)[0]
        if (!enemy)
            continue

        const protection = buildingProtection(enemy)
        const wasAlive = enemy.health > 0
        const damage = (2.8 + dot.skills.fight * 5.8 + dot.traits.aggression * 1.8) * (1 - protection)
        enemy.health -= damage
        if (wasAlive && enemy.health <= 0)
            tribeKills[dot.tribe] += 1
        enemy.hunger = clamp(enemy.hunger + 0.04, 0, 1)
        dot.cooldown = 20 - dot.skills.fight * 7
        metrics.fights += 1
        flashes.push({ x: (dot.x + enemy.x) / 2, y: (dot.y + enemy.y) / 2, life: 16, color: 'rgba(248,113,113,.8)' })
    }
}

const updateBuildings = (dt: number) => {
    for (const building of buildings) {
        building.workers = []
        const nearBuilders = dots
            .filter(dot => dot.tribe === building.tribe && dot.role === 'build' && dist2(dot.x, dot.y, building.x, building.y) < building.radius * building.radius)
            .sort((a, b) => b.skills.build - a.skills.build)
        building.workers = nearBuilders.slice(0, 3).map(dot => dot.id)

        if (building.progress < 1) {
            if (nearBuilders.length >= 2) {
                const work = nearBuilders.slice(0, 3).reduce((sum, dot) => sum + dot.skills.build, 0)
                building.progress = clamp(building.progress + work * 0.0017 * dt, 0, 1)
                for (const worker of nearBuilders.slice(0, 3)) {
                    worker.hunger = clamp(worker.hunger + 0.0019 * dt, 0, 1)
                    worker.health = clamp(worker.health - 0.003 * dt, 0, 120)
                }
            }
            continue
        }

        if (building.kind !== 'spawn')
            continue

        building.spawnClock -= dt
        if (building.spawnClock > 0)
            continue

        const tribeDots = dots.filter(dot => dot.tribe === building.tribe)
        const foodPerDot = foods.length / Math.max(1, dots.length)
        const foodSafe = foodPerDot > 0.72 || tribeDots.length < initialDotsPerTribe.value * 0.75
        const parents = tribeDots
            .filter(dot => dot.health > 68 && dot.hunger < 0.5 && dot.spawnCooldown <= 0 && dist2(dot.x, dot.y, building.x, building.y) < building.radius * building.radius * 6.8)
            .sort((a, b) => (b.role === 'spawn' ? 1 : 0) - (a.role === 'spawn' ? 1 : 0) || b.health - a.health)
        const maxPopulation = initialDotsPerTribe.value * clamp(1.16 + foodPerDot * 0.22, 1.2, 1.75)
        if (foodSafe && parents.length >= 2 && tribeDots.length < maxPopulation) {
            const a = parents[Math.floor(random() * Math.min(6, parents.length))]
            const b = parents[Math.floor(random() * Math.min(6, parents.length))]
            const angle = random() * Math.PI * 2
            const baby = createDot(
                building.tribe,
                clamp(building.x + Math.cos(angle) * randRange(16, 38), 16, width - 16),
                clamp(building.y + Math.sin(angle) * randRange(16, 38), 16, height - 16),
                mixSkills(a.skills, b.skills),
                mixTraits(a.traits, b.traits),
            )
            baby.health = 70
            baby.hunger = 0.36
            baby.memory.foods = [...a.memory.foods.slice(0, 3), ...b.memory.foods.slice(0, 3)]
            baby.memory.enemies = [...a.memory.enemies.slice(0, 3), ...b.memory.enemies.slice(0, 3)]
            dots.push(baby)
            a.health -= 4
            b.health -= 4
            a.spawnCooldown = randRange(520, 920)
            b.spawnCooldown = randRange(520, 920)
            metrics.births += 1
            flashes.push({ x: baby.x, y: baby.y, life: 28, color: tribePalette[building.tribe].color })
        }
        building.spawnClock = randRange(260, 620)
    }
}

const updateFood = (dt: number) => {
    for (const food of foods) {
        const disturbed = dots.some(dot => dist2(dot.x, dot.y, food.x, food.y) < 34 * 34)
        if (disturbed)
            food.undisturbed = 0
        else
            food.undisturbed += dt

        const growBoost = food.undisturbed > 120 ? 2.3 : 1
        food.energy = clamp(food.energy + food.growth * growBoost * dt, 3, 72)
    }

    const targetFood = Math.floor((width * height) / 8200 * foodRate.value)
    const deficit = clamp((targetFood - foods.length) / Math.max(1, targetFood), 0, 1)
    if (foods.length < targetFood && random() < (0.075 + deficit * 0.08) * foodRate.value * dt)
        spawnFood(randRange(14, 34))

    if (random() < (0.01 + deficit * 0.012) * foodRate.value * dt) {
        const seed = foods[Math.floor(random() * foods.length)]
        spawnFood(randRange(8, 18), seed)
    }
}

const updateDots = (dt: number) => {
    for (const dot of dots) {
        dot.age += dt
        dot.spawnCooldown = Math.max(0, dot.spawnCooldown - dt)
        dot.hunger = clamp(dot.hunger + (0.0003 + dot.age * 0.0000000016) * dt, 0, 1)
        dot.health -= (0.004 + dot.hunger * 0.013) * dt
        decayMemory(dot, dt)
        if (dot.age % 12 < dt)
            chooseBehavior(dot)
        steerDot(dot, dt)
        eatFood(dot)
    }

    for (let i = 0; i < dots.length; i += 1) {
        for (let j = i + 1; j < dots.length; j += 1) {
            if (dist2(dots[i].x, dots[i].y, dots[j].x, dots[j].y) < 20 * 20)
                shareMemory(dots[i], dots[j])
        }
    }

    resolveCombat(dt)

    const before = dots.length
    dots = dots.filter((dot) => {
        if (dot.health > 0)
            return true
        metrics.deaths += 1
        flashes.push({ x: dot.x, y: dot.y, life: 24, color: 'rgba(148,163,184,.68)' })
        return false
    })
    if (selectedDot.value && !dots.includes(selectedDot.value))
        selectedDot.value = null
    if (before !== dots.length)
        updateMetrics()
}

const updateFlashes = (dt: number) => {
    flashes.forEach(flash => flash.life -= dt)
    flashes = flashes.filter(flash => flash.life > 0)
}

const tick = (rawDt: number) => {
    const dt = clamp(rawDt / 16.67, 0.25, 2.4) * selectedSpeed.value
    updateFood(dt)
    updateDots(dt)
    updateBuildings(dt)
    updateFlashes(dt)
    updateMetrics()
}

const stepOnce = () => {
    tick(16.67)
    render()
}

const updateMetrics = () => {
    metrics.alive = dots.length
    metrics.food = foods.length
    metrics.buildings = buildings.length
    const roles: DotRole[] = ['forage', 'spawn', 'build', 'fight', 'hunt', 'scout', 'rest']
    roleStats.value = roles.map(role => ({
        role,
        count: dots.filter(dot => dot.role === role).length,
        color: roleColor(role),
    })).filter(entry => entry.count > 0)
    tribeStats.value = tribePalette.slice(0, tribeCount.value).map((tribe, id) => {
        const tribeDots = dots.filter(dot => dot.tribe === id)
        const health = tribeDots.length
            ? tribeDots.reduce((sum, dot) => sum + clamp(dot.health / 120, 0, 1), 0) / tribeDots.length
            : 0
        return {
            id: id as TribeId,
            name: tribe.name,
            color: tribe.color,
            alive: tribeDots.length,
            health,
            kills: tribeKills[id],
            buildings: buildings.filter(building => building.tribe === id && building.progress >= 1).length,
        }
    })
}

const renderGrid = (ctx: CanvasRenderingContext2D) => {
    ctx.fillStyle = '#071019'
    ctx.fillRect(0, 0, width, height)
    ctx.strokeStyle = 'rgba(148,163,184,.055)'
    ctx.lineWidth = 1
    const step = 40
    for (let x = 0; x < width; x += step) {
        ctx.beginPath()
        ctx.moveTo(x, 0)
        ctx.lineTo(x, height)
        ctx.stroke()
    }
    for (let y = 0; y < height; y += step) {
        ctx.beginPath()
        ctx.moveTo(0, y)
        ctx.lineTo(width, y)
        ctx.stroke()
    }
    ctx.strokeStyle = 'rgba(94,234,212,.18)'
    ctx.lineWidth = 2
    ctx.strokeRect(1, 1, width - 2, height - 2)
}

const renderWalls = (ctx: CanvasRenderingContext2D) => {
    ctx.fillStyle = 'rgba(30,41,59,.95)'
    ctx.strokeStyle = 'rgba(148,163,184,.18)'
    ctx.lineWidth = 1
    for (const wall of walls) {
        ctx.fillRect(wall.x, wall.y, wall.w, wall.h)
        ctx.strokeRect(wall.x + 0.5, wall.y + 0.5, wall.w, wall.h)
    }
}

const renderFood = (ctx: CanvasRenderingContext2D) => {
    for (const food of foods) {
        const r = 2.4 + food.energy * 0.07
        ctx.beginPath()
        ctx.fillStyle = `rgba(74,222,128,${0.42 + food.energy / 100})`
        ctx.arc(food.x, food.y, r, 0, Math.PI * 2)
        ctx.fill()
        if (food.undisturbed > 160) {
            ctx.strokeStyle = 'rgba(74,222,128,.18)'
            ctx.lineWidth = 1
            ctx.beginPath()
            ctx.arc(food.x, food.y, r + 5, 0, Math.PI * 2)
            ctx.stroke()
        }
    }
}

const renderBuildings = (ctx: CanvasRenderingContext2D) => {
    if (!showBuildings.value)
        return

    for (const building of buildings) {
        const color = tribePalette[building.tribe].color
        ctx.save()
        ctx.translate(building.x, building.y)
        ctx.globalAlpha = building.progress >= 1 ? 1 : 0.45

        if (building.kind === 'fortress') {
            ctx.fillStyle = tribePalette[building.tribe].soft
            ctx.strokeStyle = color
            ctx.lineWidth = 1.5
            ctx.beginPath()
            ctx.arc(0, 0, building.radius, 0, Math.PI * 2)
            ctx.fill()
            ctx.stroke()
        }
        else if (building.kind === 'tower') {
            ctx.strokeStyle = color
            ctx.fillStyle = tribePalette[building.tribe].soft
            ctx.beginPath()
            ctx.arc(0, 0, building.radius, 0, Math.PI * 2)
            ctx.stroke()
        }

        ctx.strokeStyle = color
        ctx.fillStyle = '#0f172a'
        ctx.lineWidth = 2
        if (building.kind === 'spawn') {
            ctx.beginPath()
            ctx.roundRect(-15, -15, 30, 30, 5)
            ctx.fill()
            ctx.stroke()
            ctx.beginPath()
            ctx.arc(0, 0, 7, 0, Math.PI * 2)
            ctx.stroke()
        }
        else if (building.kind === 'fortress') {
            ctx.beginPath()
            for (let i = 0; i < 6; i += 1) {
                const angle = (Math.PI * 2 * i) / 6 + Math.PI / 6
                const x = Math.cos(angle) * 17
                const y = Math.sin(angle) * 17
                if (i === 0)
                    ctx.moveTo(x, y)
                else
                    ctx.lineTo(x, y)
            }
            ctx.closePath()
            ctx.fill()
            ctx.stroke()
        }
        else {
            ctx.beginPath()
            ctx.moveTo(0, -20)
            ctx.lineTo(17, 16)
            ctx.lineTo(-17, 16)
            ctx.closePath()
            ctx.fill()
            ctx.stroke()
            ctx.beginPath()
            ctx.moveTo(0, -20)
            ctx.lineTo(0, -32)
            ctx.stroke()
        }

        if (building.progress < 1) {
            ctx.strokeStyle = 'rgba(255,255,255,.72)'
            ctx.lineWidth = 3
            ctx.beginPath()
            ctx.arc(0, 0, 24, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * building.progress)
            ctx.stroke()
        }
        ctx.restore()
    }
}

const roleColor = (role: DotRole) => {
    switch (role) {
        case 'fight': return '#f87171'
        case 'hunt': return '#fb923c'
        case 'forage': return '#4ade80'
        case 'build': return '#facc15'
        case 'spawn': return '#f472b6'
        case 'scout': return '#60a5fa'
        case 'rest': return '#cbd5e1'
        default: return '#ffffff'
    }
}

const renderDots = (ctx: CanvasRenderingContext2D) => {
    if (showMemory.value) {
        for (const dot of dots) {
            const color = tribePalette[dot.tribe].color
            ctx.globalAlpha = 0.12
            ctx.fillStyle = color
            for (const food of dot.memory.foods.slice(0, 2)) {
                ctx.beginPath()
                ctx.arc(food.x, food.y, 5, 0, Math.PI * 2)
                ctx.fill()
            }
            ctx.strokeStyle = '#fb7185'
            for (const enemy of dot.memory.enemies.slice(0, 1)) {
                ctx.beginPath()
                ctx.moveTo(enemy.x - 6, enemy.y - 6)
                ctx.lineTo(enemy.x + 6, enemy.y + 6)
                ctx.moveTo(enemy.x + 6, enemy.y - 6)
                ctx.lineTo(enemy.x - 6, enemy.y + 6)
                ctx.stroke()
            }
            ctx.globalAlpha = 1
        }
    }

    if (showVision.value || showHearing.value) {
        for (const dot of dots.filter((_, index) => index % 5 === 0)) {
            const color = tribePalette[dot.tribe]
            if (showVision.value) {
                ctx.strokeStyle = color.soft
                ctx.lineWidth = 1
                ctx.beginPath()
                ctx.arc(dot.x, dot.y, effectiveVision(dot), 0, Math.PI * 2)
                ctx.stroke()
            }
            if (showHearing.value) {
                ctx.strokeStyle = 'rgba(226,232,240,.08)'
                ctx.lineWidth = 1
                ctx.beginPath()
                ctx.arc(dot.x, dot.y, dot.hearing, 0, Math.PI * 2)
                ctx.stroke()
            }
        }
    }

    for (const dot of dots) {
        const tribe = tribePalette[dot.tribe]
        if (showTrails.value && dot.trail.length > 1) {
            ctx.strokeStyle = tribe.soft
            ctx.lineWidth = 1.5
            ctx.beginPath()
            ctx.moveTo(dot.trail[0].x, dot.trail[0].y)
            for (const point of dot.trail)
                ctx.lineTo(point.x, point.y)
            ctx.stroke()
        }

        const r = 4 + clamp(dot.health / 120, 0, 1) * 2.4
        ctx.fillStyle = tribe.color
        ctx.strokeStyle = dot.selected ? '#ffffff' : 'rgba(15,23,42,.86)'
        ctx.lineWidth = dot.selected ? 2.8 : 1.2
        ctx.beginPath()
        ctx.arc(dot.x, dot.y, r, 0, Math.PI * 2)
        ctx.fill()
        ctx.stroke()

        ctx.strokeStyle = roleColor(dot.role)
        ctx.lineWidth = 1.4
        ctx.beginPath()
        ctx.arc(dot.x, dot.y, r + 3, -Math.PI / 2, -Math.PI / 2 + Math.PI * 2 * clamp(dot.health / 120, 0, 1))
        ctx.stroke()

        if (showRoles.value) {
            ctx.fillStyle = roleColor(dot.role)
            ctx.beginPath()
            ctx.arc(dot.x + r * 0.9, dot.y - r * 0.9, 2.2, 0, Math.PI * 2)
            ctx.fill()
        }
    }
}

const renderFlashes = (ctx: CanvasRenderingContext2D) => {
    for (const flash of flashes) {
        ctx.globalAlpha = clamp(flash.life / 24, 0, 1)
        ctx.fillStyle = flash.color
        ctx.beginPath()
        ctx.arc(flash.x, flash.y, 4 + (24 - flash.life) * 0.55, 0, Math.PI * 2)
        ctx.fill()
        ctx.globalAlpha = 1
    }
}

const render = () => {
    const canvas = canvasRef.value
    const ctx = canvas?.getContext('2d')
    if (!ctx)
        return

    ctx.setTransform(pixelRatio, 0, 0, pixelRatio, 0, 0)
    ctx.fillStyle = '#050a12'
    ctx.fillRect(0, 0, viewportWidth, viewportHeight)
    ctx.save()
    ctx.translate(-camera.x * camera.zoom, -camera.y * camera.zoom)
    ctx.scale(camera.zoom, camera.zoom)
    renderGrid(ctx)
    renderFood(ctx)
    renderWalls(ctx)
    renderBuildings(ctx)
    renderDots(ctx)
    renderFlashes(ctx)
    ctx.restore()
}

const loop = (time: number) => {
    const dt = lastTime ? time - lastTime : 16.67
    lastTime = time
    if (running.value)
        tick(dt)
    render()
    frameHandle = requestAnimationFrame(loop)
}

const dotAt = (x: number, y: number) => dots
    .filter(dot => dist2(dot.x, dot.y, x, y) < 12 * 12)
    .sort((a, b) => dist2(a.x, a.y, x, y) - dist2(b.x, b.y, x, y))[0]

const handleWheel = (event: WheelEvent) => {
    const point = canvasPoint(event)
    zoomTo(camera.zoom * (event.deltaY > 0 ? 0.88 : 1.12), point.x, point.y)
}

const handlePointerDown = (event: PointerEvent) => {
    const point = canvasPoint(event)
    const world = screenToWorld(point.x, point.y)
    pointerState.down = true
    pointerState.dragging = false
    pointerState.startX = point.x
    pointerState.startY = point.y
    pointerState.lastX = point.x
    pointerState.lastY = point.y
    const dot = dotAt(world.x, world.y)
    dots.forEach(entry => entry.selected = false)
    if (dot) {
        dot.selected = true
        selectedDot.value = dot
    }
    else {
        selectedDot.value = null
    }
    canvasRef.value?.setPointerCapture(event.pointerId)
}

const handlePointerMove = (event: PointerEvent) => {
    if (!pointerState.down)
        return
    const point = canvasPoint(event)
    const dx = point.x - pointerState.lastX
    const dy = point.y - pointerState.lastY
    pointerState.lastX = point.x
    pointerState.lastY = point.y
    if (Math.abs(point.x - pointerState.startX) + Math.abs(point.y - pointerState.startY) > 4)
        pointerState.dragging = true
    camera.x -= dx / camera.zoom
    camera.y -= dy / camera.zoom
    clampCamera()
}

const handlePointerUp = () => {
    pointerState.down = false
    pointerState.dragging = false
}

onMounted(() => {
    resetWorld()
    window.addEventListener('resize', resetWorld)
    frameHandle = requestAnimationFrame(loop)
})

onBeforeUnmount(() => {
    cancelAnimationFrame(frameHandle)
    window.removeEventListener('resize', resetWorld)
})
</script>

<style scoped>
.dot-war {
    position: fixed;
    inset: 0;
    overflow: hidden;
    background: #071019;
    color: #e5edf5;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.world {
    position: absolute;
    inset: 0;
    width: 100vw;
    height: 100vh;
    cursor: grab;
}

.world.dragging {
    cursor: grabbing;
}

.panel {
    position: absolute;
    top: 16px;
    z-index: 5;
    width: min(330px, calc(100vw - 32px));
    max-height: calc(100vh - 32px);
    overflow: auto;
    border: 1px solid rgba(148, 163, 184, .2);
    border-radius: 8px;
    background: rgba(8, 13, 24, .86);
    box-shadow: 0 16px 44px rgba(0, 0, 0, .34);
    backdrop-filter: blur(14px);
}

.left-panel {
    left: 16px;
    padding: 16px;
}

.right-panel {
    right: 16px;
    padding: 14px;
}

.panel-header,
.toolbar,
.tribe-title,
.metric-row,
.tribe-sub {
    display: flex;
    align-items: center;
}

.panel-header {
    justify-content: space-between;
    gap: 12px;
    margin-bottom: 14px;
}

.eyebrow {
    margin: 0 0 2px;
    color: #5eead4;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: .08em;
    text-transform: uppercase;
}

h1,
h2,
p {
    margin: 0;
}

h1 {
    font-size: 28px;
    line-height: 1;
}

h2 {
    margin: 16px 0 10px;
    color: #cbd5e1;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: .08em;
    text-transform: uppercase;
}

.sim-state {
    border: 1px solid rgba(148, 163, 184, .3);
    border-radius: 999px;
    padding: 5px 9px;
    color: #cbd5e1;
    font-size: 12px;
    font-weight: 700;
}

.sim-state.active {
    border-color: rgba(45, 212, 191, .45);
    color: #5eead4;
}

button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 7px;
    border: 1px solid rgba(148, 163, 184, .2);
    border-radius: 7px;
    background: rgba(15, 23, 42, .86);
    color: #e2e8f0;
    min-height: 34px;
    padding: 7px 10px;
    font-size: 13px;
    font-weight: 700;
    cursor: pointer;
    transition: border-color .16s ease, background .16s ease, transform .16s ease;
}

button:hover {
    border-color: rgba(94, 234, 212, .42);
    background: rgba(30, 41, 59, .9);
}

button:active {
    transform: translateY(1px);
}

button.primary,
button.selected {
    border-color: rgba(45, 212, 191, .58);
    background: rgba(20, 184, 166, .18);
    color: #99f6e4;
}

.toolbar {
    gap: 8px;
    flex-wrap: wrap;
}

.camera-controls {
    display: grid;
    grid-template-columns: 40px 1fr 40px repeat(2, minmax(72px, auto));
    gap: 7px;
}

.camera-readout {
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid rgba(148, 163, 184, .2);
    border-radius: 7px;
    background: rgba(15, 23, 42, .72);
    color: #e2e8f0;
    min-height: 34px;
    font-size: 13px;
    font-weight: 800;
    font-variant-numeric: tabular-nums;
}

.hint {
    margin-top: 8px;
    color: #94a3b8;
    font-size: 12px;
    line-height: 1.35;
}

.segmented,
.toggle-grid {
    display: grid;
    gap: 7px;
}

.segmented {
    grid-template-columns: repeat(4, 1fr);
}

.toggle-grid {
    grid-template-columns: repeat(2, 1fr);
}

.controls {
    display: grid;
    gap: 12px;
}

label {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 6px 10px;
    color: #cbd5e1;
    font-size: 13px;
    font-weight: 700;
}

output {
    color: #f8fafc;
    font-variant-numeric: tabular-nums;
}

input[type="range"] {
    grid-column: 1 / -1;
    width: 100%;
    accent-color: #14b8a6;
}

.legend {
    display: grid;
    gap: 7px;
}

.legend div {
    display: flex;
    align-items: center;
    gap: 8px;
    color: #cbd5e1;
    font-size: 12px;
}

.dot,
.building {
    display: inline-block;
    flex: 0 0 auto;
}

.dot {
    width: 10px;
    height: 10px;
    border-radius: 999px;
}

.dot.food {
    background: #4ade80;
}

.dot.fight {
    background: #f87171;
}

.building {
    width: 12px;
    height: 12px;
    border: 2px solid #f8fafc;
}

.building.spawn {
    border-color: #5eead4;
}

.building.fort {
    border-color: #facc15;
    border-radius: 999px;
}

.building.tower {
    width: 0;
    height: 0;
    border-right: 7px solid transparent;
    border-bottom: 13px solid #60a5fa;
    border-left: 7px solid transparent;
}

.metric-row {
    gap: 8px;
    margin-bottom: 8px;
}

.metric-row > div {
    flex: 1;
    border: 1px solid rgba(148, 163, 184, .16);
    border-radius: 8px;
    background: rgba(15, 23, 42, .6);
    padding: 10px;
}

.metric-row p {
    color: #94a3b8;
    font-size: 11px;
    font-weight: 800;
    letter-spacing: .06em;
    text-transform: uppercase;
}

.metric-row strong {
    color: #f8fafc;
    font-size: 20px;
    font-variant-numeric: tabular-nums;
}

.role-mix {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 7px;
}

.role-mix div {
    display: grid;
    grid-template-columns: 9px auto 1fr;
    align-items: center;
    gap: 7px;
    border: 1px solid rgba(148, 163, 184, .16);
    border-radius: 7px;
    background: rgba(15, 23, 42, .58);
    padding: 7px 8px;
}

.role-mix span {
    width: 9px;
    height: 9px;
    border-radius: 999px;
}

.role-mix b {
    color: #f8fafc;
    font-size: 13px;
    font-variant-numeric: tabular-nums;
}

.role-mix em {
    overflow: hidden;
    color: #94a3b8;
    font-size: 11px;
    font-style: normal;
    font-weight: 800;
    text-overflow: ellipsis;
    text-transform: capitalize;
    white-space: nowrap;
}

.tribe-card {
    border: 1px solid rgba(148, 163, 184, .16);
    border-radius: 8px;
    background: rgba(15, 23, 42, .58);
    padding: 10px;
}

.tribe-card + .tribe-card {
    margin-top: 8px;
}

.tribe-title {
    gap: 8px;
    justify-content: space-between;
    font-size: 13px;
}

.tribe-title strong {
    margin-right: auto;
}

.tribe-title span:last-child {
    color: #94a3b8;
    font-size: 12px;
    font-weight: 700;
}

.tribe-chip {
    width: 10px;
    height: 10px;
    border-radius: 999px;
}

.bar-track {
    height: 6px;
    margin: 9px 0 7px;
    overflow: hidden;
    border-radius: 999px;
    background: rgba(51, 65, 85, .8);
}

.bar-fill {
    height: 100%;
    border-radius: inherit;
}

.tribe-sub {
    justify-content: space-between;
    color: #94a3b8;
    font-size: 11px;
    font-weight: 700;
}

.selected-dot,
.empty {
    border: 1px solid rgba(148, 163, 184, .16);
    border-radius: 8px;
    background: rgba(15, 23, 42, .58);
    padding: 10px;
}

.empty {
    color: #94a3b8;
    font-size: 13px;
    line-height: 1.45;
}

.info-grid {
    display: grid;
    grid-template-columns: 1fr auto;
    gap: 5px 12px;
    margin-top: 10px;
    color: #94a3b8;
    font-size: 12px;
}

.info-grid b {
    color: #f8fafc;
    font-variant-numeric: tabular-nums;
}

@media (max-width: 980px) {
    .panel {
        width: calc(100vw - 24px);
        max-height: 44vh;
    }

    .left-panel {
        top: 12px;
        left: 12px;
        right: 12px;
    }

    .right-panel {
        top: auto;
        right: 12px;
        bottom: 12px;
        left: 12px;
    }

    .camera-controls {
        grid-template-columns: 40px 1fr 40px;
    }

    .camera-controls button:nth-last-child(-n+2) {
        grid-column: span 1;
    }
}
</style>
