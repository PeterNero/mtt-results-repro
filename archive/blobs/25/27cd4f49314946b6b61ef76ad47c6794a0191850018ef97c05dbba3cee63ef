<template>
    <section ref="shellRef" class="gravity-miner-shell">
        <canvas
            ref="canvasRef"
            class="gravity-miner-canvas"
            @pointerdown="onPointerDown"
            @pointermove="onPointerMove"
            @pointerup="onPointerUp"
            @pointerleave="onPointerUp"
            @wheel.prevent="onWheel"
        ></canvas>

        <header class="topbar">
            <NuxtLink to="/" class="home-link" title="Home">
                <span class="i-tabler-arrow-left text-base"></span>
                <span>SandboxScience</span>
            </NuxtLink>
            <div class="title-wrap">
                <div class="title-row">
                    <span class="i-tabler-rocket title-icon"></span>
                    <h1>Gravity Miner</h1>
                    <span class="mode-pill">lander sim</span>
                </div>
                <p>Thruster-only flight through planetary gravity, cave mining, tractor haulage, and base delivery.</p>
            </div>
            <div class="top-actions">
                <button class="icon-button" type="button" :title="running ? 'Pause' : 'Run'" @click="running = !running">
                    <span :class="running ? 'i-tabler-player-pause' : 'i-tabler-player-play'"></span>
                </button>
                <button class="icon-button" type="button" title="Reset run" @click="resetGame">
                    <span class="i-tabler-refresh"></span>
                </button>
            </div>
        </header>

        <aside class="hud panel">
            <div class="metric-row">
                <span>Credits</span>
                <strong>{{ score }}</strong>
            </div>
            <div class="metric-row">
                <span>Cargo</span>
                <strong>{{ cargoLabel }}</strong>
            </div>
            <div class="metric-row">
                <span>Fuel</span>
                <strong>{{ Math.round(ship.fuel) }}%</strong>
            </div>
            <div class="metric-row">
                <span>Hull</span>
                <strong>{{ Math.round(ship.hull) }}%</strong>
            </div>
            <div class="metric-row">
                <span>Speed</span>
                <strong>{{ shipSpeed.toFixed(1) }}</strong>
            </div>
            <div class="metric-row">
                <span>Nearest</span>
                <strong>{{ nearestOreLabel }}</strong>
            </div>
        </aside>

        <aside class="controls panel">
            <section>
                <h2>Flight</h2>
                <div class="control-grid">
                    <span><b>W</b> main thrust</span>
                    <span><b>A/D</b> rotate</span>
                    <span><b>Q/E</b> side jets</span>
                    <span><b>Space</b> tractor</span>
                </div>
            </section>
            <section>
                <h2>Simulation</h2>
                <label>
                    <span>Gravity</span>
                    <input v-model.number="settings.gravity" type="range" min="0.15" max="1.6" step="0.05">
                    <strong>{{ settings.gravity.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Tractor</span>
                    <input v-model.number="settings.tractor" type="range" min="0.4" max="2.6" step="0.05">
                    <strong>{{ settings.tractor.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Caves</span>
                    <input v-model.number="settings.caveGlow" type="range" min="0" max="1" step="0.05">
                    <strong>{{ Math.round(settings.caveGlow * 100) }}%</strong>
                </label>
                <label class="checkbox-row">
                    <input v-model="settings.showVectors" type="checkbox">
                    <span>Vectors</span>
                </label>
            </section>
        </aside>

        <div class="status-strip">
            <span>{{ statusText }}</span>
        </div>
    </section>
</template>

<script setup lang="ts">
type OreKind = 'iron' | 'copper' | 'gold' | 'iridium'

interface Cave {
    x: number
    y: number
    r: number
}

interface OreChunk {
    id: number
    kind: OreKind
    value: number
    x: number
    y: number
    vx: number
    vy: number
    r: number
    mass: number
    planetId: number
    state: 'embedded' | 'loose' | 'carried' | 'delivered'
}

interface Planet {
    id: number
    name: string
    x: number
    y: number
    r: number
    mass: number
    colorA: string
    colorB: string
    baseAngle?: number
    caves: Cave[]
    ores: OreChunk[]
}

interface Ship {
    x: number
    y: number
    vx: number
    vy: number
    angle: number
    av: number
    fuel: number
    hull: number
    landed: boolean
}

const canvasRef = ref<HTMLCanvasElement | null>(null)
const shellRef = ref<HTMLElement | null>(null)
const running = ref(true)
const score = ref(0)
const statusText = ref('Collect cave metals with the tractor beam and haul them back to the base pad.')

const settings = reactive({
    gravity: 0.72,
    tractor: 1.15,
    caveGlow: 0.7,
    showVectors: false,
})

const keys = new Set<string>()
const pointer = reactive({ active: false, x: 0, y: 0 })
const camera = reactive({ x: 0, y: 0, zoom: 1 })
const ship = reactive<Ship>({ x: -120, y: -470, vx: 1.1, vy: 0.15, angle: -0.18, av: 0, fuel: 100, hull: 100, landed: false })

let ctx: CanvasRenderingContext2D | null = null
let planets: Planet[] = []
let carriedOre: OreChunk | null = null
let animationId = 0
let lastFrame = performance.now()
let dpr = 1
let width = 1
let height = 1
let nextOreId = 1

const orePalette: Record<OreKind, { fill: string, glow: string, label: string }> = {
    iron: { fill: '#9ca3af', glow: 'rgba(203, 213, 225, 0.5)', label: 'Iron' },
    copper: { fill: '#f97316', glow: 'rgba(251, 146, 60, 0.55)', label: 'Copper' },
    gold: { fill: '#facc15', glow: 'rgba(250, 204, 21, 0.62)', label: 'Gold' },
    iridium: { fill: '#a78bfa', glow: 'rgba(167, 139, 250, 0.65)', label: 'Iridium' },
}

const cargoLabel = computed(() => carriedOre ? orePalette[carriedOre.kind].label : 'empty')
const shipSpeed = computed(() => Math.hypot(ship.vx, ship.vy))
const nearestOreLabel = computed(() => {
    const nearest = findNearestOre()
    if (!nearest) return 'none'
    return `${orePalette[nearest.ore.kind].label} ${Math.round(nearest.distance)}m`
})

function resetGame() {
    score.value = 0
    nextOreId = 1
    carriedOre = null
    Object.assign(ship, { x: -120, y: -470, vx: 1.1, vy: 0.15, angle: -0.18, av: 0, fuel: 100, hull: 100, landed: false })
    planets = buildSystem()
    statusText.value = 'Collect cave metals with the tractor beam and haul them back to the base pad.'
}

function buildSystem() {
    const home = makePlanet({
        id: 1,
        name: 'Bastion',
        x: 0,
        y: 0,
        r: 260,
        mass: 118000,
        colorA: '#50616d',
        colorB: '#232c34',
        baseAngle: -Math.PI / 2,
        caveSeed: 0,
        oreKinds: ['iron', 'copper', 'gold'],
    })

    const ember = makePlanet({
        id: 2,
        name: 'Emberfall',
        x: 840,
        y: -180,
        r: 190,
        mass: 72000,
        colorA: '#6f4f46',
        colorB: '#2f1f1d',
        caveSeed: 1.7,
        oreKinds: ['copper', 'gold', 'iridium'],
    })

    const pale = makePlanet({
        id: 3,
        name: 'Pale Quarry',
        x: -760,
        y: 460,
        r: 150,
        mass: 42000,
        colorA: '#68717f',
        colorB: '#2b3140',
        caveSeed: 3.1,
        oreKinds: ['iron', 'gold', 'iridium'],
    })

    return [home, ember, pale]
}

function makePlanet(config: {
    id: number
    name: string
    x: number
    y: number
    r: number
    mass: number
    colorA: string
    colorB: string
    baseAngle?: number
    caveSeed: number
    oreKinds: OreKind[]
}): Planet {
    const caves: Cave[] = []
    const ores: OreChunk[] = []
    for (let i = 0; i < 9; i++) {
        const angle = config.caveSeed + i * 1.74
        const depth = 0.28 + ((i * 37) % 41) / 100
        const radius = config.r * (0.12 + ((i * 19) % 27) / 220)
        caves.push({
            x: Math.cos(angle) * config.r * depth,
            y: Math.sin(angle) * config.r * depth,
            r: radius,
        })
    }

    for (let i = 0; i < 18; i++) {
        const cave = caves[i % caves.length]
        const angle = config.caveSeed * 2 + i * 2.31
        const radius = cave.r * (0.18 + ((i * 13) % 70) / 110)
        const kind = config.oreKinds[i % config.oreKinds.length]
        const value = kind === 'iron' ? 35 : kind === 'copper' ? 55 : kind === 'gold' ? 95 : 160
        ores.push({
            id: nextOreId++,
            kind,
            value,
            x: config.x + cave.x + Math.cos(angle) * radius,
            y: config.y + cave.y + Math.sin(angle) * radius,
            vx: 0,
            vy: 0,
            r: kind === 'iridium' ? 7 : kind === 'gold' ? 6 : 5,
            mass: kind === 'iridium' ? 2.4 : kind === 'gold' ? 1.8 : 1.25,
            planetId: config.id,
            state: 'embedded',
        })
    }

    return { ...config, caves, ores }
}

function resize() {
    const canvas = canvasRef.value
    if (!canvas || !shellRef.value) return
    const rect = shellRef.value.getBoundingClientRect()
    dpr = Math.min(2, window.devicePixelRatio || 1)
    width = Math.max(1, rect.width)
    height = Math.max(1, rect.height)
    canvas.width = Math.round(width * dpr)
    canvas.height = Math.round(height * dpr)
    canvas.style.width = `${width}px`
    canvas.style.height = `${height}px`
    ctx = canvas.getContext('2d')
    ctx?.setTransform(dpr, 0, 0, dpr, 0, 0)
}

function worldToScreen(x: number, y: number) {
    return {
        x: (x - camera.x) * camera.zoom + width / 2,
        y: (y - camera.y) * camera.zoom + height / 2,
    }
}

function screenToWorld(x: number, y: number) {
    return {
        x: (x - width / 2) / camera.zoom + camera.x,
        y: (y - height / 2) / camera.zoom + camera.y,
    }
}

function gravityAt(x: number, y: number) {
    let gx = 0
    let gy = 0
    let strongest: Planet | null = null
    let strongestPull = 0

    for (const planet of planets) {
        const dx = planet.x - x
        const dy = planet.y - y
        const d2 = Math.max(planet.r * planet.r * 0.18, dx * dx + dy * dy)
        const d = Math.sqrt(d2)
        const pull = settings.gravity * planet.mass / d2
        gx += dx / d * pull
        gy += dy / d * pull
        if (pull > strongestPull) {
            strongestPull = pull
            strongest = planet
        }
    }

    return { gx, gy, strongest }
}

function isInsideCave(planet: Planet, x: number, y: number) {
    const lx = x - planet.x
    const ly = y - planet.y
    for (const cave of planet.caves) {
        const dx = lx - cave.x
        const dy = ly - cave.y
        if (dx * dx + dy * dy < cave.r * cave.r) return true
    }
    return false
}

function isNearBase(planet: Planet, x: number, y: number) {
    if (planet.baseAngle === undefined) return false
    const base = basePosition(planet)
    return Math.hypot(x - base.x, y - base.y) < 46
}

function basePosition(planet: Planet) {
    const angle = planet.baseAngle ?? 0
    return {
        x: planet.x + Math.cos(angle) * (planet.r + 8),
        y: planet.y + Math.sin(angle) * (planet.r + 8),
        angle,
    }
}

function update(dt: number) {
    if (!running.value) return
    const step = Math.min(0.033, dt)
    updateShip(step)
    updateOres(step)
    updateCamera(step)
}

function updateShip(dt: number) {
    const left = keys.has('arrowleft') || keys.has('a')
    const right = keys.has('arrowright') || keys.has('d')
    const thrust = keys.has('arrowup') || keys.has('w')
    const retro = keys.has('arrowdown') || keys.has('s')
    const strafeLeft = keys.has('q')
    const strafeRight = keys.has('e')
    const tractor = keys.has(' ') || pointer.active

    ship.av += (left ? -3.2 : 0) * dt
    ship.av += (right ? 3.2 : 0) * dt
    ship.av *= 0.9
    ship.angle += ship.av * dt

    if (ship.fuel > 0) {
        const main = thrust ? 205 : retro ? -86 : 0
        const side = (strafeRight ? 1 : 0) - (strafeLeft ? 1 : 0)
        const ax = Math.cos(ship.angle) * main + Math.cos(ship.angle + Math.PI / 2) * side * 92
        const ay = Math.sin(ship.angle) * main + Math.sin(ship.angle + Math.PI / 2) * side * 92
        ship.vx += ax * dt
        ship.vy += ay * dt
        if (main !== 0 || side !== 0) ship.fuel = Math.max(0, ship.fuel - (Math.abs(main) * 0.008 + Math.abs(side) * 0.34) * dt)
    }

    const g = gravityAt(ship.x, ship.y)
    ship.vx += g.gx * dt
    ship.vy += g.gy * dt
    ship.x += ship.vx * dt
    ship.y += ship.vy * dt
    ship.landed = false

    resolveShipCollision()
    if (tractor) applyTractor(dt)
}

function resolveShipCollision() {
    for (const planet of planets) {
        const dx = ship.x - planet.x
        const dy = ship.y - planet.y
        const d = Math.hypot(dx, dy)
        if (d > planet.r + 14 || isInsideCave(planet, ship.x, ship.y)) continue

        const nx = dx / Math.max(1, d)
        const ny = dy / Math.max(1, d)
        const normalSpeed = ship.vx * nx + ship.vy * ny
        const tangentSpeed = Math.abs(ship.vx * -ny + ship.vy * nx)
        ship.x = planet.x + nx * (planet.r + 14)
        ship.y = planet.y + ny * (planet.r + 14)

        const onBase = isNearBase(planet, ship.x, ship.y)
        if (normalSpeed > 0) continue

        if (onBase && Math.abs(normalSpeed) < 22 && tangentSpeed < 34) {
            ship.vx -= nx * normalSpeed
            ship.vy -= ny * normalSpeed
            ship.vx *= 0.88
            ship.vy *= 0.88
            ship.fuel = Math.min(100, ship.fuel + 0.34)
            ship.hull = Math.min(100, ship.hull + 0.06)
            ship.landed = true
            deliverCargo()
            statusText.value = carriedOre ? 'Cargo secured. Set it down on the base pad to sell.' : 'Refueling at base pad.'
        } else {
            ship.vx -= nx * normalSpeed * 1.35
            ship.vy -= ny * normalSpeed * 1.35
            ship.vx *= 0.72
            ship.vy *= 0.72
            const impact = Math.max(0, Math.abs(normalSpeed) + tangentSpeed * 0.35 - 26)
            if (impact > 0) {
                ship.hull = Math.max(0, ship.hull - impact * 0.22)
                statusText.value = ship.hull <= 0 ? 'Hull breached. Reset run to try again.' : 'Hard contact. Touch down gently or use a cave opening.'
            }
        }
    }
}

function findNearestOre() {
    let best: { ore: OreChunk, distance: number } | null = null
    for (const planet of planets) {
        for (const ore of planet.ores) {
            if (ore.state === 'delivered' || ore.state === 'carried') continue
            const distance = Math.hypot(ore.x - ship.x, ore.y - ship.y)
            if (distance > 190) continue
            if (!best || distance < best.distance) best = { ore, distance }
        }
    }
    return best
}

function applyTractor(dt: number) {
    if (carriedOre) return
    const nearest = findNearestOre()
    if (!nearest) {
        statusText.value = 'No metal in tractor range.'
        return
    }

    const ore = nearest.ore
    ore.state = 'loose'
    const dx = ship.x - ore.x
    const dy = ship.y - ore.y
    const d = Math.max(1, Math.hypot(dx, dy))
    const pull = settings.tractor * 850 / (d + 80)
    ore.vx += dx / d * pull * dt / ore.mass
    ore.vy += dy / d * pull * dt / ore.mass
    ship.vx -= dx / d * pull * dt * 0.018
    ship.vy -= dy / d * pull * dt * 0.018
    statusText.value = `Tractor locked: ${orePalette[ore.kind].label}.`

    if (d < 24) {
        carriedOre = ore
        ore.state = 'carried'
        statusText.value = `${orePalette[ore.kind].label} attached. Tow it back to base.`
    }
}

function deliverCargo() {
    if (!carriedOre) return
    const home = planets.find(planet => planet.baseAngle !== undefined)
    if (!home || !isNearBase(home, ship.x, ship.y)) return
    score.value += carriedOre.value
    carriedOre.state = 'delivered'
    statusText.value = `${orePalette[carriedOre.kind].label} delivered for ${carriedOre.value} credits.`
    carriedOre = null
}

function updateOres(dt: number) {
    for (const planet of planets) {
        for (const ore of planet.ores) {
            if (ore.state === 'embedded' || ore.state === 'delivered') continue

            if (ore.state === 'carried' && carriedOre === ore) {
                const backX = ship.x - Math.cos(ship.angle) * 42
                const backY = ship.y - Math.sin(ship.angle) * 42
                const dx = backX - ore.x
                const dy = backY - ore.y
                ore.vx += dx * 4.4 * dt
                ore.vy += dy * 4.4 * dt
                ore.vx += (ship.vx - ore.vx) * 1.8 * dt
                ore.vy += (ship.vy - ore.vy) * 1.8 * dt
            } else {
                const g = gravityAt(ore.x, ore.y)
                ore.vx += g.gx * dt
                ore.vy += g.gy * dt
            }

            ore.x += ore.vx * dt
            ore.y += ore.vy * dt
            ore.vx *= 0.995
            ore.vy *= 0.995
            resolveOreCollision(ore)
        }
    }
}

function resolveOreCollision(ore: OreChunk) {
    for (const planet of planets) {
        const dx = ore.x - planet.x
        const dy = ore.y - planet.y
        const d = Math.hypot(dx, dy)
        if (d > planet.r + ore.r || isInsideCave(planet, ore.x, ore.y)) continue
        const nx = dx / Math.max(1, d)
        const ny = dy / Math.max(1, d)
        const normalSpeed = ore.vx * nx + ore.vy * ny
        ore.x = planet.x + nx * (planet.r + ore.r)
        ore.y = planet.y + ny * (planet.r + ore.r)
        if (normalSpeed < 0) {
            ore.vx -= nx * normalSpeed * 1.25
            ore.vy -= ny * normalSpeed * 1.25
            ore.vx *= 0.78
            ore.vy *= 0.78
        }
    }
}

function updateCamera(dt: number) {
    const targetX = ship.x + ship.vx * 0.8
    const targetY = ship.y + ship.vy * 0.8
    camera.x += (targetX - camera.x) * Math.min(1, dt * 3.2)
    camera.y += (targetY - camera.y) * Math.min(1, dt * 3.2)
}

function draw() {
    if (!ctx) return
    ctx.clearRect(0, 0, width, height)
    drawStars()
    drawWorld()
    drawHudVectors()
}

function drawStars() {
    if (!ctx) return
    const gradient = ctx.createLinearGradient(0, 0, width, height)
    gradient.addColorStop(0, '#06080d')
    gradient.addColorStop(1, '#101018')
    ctx.fillStyle = gradient
    ctx.fillRect(0, 0, width, height)
    ctx.fillStyle = 'rgba(226, 232, 240, 0.75)'
    for (let i = 0; i < 120; i++) {
        const sx = ((i * 137.5 - camera.x * 0.04) % width + width) % width
        const sy = ((i * 73.3 - camera.y * 0.04) % height + height) % height
        const r = 0.45 + (i % 5) * 0.18
        ctx.globalAlpha = 0.18 + (i % 7) * 0.075
        ctx.beginPath()
        ctx.arc(sx, sy, r, 0, Math.PI * 2)
        ctx.fill()
    }
    ctx.globalAlpha = 1
}

function drawWorld() {
    if (!ctx) return
    ctx.save()
    ctx.translate(width / 2, height / 2)
    ctx.scale(camera.zoom, camera.zoom)
    ctx.translate(-camera.x, -camera.y)

    for (const planet of planets) drawPlanet(planet)
    drawTractorBeam()
    for (const planet of planets) {
        for (const ore of planet.ores) drawOre(ore)
    }
    drawShip()

    ctx.restore()
}

function drawPlanet(planet: Planet) {
    if (!ctx) return
    const body = ctx.createRadialGradient(planet.x - planet.r * 0.4, planet.y - planet.r * 0.45, planet.r * 0.1, planet.x, planet.y, planet.r * 1.08)
    body.addColorStop(0, planet.colorA)
    body.addColorStop(0.72, planet.colorB)
    body.addColorStop(1, '#07090d')
    ctx.fillStyle = body
    ctx.beginPath()
    ctx.arc(planet.x, planet.y, planet.r, 0, Math.PI * 2)
    ctx.fill()

    ctx.save()
    ctx.globalCompositeOperation = 'destination-out'
    for (const cave of planet.caves) {
        ctx.beginPath()
        ctx.arc(planet.x + cave.x, planet.y + cave.y, cave.r, 0, Math.PI * 2)
        ctx.fill()
    }
    ctx.restore()

    ctx.strokeStyle = `rgba(103, 232, 249, ${0.08 + settings.caveGlow * 0.18})`
    ctx.lineWidth = 1.2 / camera.zoom
    for (const cave of planet.caves) {
        ctx.beginPath()
        ctx.arc(planet.x + cave.x, planet.y + cave.y, cave.r, 0, Math.PI * 2)
        ctx.stroke()
    }

    ctx.strokeStyle = 'rgba(255,255,255,0.08)'
    ctx.lineWidth = 2 / camera.zoom
    ctx.beginPath()
    ctx.arc(planet.x, planet.y, planet.r, 0, Math.PI * 2)
    ctx.stroke()

    if (planet.baseAngle !== undefined) drawBase(planet)
}

function drawBase(planet: Planet) {
    if (!ctx) return
    const base = basePosition(planet)
    const nx = Math.cos(base.angle)
    const ny = Math.sin(base.angle)
    const tx = -ny
    const ty = nx
    ctx.save()
    ctx.translate(base.x, base.y)
    ctx.rotate(base.angle + Math.PI / 2)
    ctx.fillStyle = ship.landed ? 'rgba(74, 222, 128, 0.92)' : 'rgba(45, 212, 191, 0.82)'
    ctx.strokeStyle = 'rgba(255,255,255,0.62)'
    ctx.lineWidth = 2 / camera.zoom
    ctx.fillRect(-36, -6, 72, 12)
    ctx.strokeRect(-36, -6, 72, 12)
    ctx.fillStyle = 'rgba(15, 23, 42, 0.82)'
    ctx.fillRect(-20, -30, 40, 24)
    ctx.restore()

    ctx.strokeStyle = 'rgba(45, 212, 191, 0.22)'
    ctx.beginPath()
    ctx.moveTo(base.x - tx * 42 + nx * 4, base.y - ty * 42 + ny * 4)
    ctx.lineTo(base.x + tx * 42 + nx * 4, base.y + ty * 42 + ny * 4)
    ctx.stroke()
}

function drawOre(ore: OreChunk) {
    if (!ctx || ore.state === 'delivered') return
    const palette = orePalette[ore.kind]
    ctx.save()
    if (ore.state === 'embedded') ctx.globalAlpha = 0.78
    ctx.shadowBlur = ore.state === 'carried' ? 18 : 9
    ctx.shadowColor = palette.glow
    ctx.fillStyle = palette.fill
    ctx.beginPath()
    ctx.arc(ore.x, ore.y, ore.r, 0, Math.PI * 2)
    ctx.fill()
    ctx.strokeStyle = 'rgba(255,255,255,0.34)'
    ctx.lineWidth = 1 / camera.zoom
    ctx.stroke()
    ctx.restore()
}

function drawShip() {
    if (!ctx) return
    ctx.save()
    ctx.translate(ship.x, ship.y)
    ctx.rotate(ship.angle)

    ctx.fillStyle = ship.hull > 35 ? '#e2e8f0' : '#fb7185'
    ctx.strokeStyle = 'rgba(15, 23, 42, 0.9)'
    ctx.lineWidth = 2 / camera.zoom
    ctx.beginPath()
    ctx.moveTo(22, 0)
    ctx.lineTo(-16, -13)
    ctx.lineTo(-10, 0)
    ctx.lineTo(-16, 13)
    ctx.closePath()
    ctx.fill()
    ctx.stroke()

    if ((keys.has('w') || keys.has('arrowup')) && ship.fuel > 0) {
        ctx.fillStyle = 'rgba(251, 146, 60, 0.86)'
        ctx.beginPath()
        ctx.moveTo(-15, -7)
        ctx.lineTo(-36 - Math.random() * 10, 0)
        ctx.lineTo(-15, 7)
        ctx.fill()
    }

    ctx.restore()
}

function drawTractorBeam() {
    if (!ctx) return
    const active = keys.has(' ') || pointer.active
    if (!active) return
    const target = carriedOre ?? findNearestOre()?.ore
    if (!target) return
    ctx.strokeStyle = 'rgba(125, 211, 252, 0.55)'
    ctx.lineWidth = 2 / camera.zoom
    ctx.setLineDash([8 / camera.zoom, 8 / camera.zoom])
    ctx.beginPath()
    ctx.moveTo(ship.x, ship.y)
    ctx.lineTo(target.x, target.y)
    ctx.stroke()
    ctx.setLineDash([])
}

function drawHudVectors() {
    if (!ctx || !settings.showVectors) return
    const g = gravityAt(ship.x, ship.y)
    const start = worldToScreen(ship.x, ship.y)
    ctx.strokeStyle = 'rgba(248, 113, 113, 0.82)'
    ctx.lineWidth = 2
    ctx.beginPath()
    ctx.moveTo(start.x, start.y)
    ctx.lineTo(start.x + g.gx * 6, start.y + g.gy * 6)
    ctx.stroke()
}

function loop(now: number) {
    const dt = Math.max(0.001, (now - lastFrame) / 1000)
    lastFrame = now
    update(dt)
    draw()
    animationId = requestAnimationFrame(loop)
}

function onKeyDown(event: KeyboardEvent) {
    keys.add(event.key.toLowerCase())
    if (event.key === ' ') event.preventDefault()
}

function onKeyUp(event: KeyboardEvent) {
    keys.delete(event.key.toLowerCase())
}

function onPointerDown(event: PointerEvent) {
    const point = screenToWorld(event.offsetX, event.offsetY)
    pointer.active = true
    pointer.x = point.x
    pointer.y = point.y
}

function onPointerMove(event: PointerEvent) {
    const point = screenToWorld(event.offsetX, event.offsetY)
    pointer.x = point.x
    pointer.y = point.y
}

function onPointerUp() {
    pointer.active = false
}

function onWheel(event: WheelEvent) {
    const delta = event.deltaY > 0 ? 0.9 : 1.1
    camera.zoom = Math.min(1.55, Math.max(0.45, camera.zoom * delta))
}

onMounted(() => {
    resize()
    resetGame()
    window.addEventListener('resize', resize)
    window.addEventListener('keydown', onKeyDown)
    window.addEventListener('keyup', onKeyUp)
    lastFrame = performance.now()
    animationId = requestAnimationFrame(loop)
})

onBeforeUnmount(() => {
    cancelAnimationFrame(animationId)
    window.removeEventListener('resize', resize)
    window.removeEventListener('keydown', onKeyDown)
    window.removeEventListener('keyup', onKeyUp)
})
</script>

<style scoped>
.gravity-miner-shell {
    position: fixed;
    inset: 0;
    overflow: hidden;
    background: #06080d;
    color: #e5f3f6;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.gravity-miner-canvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    touch-action: none;
}

.topbar {
    position: absolute;
    top: 14px;
    left: 14px;
    right: 14px;
    z-index: 3;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
    pointer-events: none;
}

.home-link,
.top-actions,
.panel,
.status-strip {
    pointer-events: auto;
}

.home-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    color: #dff8f3;
    text-decoration: none;
    background: rgba(9, 14, 20, 0.72);
    border: 1px solid rgba(148, 163, 184, 0.24);
    border-radius: 8px;
    padding: 9px 12px;
    backdrop-filter: blur(14px);
}

.title-wrap {
    min-width: 0;
    flex: 1;
    background: rgba(9, 14, 20, 0.62);
    border: 1px solid rgba(148, 163, 184, 0.18);
    border-radius: 8px;
    padding: 10px 14px;
    backdrop-filter: blur(14px);
}

.title-row {
    display: flex;
    align-items: center;
    gap: 10px;
}

.title-row h1 {
    margin: 0;
    font-size: 18px;
    line-height: 1.1;
}

.title-icon {
    color: #67e8f9;
    font-size: 22px;
}

.mode-pill {
    border: 1px solid rgba(103, 232, 249, 0.3);
    color: #a7f3d0;
    border-radius: 999px;
    padding: 2px 8px;
    font-size: 11px;
}

.title-wrap p {
    margin: 5px 0 0;
    color: #aebdca;
    font-size: 12px;
}

.top-actions {
    display: flex;
    gap: 8px;
}

.icon-button {
    display: grid;
    place-items: center;
    width: 38px;
    height: 38px;
    border: 1px solid rgba(148, 163, 184, 0.28);
    border-radius: 8px;
    background: rgba(9, 14, 20, 0.78);
    color: #e5f3f6;
}

.panel {
    position: absolute;
    z-index: 2;
    border: 1px solid rgba(148, 163, 184, 0.2);
    border-radius: 8px;
    background: rgba(9, 14, 20, 0.72);
    backdrop-filter: blur(14px);
    box-shadow: 0 22px 80px rgba(0, 0, 0, 0.32);
}

.hud {
    left: 16px;
    bottom: 16px;
    width: 210px;
    padding: 12px;
}

.metric-row {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    font-size: 12px;
    padding: 5px 0;
    border-bottom: 1px solid rgba(148, 163, 184, 0.1);
}

.metric-row:last-child {
    border-bottom: 0;
}

.metric-row span {
    color: #aebdca;
}

.metric-row strong {
    color: #f8fafc;
}

.controls {
    right: 16px;
    bottom: 16px;
    width: 268px;
    padding: 14px;
}

.controls section + section {
    margin-top: 14px;
}

.controls h2 {
    margin: 0 0 8px;
    font-size: 12px;
    color: #a7f3d0;
    text-transform: uppercase;
    letter-spacing: 0;
}

.control-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 7px;
    font-size: 12px;
    color: #cbd5e1;
}

.control-grid b {
    color: #fde68a;
}

.controls label {
    display: grid;
    grid-template-columns: 70px 1fr 44px;
    align-items: center;
    gap: 8px;
    font-size: 12px;
    margin-top: 8px;
}

.controls input[type="range"] {
    min-width: 0;
}

.controls strong {
    text-align: right;
    color: #f8fafc;
}

.checkbox-row {
    grid-template-columns: 18px 1fr !important;
}

.status-strip {
    position: absolute;
    left: 50%;
    bottom: 16px;
    transform: translateX(-50%);
    z-index: 2;
    max-width: min(520px, calc(100vw - 32px));
    padding: 10px 14px;
    border: 1px solid rgba(103, 232, 249, 0.22);
    border-radius: 8px;
    background: rgba(9, 14, 20, 0.7);
    color: #dff8f3;
    font-size: 12px;
    text-align: center;
    backdrop-filter: blur(14px);
}

@media (max-width: 760px) {
    .topbar {
        align-items: flex-start;
    }

    .title-wrap p {
        display: none;
    }

    .hud {
        width: 180px;
    }

    .controls {
        left: 16px;
        right: 16px;
        bottom: 112px;
        width: auto;
    }

    .status-strip {
        display: none;
    }
}
</style>
