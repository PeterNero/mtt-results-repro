<template>
    <section ref="shellRef" class="universe-shell">
        <canvas
            ref="canvasRef"
            class="universe-canvas"
            @pointerdown="startPan"
            @pointermove="movePan"
            @pointerup="endPan"
            @pointercancel="endPan"
            @wheel.prevent="handleWheel"
        ></canvas>

        <header class="topbar">
            <NuxtLink to="/" class="home-link" title="Home">
                <span class="i-tabler-arrow-left text-base"></span>
                <span>SandboxScience</span>
            </NuxtLink>
            <div class="title-wrap">
                <div class="title-row">
                    <span class="i-tabler-world-star title-icon"></span>
                    <h1>Universe Forge</h1>
                    <span class="mode-pill">coarse gravity</span>
                    <span class="mode-pill physics-pill">stellar chemistry</span>
                    <span class="mode-pill mtt-pill">MTT audit</span>
                </div>
                <p>Dark matter gathers hot H/He gas, radiation pressure fades, stars enrich space, and stable systems emerge from local cooling and feedback.</p>
            </div>
            <div class="top-actions">
                <button class="icon-button" type="button" :title="isRunning ? 'Pause' : 'Run'" @click="toggleRunning">
                    <span :class="isRunning ? 'i-tabler-player-pause' : 'i-tabler-player-play'"></span>
                </button>
                <button class="icon-button" type="button" title="Step" @click="stepOnce">
                    <span class="i-tabler-player-track-next"></span>
                </button>
                <button class="icon-button" type="button" title="Reset" @click="resetSimulation">
                    <span class="i-tabler-refresh"></span>
                </button>
            </div>
        </header>

        <aside class="control-panel">
            <section class="panel-section">
                <h2>Preset</h2>
                <div class="preset-grid">
                    <button
                        v-for="preset in presets"
                        :key="preset.id"
                        type="button"
                        :class="{ active: selectedPreset === preset.id }"
                        @click="applyPreset(preset.id)"
                    >
                        <span>{{ preset.short }}</span>
                        <b>{{ preset.label }}</b>
                    </button>
                </div>
            </section>

            <section class="panel-section">
                <h2>View</h2>
                <div class="view-tabs">
                    <button
                        v-for="mode in viewModes"
                        :key="mode.id"
                        type="button"
                        :class="{ active: viewMode === mode.id }"
                        @click="viewMode = mode.id"
                    >
                        <span :class="mode.icon"></span>
                        {{ mode.label }}
                    </button>
                </div>
            </section>

            <section class="panel-section controls">
                <h2>Engine</h2>
                <label>
                    <span>gravity</span>
                    <input v-model.number="settings.gravity" type="range" min="0.04" max="1.1" step="0.01">
                    <strong>{{ settings.gravity.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>pressure</span>
                    <input v-model.number="settings.pressure" type="range" min="0" max="1.15" step="0.01">
                    <strong>{{ settings.pressure.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>radiation</span>
                    <input v-model.number="settings.radiationPressure" type="range" min="0" max="1.4" step="0.01">
                    <strong>{{ settings.radiationPressure.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>cooling</span>
                    <input v-model.number="settings.cooling" type="range" min="0" max="1.25" step="0.01">
                    <strong>{{ settings.cooling.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>star birth</span>
                    <input v-model.number="settings.starThreshold" type="range" min="0.2" max="1.4" step="0.01">
                    <strong>{{ settings.starThreshold.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>fusion</span>
                    <input v-model.number="settings.fusion" type="range" min="0.05" max="1.2" step="0.01">
                    <strong>{{ settings.fusion.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>feedback</span>
                    <input v-model.number="settings.feedback" type="range" min="0" max="1.3" step="0.01">
                    <strong>{{ settings.feedback.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>angular support</span>
                    <input v-model.number="settings.angularSupport" type="range" min="0" max="1.4" step="0.01">
                    <strong>{{ settings.angularSupport.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>spiral waves</span>
                    <input v-model.number="settings.spiralStrength" type="range" min="0" max="1.4" step="0.01">
                    <strong>{{ settings.spiralStrength.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>planet yield</span>
                    <input v-model.number="settings.planetFormation" type="range" min="0" max="1.8" step="0.01">
                    <strong>{{ settings.planetFormation.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>time</span>
                    <input v-model.number="settings.timeScale" type="range" min="0.15" max="3.5" step="0.01">
                    <strong>{{ settings.timeScale.toFixed(2) }}</strong>
                </label>
            </section>

            <section class="panel-section">
                <h2>Switches</h2>
                <label class="checkbox-row">
                    <input v-model="settings.darkMatter" type="checkbox">
                    <span>dark-matter scaffold</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="settings.pressureForces" type="checkbox">
                    <span>pressure support</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="settings.stellarFeedback" type="checkbox">
                    <span>supernova feedback</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="settings.compactMergers" type="checkbox">
                    <span>compact mergers</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="settings.blackHoles" type="checkbox">
                    <span>black-hole growth</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="settings.showPlanets" type="checkbox">
                    <span>planet systems</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="settings.mttOverlay" type="checkbox">
                    <span>MTT stability overlay</span>
                </label>
            </section>

            <section class="panel-section quick-actions">
                <h2>Add</h2>
                <div class="action-grid">
                    <button type="button" @click="injectGasCloud">
                        <span class="i-tabler-cloud-plus"></span>
                        gas cloud
                    </button>
                    <button type="button" @click="seedHalo">
                        <span class="i-tabler-spiral"></span>
                        halo seed
                    </button>
                    <button type="button" @click="triggerWave">
                        <span class="i-tabler-wave-saw-tool"></span>
                        shock wave
                    </button>
                    <button type="button" @click="enrichRegion">
                        <span class="i-tabler-atom"></span>
                        metals
                    </button>
                </div>
            </section>
        </aside>

        <aside class="metrics-panel">
            <section>
                <h2>Universe State</h2>
                <p>{{ stateSummary }}</p>
            </section>
            <div class="metric-grid">
                <div v-for="card in metricCards" :key="card.label" class="metric">
                    <span>{{ card.label }}</span>
                    <strong>{{ card.value }}</strong>
                </div>
            </div>
            <section>
                <h2>Element Ledger</h2>
                <div class="ledger">
                    <div v-for="item in elementLedger" :key="item.key">
                        <span>{{ item.label }}</span>
                        <b>{{ item.value }}</b>
                        <i :style="{ width: item.width }"></i>
                    </div>
                </div>
            </section>
            <section>
                <h2>Local Memory</h2>
                <div class="memory-list">
                    <div v-for="item in regionMemoryRows" :key="item.label">
                        <span>{{ item.label }}</span>
                        <strong>{{ item.value }}</strong>
                    </div>
                </div>
            </section>
            <section>
                <h2>Physics Audit</h2>
                <div class="audit-list">
                    <div class="audit-item native">
                        <i>std</i>
                        <span>Gravity, radiation pressure, local metal cooling, staged burning, remnant outcomes, supernova yields, compact mergers, and optional black-hole growth are coarse standard-physics rules.</span>
                    </div>
                    <div class="audit-item mtt">
                        <i>MTT</i>
                        <span>Stable clumps, stars, records, enriched regions, and systems are interpreted as closure-selected patterns in the extended proto-spinor world.</span>
                    </div>
                    <div class="audit-item toy">
                        <i>toy</i>
                        <span>Particle counts, two-dimensional projection, and visual aggregation are performance scaffolds, not claims of full cosmology.</span>
                    </div>
                </div>
            </section>
        </aside>

        <div class="legend">
            <span><i class="dot dark"></i> dark matter</span>
            <span><i class="dot gas"></i> H/He gas</span>
            <span><i class="dot star"></i> stars</span>
            <span><i class="dot remnant"></i> white dwarfs / NS</span>
            <span><i class="dot hole"></i> black holes</span>
            <span><i class="dot planet"></i> planet systems</span>
        </div>

        <div class="camera-help">
            <span class="i-tabler-arrows-move"></span>
            drag pan
            <span class="separator"></span>
            <span class="i-tabler-zoom-in"></span>
            wheel zoom
        </div>
    </section>
</template>

<script setup lang="ts">
import { computed, onMounted, onUnmounted, reactive, ref, shallowRef } from 'vue'

type BodyKind = 'dark' | 'gas' | 'star' | 'remnant' | 'blackHole'
type StarType = 'none' | 'red' | 'yellow' | 'blue' | 'giant'
type StarStage = 'none' | 'mainSequence' | 'giantShell' | 'heliumBurning' | 'lateBurning'
type RemnantType = 'none' | 'whiteDwarf' | 'neutronStar'
type RegionEvent = 'birth' | 'death' | 'merger' | 'manual'
type ViewMode = 'matter' | 'temperature' | 'elements' | 'gravity' | 'systems'
type PresetId = 'uniform' | 'nursery' | 'mature' | 'metal'

type ElementMix = {
    h: number
    he: number
    cno: number
    rock: number
    iron: number
}

type RegionMemory = {
    id: number
    x: number
    y: number
    radius: number
    elements: ElementMix
    generation: number
    births: number
    deaths: number
    mergerBursts: number
    feedback: number
    mass: number
    spin: number
    virialSupport: number
    spiralPhase: number
    diskSettling: number
}

type UniverseBody = {
    id: number
    kind: BodyKind
    starType: StarType
    starStage: StarStage
    remnantType: RemnantType
    x: number
    y: number
    vx: number
    vy: number
    mass: number
    birthMass: number
    radius: number
    density: number
    temperature: number
    age: number
    lifetime: number
    luminosity: number
    flash: number
    planets: number
    diskMass: number
    systemStability: number
    planetSeed: number
    spin: number
    elements: ElementMix
    regionId: number
    generation: number
    birthMetallicity: number
}

const TAU = Math.PI * 2
const WORLD_RADIUS = 2400
const MAX_BODIES = 980

const shellRef = ref<HTMLElement | null>(null)
const canvasRef = ref<HTMLCanvasElement | null>(null)
const bodies = shallowRef<UniverseBody[]>([])
const regions = shallowRef<RegionMemory[]>([])
const isRunning = ref(true)
const viewMode = ref<ViewMode>('matter')
const selectedPreset = ref<PresetId>('uniform')
const simTick = ref(0)
const cosmicAgeGyr = ref(0.22)

const camera = reactive({
    x: 0,
    y: 0,
    zoom: 0.58,
})

const settings = reactive({
    gravity: 0.3,
    pressure: 0.58,
    radiationPressure: 0.95,
    cooling: 0.72,
    starThreshold: 0.72,
    fusion: 0.58,
    feedback: 0.84,
    angularSupport: 0.92,
    spiralStrength: 0.72,
    planetFormation: 1.05,
    timeScale: 1.45,
    darkMatter: true,
    pressureForces: true,
    stellarFeedback: true,
    compactMergers: true,
    blackHoles: false,
    showPlanets: true,
    mttOverlay: true,
})

const presets: Array<{ id: PresetId, short: string, label: string }> = [
    { id: 'uniform', short: 'BB', label: 'uniform seed' },
    { id: 'nursery', short: 'SF', label: 'stellar nursery' },
    { id: 'mature', short: 'MW', label: 'mature galaxy' },
    { id: 'metal', short: 'Fe', label: 'metal rich' },
]

const viewModes: Array<{ id: ViewMode, label: string, icon: string }> = [
    { id: 'matter', label: 'Matter', icon: 'i-tabler-circles' },
    { id: 'temperature', label: 'Temp', icon: 'i-tabler-temperature' },
    { id: 'elements', label: 'Elements', icon: 'i-tabler-atom' },
    { id: 'gravity', label: 'Gravity', icon: 'i-tabler-capture' },
    { id: 'systems', label: 'Systems', icon: 'i-tabler-orbit' },
]

let context: CanvasRenderingContext2D | null = null
let width = 1
let height = 1
let dpr = 1
let animationFrame = 0
let lastTimestamp = 0
let nextBodyId = 1
let nextRegionId = 1
let rngState = 0x9e3779b9

const panState = {
    active: false,
    pointerId: -1,
    lastX: 0,
    lastY: 0,
}

const stats = computed(() => {
    simTick.value
    const result = {
        totalMass: 0,
        gas: 0,
        stars: 0,
        remnants: 0,
        whiteDwarfs: 0,
        neutronStars: 0,
        blackHoles: 0,
        dark: 0,
        planets: 0,
        protoDisks: 0,
        lateBurners: 0,
        enrichedRegions: 0,
        rotatingRegions: 0,
        spiralRegions: 0,
        maxRegionMetallicity: 0,
        maxGeneration: 0,
        secondGenerationStars: 0,
        meanMetallicity: 0,
        stableSystems: 0,
        elements: { h: 0, he: 0, cno: 0, rock: 0, iron: 0 } as ElementMix,
    }

    for (const body of bodies.value) {
        result.totalMass += body.mass
        if (body.kind === 'gas') result.gas += 1
        if (body.kind === 'star') result.stars += 1
        if (body.kind === 'star' && body.generation > 1) result.secondGenerationStars += 1
        result.maxGeneration = Math.max(result.maxGeneration, body.generation)
        if (body.kind === 'star' && body.starStage === 'lateBurning') result.lateBurners += 1
        if (body.kind === 'remnant') {
            result.remnants += 1
            if (body.remnantType === 'whiteDwarf') result.whiteDwarfs += 1
            if (body.remnantType === 'neutronStar') result.neutronStars += 1
        }
        if (body.kind === 'blackHole') result.blackHoles += 1
        if (body.kind === 'dark') result.dark += 1
        result.planets += body.planets
        if (body.diskMass > 0.45) result.protoDisks += 1
        if (body.planets > 0 || (body.diskMass > 0.65 && body.systemStability > 0.5)) result.stableSystems += 1
        result.elements.h += body.elements.h * body.mass
        result.elements.he += body.elements.he * body.mass
        result.elements.cno += body.elements.cno * body.mass
        result.elements.rock += body.elements.rock * body.mass
        result.elements.iron += body.elements.iron * body.mass
    }

    const baryonicMass = Math.max(1e-6, result.totalMass - bodies.value.filter((body) => body.kind === 'dark').reduce((sum, body) => sum + body.mass, 0))
    const metals = result.elements.cno + result.elements.rock + result.elements.iron
    result.meanMetallicity = metals / baryonicMass

    for (const key of Object.keys(result.elements) as Array<keyof ElementMix>) {
        result.elements[key] /= Math.max(1e-6, baryonicMass)
    }

    for (const region of regions.value) {
        const metallicity = metalFraction(region.elements)
        if (metallicity > 0.003 || region.generation > 1 || region.births > 0) result.enrichedRegions += 1
        if (Math.abs(region.spin) > 0.16 && region.virialSupport > 0.24) result.rotatingRegions += 1
        if (region.diskSettling > 0.42 && Math.abs(region.spin) > 0.18) result.spiralRegions += 1
        result.maxRegionMetallicity = Math.max(result.maxRegionMetallicity, metallicity)
        result.maxGeneration = Math.max(result.maxGeneration, region.generation)
    }

    return result
})

const metricCards = computed(() => [
    { label: 'age', value: formatAge(cosmicAgeGyr.value) },
    { label: 'radiation', value: `${Math.round(currentRadiationPressure() * 100)}%` },
    { label: 'bodies', value: bodies.value.length.toString() },
    { label: 'gas', value: stats.value.gas.toString() },
    { label: 'stars', value: stats.value.stars.toString() },
    { label: 'late burners', value: stats.value.lateBurners.toString() },
    { label: 'white dwarfs', value: stats.value.whiteDwarfs.toString() },
    { label: 'neutron stars', value: stats.value.neutronStars.toString() },
    { label: 'black holes', value: stats.value.blackHoles.toString() },
    { label: 'proto disks', value: stats.value.protoDisks.toString() },
    { label: 'gen 2+ stars', value: stats.value.secondGenerationStars.toString() },
    { label: 'systems', value: stats.value.stableSystems.toString() },
    { label: 'planets', value: stats.value.planets.toString() },
    { label: 'metallicity', value: `${(stats.value.meanMetallicity * 100).toFixed(2)}%` },
])

const elementLedger = computed(() => {
    const entries: Array<{ key: keyof ElementMix, label: string }> = [
        { key: 'h', label: 'hydrogen' },
        { key: 'he', label: 'helium' },
        { key: 'cno', label: 'CNO' },
        { key: 'rock', label: 'rock/silicate' },
        { key: 'iron', label: 'iron peak' },
    ]

    return entries.map((entry) => {
        const value = stats.value.elements[entry.key]
        return {
            key: entry.key,
            label: entry.label,
            value: value < 0.001 ? `${(value * 10000).toFixed(2)} bp` : `${(value * 100).toFixed(2)}%`,
            width: `${Math.max(2, Math.min(100, value * 120))}%`,
        }
    })
})

const stateSummary = computed(() => {
    const radiation = currentRadiationPressure()
    if (radiation > 0.45 && stats.value.stars === 0) return 'The early universe is still radiation-supported: hot H/He gas is resisting collapse while dark-matter wells gather it locally.'
    if (stats.value.stars === 0) return 'The universe is still mostly gas and dark-matter structure. Collapse needs dense, cool pockets before stars ignite.'
    if (stats.value.secondGenerationStars > 12 && stats.value.enrichedRegions > 3) return 'Local chemical memory is active: enriched regions are forming later-generation stars with higher metal cooling and better planet odds.'
    if (stats.value.neutronStars > 1 && stats.value.meanMetallicity > 0.055) return 'Compact remnants have started feeding the heavy-element channel. This is where neutron-star mergers add rare iron-rich bursts.'
    if (stats.value.blackHoles > 0 && stats.value.meanMetallicity > 0.035) return 'Several stellar generations have run. Metals, remnants, black holes, and planet-capable systems are now visible.'
    if (stats.value.meanMetallicity > 0.012) return 'Fusion and supernova feedback are enriching the gas. Planet systems can start appearing around calmer stars.'
    return 'First stars are forming from cold dense gas. Heavy elements remain rare until massive stars die.'
})

const regionMemoryRows = computed(() => {
    simTick.value
    const richest = regions.value.reduce<RegionMemory | null>((best, region) => {
        if (!best) return region
        return metalFraction(region.elements) > metalFraction(best.elements) ? region : best
    }, null)

    return [
        { label: 'active regions', value: `${stats.value.enrichedRegions}/${regions.value.length}` },
        { label: 'richest metals', value: richest ? `${(metalFraction(richest.elements) * 100).toFixed(2)}%` : '0.00%' },
        { label: 'max generation', value: stats.value.maxGeneration.toString() },
        { label: 'rotating regions', value: stats.value.rotatingRegions.toString() },
        { label: 'spiral regions', value: stats.value.spiralRegions.toString() },
        { label: 'region births', value: regions.value.reduce((sum, region) => sum + region.births, 0).toString() },
        { label: 'death imprints', value: regions.value.reduce((sum, region) => sum + region.deaths, 0).toString() },
        { label: 'merger imprints', value: regions.value.reduce((sum, region) => sum + region.mergerBursts, 0).toString() },
    ]
})

onMounted(() => {
    resizeCanvas()
    applyPreset('uniform')
    window.addEventListener('resize', resizeCanvas)
    animationFrame = requestAnimationFrame(loop)
})

onUnmounted(() => {
    window.removeEventListener('resize', resizeCanvas)
    cancelAnimationFrame(animationFrame)
})

function toggleRunning() {
    isRunning.value = !isRunning.value
}

function stepOnce() {
    for (let i = 0; i < 4; i += 1) stepSimulation(1 / 60)
    draw()
}

function applyPreset(id: PresetId) {
    selectedPreset.value = id
    rngState = hashPreset(id)
    nextBodyId = 1
    nextRegionId = 1
    camera.x = 0
    camera.y = 0
    camera.zoom = id === 'mature' || id === 'metal' ? 0.5 : 0.38

    if (id === 'uniform') {
        cosmicAgeGyr.value = 0.035
        Object.assign(settings, {
            gravity: 0.28,
            pressure: 0.62,
            radiationPressure: 1.08,
            cooling: 0.72,
            starThreshold: 0.66,
            fusion: 0.62,
            feedback: 0.5,
            angularSupport: 1.02,
            spiralStrength: 0.38,
            planetFormation: 0.8,
            timeScale: 1.62,
            compactMergers: true,
            blackHoles: false,
        })
        bodies.value = createUniformUniverse()
    }

    if (id === 'nursery') {
        cosmicAgeGyr.value = 0.9
        Object.assign(settings, {
            gravity: 0.34,
            pressure: 0.56,
            radiationPressure: 0.32,
            cooling: 0.88,
            starThreshold: 0.46,
            fusion: 0.72,
            feedback: 0.92,
            angularSupport: 1.08,
            spiralStrength: 0.62,
            planetFormation: 1.05,
            timeScale: 1.42,
            compactMergers: true,
            blackHoles: false,
        })
        bodies.value = createNurseryUniverse()
    }

    if (id === 'mature') {
        cosmicAgeGyr.value = 6.8
        Object.assign(settings, {
            gravity: 0.3,
            pressure: 0.55,
            radiationPressure: 0.04,
            cooling: 0.62,
            starThreshold: 0.7,
            fusion: 0.54,
            feedback: 0.74,
            angularSupport: 0.92,
            spiralStrength: 1.02,
            planetFormation: 1.34,
            timeScale: 1.05,
            compactMergers: true,
            blackHoles: false,
        })
        bodies.value = createMatureUniverse(false)
    }

    if (id === 'metal') {
        cosmicAgeGyr.value = 9.7
        Object.assign(settings, {
            gravity: 0.28,
            pressure: 0.54,
            radiationPressure: 0.02,
            cooling: 0.76,
            starThreshold: 0.62,
            fusion: 0.62,
            feedback: 0.78,
            angularSupport: 0.96,
            spiralStrength: 1.1,
            planetFormation: 1.48,
            timeScale: 0.98,
            compactMergers: true,
            blackHoles: false,
        })
        bodies.value = createMatureUniverse(true)
    }

    regions.value = createRegionMemory(bodies.value, id)
    assignBodiesToRegions(bodies.value)
    primeRegionMemoryFromBodies(bodies.value)
    simTick.value += 1
    draw()
}

function resetSimulation() {
    applyPreset(selectedPreset.value)
}

function createUniformUniverse() {
    const next: UniverseBody[] = []
    const haloCount = 18
    const darkCount = 320
    const gasCount = 640
    const halos = Array.from({ length: haloCount }, (_, i) => {
        const p = seededUniformFieldPoint(i, haloCount, WORLD_RADIUS * 0.92, 0.42)
        return {
            x: p.x,
            y: p.y,
            radius: randBetween(130, 280),
            gasRadius: randBetween(210, 430),
            spin: rand() > 0.5 ? 1 : -1,
            weight: randBetween(0.72, 1.45),
        }
    })

    for (let i = 0; i < darkCount; i += 1) {
        const halo = halos[i % haloCount]
        const haloSeeded = rand() < 0.78
        const p = haloSeeded
            ? haloScatterPoint(halo.x, halo.y, halo.radius)
            : seededUniformFieldPoint(i, darkCount, WORLD_RADIUS * 1.08, 0.18)
        const flow = localVortexFlow(p.x, p.y, 0.09)
        const orbit = haloSeeded ? swirlVelocity(p.x - halo.x, p.y - halo.y, 0.00042 * halo.spin * halo.weight) : { vx: 0, vy: 0 }
        next.push(createBody({
            kind: 'dark',
            x: p.x,
            y: p.y,
            vx: orbit.vx + flow.vx + Math.sin(p.y * 0.004) * 0.03 + randBetween(-0.08, 0.08),
            vy: orbit.vy + flow.vy + Math.cos(p.x * 0.004) * 0.03 + randBetween(-0.08, 0.08),
            mass: haloSeeded ? randBetween(13, 31) * halo.weight : randBetween(7, 14),
            radius: haloSeeded ? randBetween(4, 8) : randBetween(3, 5.5),
            temperature: 22,
            elements: primordialElements(0),
        }))
    }

    for (let i = 0; i < gasCount; i += 1) {
        const halo = halos[(i * 7) % haloCount]
        const haloFed = rand() < 0.66
        const p = haloFed
            ? haloScatterPoint(halo.x, halo.y, halo.gasRadius)
            : seededUniformFieldPoint(i, gasCount, WORLD_RADIUS * 1.04, 0.32)
        const wave = Math.sin(p.x * 0.0038) + Math.cos(p.y * 0.0034)
        const flow = localVortexFlow(p.x, p.y, 0.16)
        const orbit = haloFed ? swirlVelocity(p.x - halo.x, p.y - halo.y, 0.00062 * halo.spin * halo.weight) : { vx: 0, vy: 0 }
        next.push(createBody({
            kind: 'gas',
            x: p.x + wave * 10,
            y: p.y - wave * 7,
            vx: orbit.vx + flow.vx + Math.sin(p.y * 0.006 + wave) * 0.08 + randBetween(-0.16, 0.16),
            vy: orbit.vy + flow.vy + Math.cos(p.x * 0.006 - wave) * 0.08 + randBetween(-0.16, 0.16),
            mass: haloFed ? randBetween(3, 7.6) : randBetween(2.1, 5.3),
            radius: randBetween(5.5, 11),
            density: haloFed ? randBetween(0.18, 0.42) : randBetween(0.07, 0.2),
            temperature: haloFed ? randBetween(5200, 15500) : randBetween(8200, 24000),
            elements: primordialElements(0.00005),
        }))
    }

    return next
}

function createNurseryUniverse() {
    const next = createUniformUniverse()
    for (let c = 0; c < 7; c += 1) {
        addGasCluster(next, randBetween(-760, 760), randBetween(-520, 520), randBetween(46, 72), randBetween(130, 230), 0.002)
    }
    for (let i = 0; i < next.length; i += 1) {
        const body = next[i]
        if (body.kind === 'gas' && rand() < 0.14) convertGasToStar(body, body.density + 0.8)
    }
    return next.slice(0, MAX_BODIES)
}

function createMatureUniverse(metalRich: boolean) {
    const next: UniverseBody[] = []
    const arms = 4
    for (let i = 0; i < 210; i += 1) {
        const p = spiralPoint(i, 210, arms, WORLD_RADIUS * 0.82, randBetween(-135, 135))
        const orbit = circularVelocity(p.x, p.y, 0.42)
        next.push(createBody({
            kind: 'dark',
            x: p.x * 1.08,
            y: p.y * 1.08,
            vx: orbit.vx * 0.35,
            vy: orbit.vy * 0.35,
            mass: randBetween(8, 20),
            radius: randBetween(3, 7),
            temperature: 20,
            elements: primordialElements(0),
        }))
    }

    for (let i = 0; i < 340; i += 1) {
        const p = spiralPoint(i, 340, arms, WORLD_RADIUS * 0.76, randBetween(-105, 105))
        const orbit = circularVelocity(p.x, p.y, 0.62)
        const metal = metalRich ? randBetween(0.025, 0.085) : randBetween(0.004, 0.025)
        const makeStar = rand() < (metalRich ? 0.62 : 0.48)
        const body = createBody({
            kind: makeStar ? 'star' : 'gas',
            starType: 'yellow',
            x: p.x,
            y: p.y,
            vx: orbit.vx + randBetween(-0.08, 0.08),
            vy: orbit.vy + randBetween(-0.08, 0.08),
            mass: makeStar ? randBetween(3.4, 13) : randBetween(2.2, 6.2),
            radius: makeStar ? randBetween(3, 8) : randBetween(5, 11),
            density: makeStar ? 1 : randBetween(0.12, 0.28),
            temperature: makeStar ? randBetween(3400, 9600) : randBetween(170, 900),
            elements: enrichedElements(metal),
        })
        if (makeStar) {
            tuneStar(body)
            body.age = randBetween(0.08, body.lifetime * 0.72)
            updateStarStage(body)
            updateStarAppearance(body, 1)
            const planetMaterial = body.elements.rock + body.elements.iron + body.elements.cno * 0.25
            const calmHost = body.starType === 'red' || body.starType === 'yellow'
            if (calmHost && planetMaterial > 0.012 && rand() < (metalRich ? 0.78 : 0.58)) body.planets = Math.floor(randBetween(2, metalRich ? 10 : 8))
            body.diskMass = body.planets > 0 ? randBetween(1.2, metalRich ? 7.5 : 5.8) : randBetween(0.18, calmHost ? 1.2 : 0.5)
            body.systemStability = body.planets > 0 ? randBetween(0.68, 0.96) : randBetween(0.16, calmHost ? 0.56 : 0.34)
        }
        next.push(body)
    }

    for (let i = 0; i < (metalRich ? 14 : 8); i += 1) {
        const p = seededDiskPoint(WORLD_RADIUS * 0.38)
        const isHole = settings.blackHoles && i < 2 && metalRich
        const remnantType: RemnantType = isHole ? 'none' : i % 3 === 0 ? 'neutronStar' : 'whiteDwarf'
        const body = createBody({
            kind: isHole ? 'blackHole' : 'remnant',
            remnantType,
            x: p.x,
            y: p.y,
            vx: randBetween(-0.1, 0.1),
            vy: randBetween(-0.1, 0.1),
            mass: isHole ? randBetween(26, 80) : remnantType === 'neutronStar' ? randBetween(1.4, 2.2) : randBetween(0.8, 1.35),
            radius: isHole ? 9 : remnantType === 'neutronStar' ? 2.8 : 3.6,
            density: 3,
            temperature: isHole ? 1e7 : remnantType === 'neutronStar' ? 4.5e5 : 13000,
            elements: enrichedElements(metalRich ? 0.12 : 0.04),
        })
        next.push(body)
    }

    return next
}

function createRegionMemory(list: UniverseBody[], preset: PresetId) {
    const next: RegionMemory[] = []
    const count = preset === 'uniform' ? 16 : preset === 'nursery' ? 22 : 26
    const anchors = list
        .slice()
        .sort((a, b) => regionAnchorScore(b) - regionAnchorScore(a))

    for (let i = 0; i < count; i += 1) {
        const anchor = anchors[i * Math.max(1, Math.floor(anchors.length / count))]
        const point = anchor ? { x: anchor.x + randBetween(-42, 42), y: anchor.y + randBetween(-42, 42) } : seededDiskPoint(WORLD_RADIUS * 0.72)
        const seededMetal = preset === 'metal' ? randBetween(0.018, 0.05) : preset === 'mature' ? randBetween(0.004, 0.018) : preset === 'nursery' ? randBetween(0.0004, 0.004) : 0.00002
        next.push({
            id: nextRegionId += 1,
            x: point.x,
            y: point.y,
            radius: preset === 'uniform' ? randBetween(230, 360) : randBetween(190, 330),
            elements: anchor ? normalizeElements({ ...anchor.elements }) : enrichedElements(seededMetal),
            generation: preset === 'metal' ? 2 : 1,
            births: 0,
            deaths: 0,
            mergerBursts: 0,
            feedback: 0,
            mass: 0,
            spin: anchor ? clamp((anchor.x * anchor.vy - anchor.y * anchor.vx) / Math.max(80, Math.hypot(anchor.x, anchor.y) * 0.5), -1, 1) : randBetween(-0.45, 0.45),
            virialSupport: preset === 'uniform' ? randBetween(0.12, 0.38) : randBetween(0.32, 0.68),
            spiralPhase: rand() * TAU,
            diskSettling: preset === 'mature' || preset === 'metal' ? randBetween(0.48, 0.82) : preset === 'nursery' ? randBetween(0.18, 0.44) : randBetween(0.06, 0.28),
        })
    }

    return next
}

function assignBodiesToRegions(list: UniverseBody[]) {
    for (const body of list) {
        const region = nearestRegion(body.x, body.y)
        body.regionId = region?.id || 0
        if (region && body.kind !== 'dark') {
            body.generation = Math.max(body.generation, region.generation)
            body.birthMetallicity = body.birthMetallicity || metalFraction(region.elements)
        }
    }
}

function primeRegionMemoryFromBodies(list: UniverseBody[]) {
    for (const region of regions.value) {
        region.mass = 0
        region.births = 0
        region.deaths = 0
        region.mergerBursts = 0
        region.feedback = 0
    }

    for (const body of list) {
        const region = regionById(body.regionId) || nearestRegion(body.x, body.y)
        if (!region) continue
        const influence = regionInfluence(region, body.x, body.y)
        if (body.kind !== 'dark') blendElements(region.elements, body.elements, 0.02 + influence * 0.05)
        region.mass += body.mass * influence * (body.kind === 'dark' ? 0.72 : 1)
        if (body.kind === 'star') {
            region.births += 1
            region.generation = Math.max(region.generation, body.generation)
        }
        if (body.kind === 'remnant' || body.kind === 'blackHole') region.deaths += 1
    }
}

function evolveRegionMemory(dt: number) {
    for (const region of regions.value) {
        region.feedback = Math.max(0, region.feedback - dt * (0.35 + region.feedback * 0.08))
        region.mass *= 0.999
        region.spin = clamp(region.spin * (1 - dt * 0.01), -1, 1)
        region.virialSupport = clamp(mix(region.virialSupport, 0.18, clamp(dt * 0.018, 0, 0.03)), 0, 1)
        region.diskSettling = clamp(mix(region.diskSettling, region.virialSupport * (0.55 + Math.abs(region.spin) * 0.38), clamp(dt * 0.024, 0, 0.04)), 0, 1)
        region.spiralPhase += dt * (0.18 + region.virialSupport * 0.28) * (region.spin < 0 ? -1 : 1)
    }
}

function updateBodyRegion(body: UniverseBody) {
    const current = regionById(body.regionId)
    if (current && regionInfluence(current, body.x, body.y) > 0.03) return current
    const nearest = nearestRegion(body.x, body.y)
    body.regionId = nearest?.id || 0
    return nearest
}

function exchangeBodyWithRegion(body: UniverseBody, region: RegionMemory, dt: number) {
    const influence = regionInfluence(region, body.x, body.y)
    if (influence <= 0) return
    const dx = body.x - region.x
    const dy = body.y - region.y
    const dist = Math.max(8, Math.hypot(dx, dy))
    const radialVelocity = (dx * body.vx + dy * body.vy) / dist
    const tangentialVelocity = (dx * body.vy - dy * body.vx) / dist
    const spinSample = clamp(tangentialVelocity / Math.max(0.08, Math.sqrt(dist) * 0.026), -1, 1)
    const supportSample = clamp(Math.abs(tangentialVelocity) / (0.08 + Math.abs(tangentialVelocity) + Math.abs(radialVelocity)), 0, 1)
    const memoryWeight = clamp(dt * influence * (body.kind === 'gas' ? 0.14 : 0.07), 0, 0.045)
    region.spin = mix(region.spin, spinSample, memoryWeight)
    region.virialSupport = mix(region.virialSupport, supportSample, clamp(memoryWeight * 1.4, 0, 0.06))
    const diskSample = clamp(supportSample * (1 - Math.min(0.75, Math.abs(radialVelocity) / (0.18 + Math.abs(tangentialVelocity) + 0.001))), 0, 1)
    region.diskSettling = mix(region.diskSettling, diskSample, clamp(memoryWeight * (body.kind === 'gas' || body.kind === 'star' ? 1.8 : 0.7), 0, 0.08))
    if (body.kind !== 'dark') {
        region.x = mix(region.x, body.x, clamp(dt * influence * 0.008, 0, 0.006))
        region.y = mix(region.y, body.y, clamp(dt * influence * 0.008, 0, 0.006))
    }
    if (body.kind === 'gas') {
        const readWeight = clamp(dt * influence * (0.02 + metalFraction(region.elements) * 0.08), 0, 0.08)
        blendElements(body.elements, region.elements, readWeight)
        body.generation = Math.max(body.generation, region.generation)
        body.birthMetallicity = Math.max(body.birthMetallicity, metalFraction(body.elements), metalFraction(region.elements))
    }
    if (body.kind === 'star') {
        region.generation = Math.max(region.generation, body.generation)
    }
    region.mass = mix(region.mass, region.mass + body.mass * influence * 0.01, clamp(dt * 0.8, 0, 0.2))
}

function applyLocalAngularSupport(body: UniverseBody, region: RegionMemory, dt: number) {
    if (settings.angularSupport <= 0) return
    const influence = regionInfluence(region, body.x, body.y)
    if (influence <= 0.01) return

    const dx = body.x - region.x
    const dy = body.y - region.y
    const dist = Math.max(10, Math.hypot(dx, dy))
    const rx = dx / dist
    const ry = dy / dist
    const tx = -ry
    const ty = rx
    const radialVelocity = body.vx * rx + body.vy * ry
    const tangentialVelocity = body.vx * tx + body.vy * ty
    const spinSign = region.spin < 0 ? -1 : 1
    const support = settings.angularSupport * influence * clamp(0.2 + Math.abs(region.spin) * 0.75 + region.virialSupport * 0.95, 0, 1.35)
    if (support <= 0) return

    const enclosedMass = Math.max(3, region.mass * (0.45 + influence) + body.mass * 1.6)
    const targetTangential = spinSign * clamp(Math.sqrt(enclosedMass) * 0.018 * Math.sqrt(region.radius / Math.max(50, dist)), 0.018, 0.72)
    const kindResponse = body.kind === 'gas' ? 1 : body.kind === 'dark' ? 0.42 : 0.58
    const tangentialCorrection = clamp((targetTangential - tangentialVelocity) * support * kindResponse * dt, -0.055, 0.055)
    body.vx += tx * tangentialCorrection
    body.vy += ty * tangentialCorrection

    if (radialVelocity < 0) {
        const brake = clamp(-radialVelocity * support * kindResponse * dt * 0.42, 0, 0.055)
        body.vx += rx * brake
        body.vy += ry * brake
        if (body.kind === 'gas') body.temperature += brake * 90
    }
}

function applySpiralDensityWave(body: UniverseBody, region: RegionMemory, dt: number) {
    if (settings.spiralStrength <= 0 || body.kind === 'dark' || body.kind === 'blackHole') return
    const influence = regionInfluence(region, body.x, body.y)
    const disk = region.diskSettling * clamp(Math.abs(region.spin) * 0.75 + region.virialSupport * 0.65, 0, 1.35)
    if (influence <= 0.04 || disk <= 0.18) return

    const dx = body.x - region.x
    const dy = body.y - region.y
    const dist = Math.max(18, Math.hypot(dx, dy))
    const angle = Math.atan2(dy, dx)
    const spinSign = region.spin < 0 ? -1 : 1
    const armCount = region.mass > 260 ? 4 : 2
    const pitch = 0.38
    const winding = Math.log(dist / 42) * pitch * spinSign
    const phase = armCount * (angle - winding) - region.spiralPhase
    const ridge = (Math.cos(phase) + 1) * 0.5
    const sharpRidge = ridge ** 5
    const wave = settings.spiralStrength * influence * disk * sharpRidge
    if (wave <= 0.0005) return

    const rx = dx / dist
    const ry = dy / dist
    const tx = -ry * spinSign
    const ty = rx * spinSign
    const kindResponse = body.kind === 'gas' ? 1 : body.kind === 'star' ? 0.36 : 0.18
    body.vx += (tx * 0.42 - rx * 0.1) * wave * kindResponse * dt
    body.vy += (ty * 0.42 - ry * 0.1) * wave * kindResponse * dt

    if (body.kind === 'gas') {
        body.density = clamp(body.density + wave * 0.18, 0, 3.2)
        body.temperature = clamp(body.temperature - wave * 18, 55, 1.5e6)
    }
    if (body.kind === 'star' && body.planets === 0 && body.diskMass > 0.3) {
        body.systemStability = clamp(body.systemStability + wave * 0.012, 0, 1)
    }
}

function applyRegionFeedbackPressure(body: UniverseBody, region: RegionMemory, dt: number) {
    const influence = regionInfluence(region, body.x, body.y)
    if (influence <= 0) return
    const dx = body.x - region.x
    const dy = body.y - region.y
    const dist = Math.max(10, Math.hypot(dx, dy))
    const strength = settings.feedback * region.feedback * influence
    body.vx += (dx / dist) * strength * dt * 0.72
    body.vy += (dy / dist) * strength * dt * 0.72
    body.temperature += strength * dt * 4200
}

function depositRegionYield(source: UniverseBody, cno: number, rock: number, iron: number, radius: number, power: number, event: RegionEvent) {
    let touched = false
    for (const region of regions.value) {
        const dist = Math.hypot(region.x - source.x, region.y - source.y)
        const strength = Math.max(0, 1 - dist / Math.max(radius, region.radius * 0.65)) * power
        if (strength <= 0) continue
        const dilution = clamp(0.035 + strength * 0.018, 0.025, 0.12) / (1 + region.mass * 0.0009)
        enrich(region.elements, cno * strength * dilution, rock * strength * dilution, iron * strength * dilution)
        region.feedback = Math.max(region.feedback, strength)
        region.generation = Math.max(region.generation, source.generation + 1)
        bumpRegionEvent(region, event)
        touched = true
    }

    if (!touched) {
        const seed = enrichedElements(Math.min(0.12, cno + rock + iron))
        const region = createOrEnrichRegion(source.x, source.y, radius * 0.55, seed, power, source.generation + 1, event)
        enrich(region.elements, cno, rock, iron)
    }
}

function createOrEnrichRegion(x: number, y: number, radius: number, elements: ElementMix, feedback: number, generation: number, event: RegionEvent) {
    const nearest = nearestRegion(x, y)
    const canUseNearest = nearest && Math.hypot(nearest.x - x, nearest.y - y) < Math.max(nearest.radius, radius) * 0.72
    const region = canUseNearest
        ? nearest
        : regions.value.length < 26
            ? pushRegion(x, y, radius, elements, generation)
            : nearest || pushRegion(x, y, radius, elements, generation)

    region.x = mix(region.x, x, 0.08)
    region.y = mix(region.y, y, 0.08)
    region.radius = clamp(Math.max(region.radius, radius * 0.82), 90, 290)
    blendElements(region.elements, elements, 0.22)
    region.feedback = Math.max(region.feedback, feedback)
    region.generation = Math.max(region.generation, generation)
    bumpRegionEvent(region, event)
    return region
}

function pushRegion(x: number, y: number, radius: number, elements: ElementMix, generation: number) {
    const region: RegionMemory = {
        id: nextRegionId += 1,
        x,
        y,
        radius: clamp(radius, 90, 290),
        elements: normalizeElements({ ...elements }),
        generation,
        births: 0,
        deaths: 0,
        mergerBursts: 0,
        feedback: 0,
        mass: 0,
        spin: randBetween(-0.4, 0.4),
        virialSupport: 0.2,
        spiralPhase: rand() * TAU,
        diskSettling: 0.16,
    }
    regions.value = [...regions.value, region]
    return region
}

function bumpRegionEvent(region: RegionMemory, event: RegionEvent) {
    if (event === 'birth') region.births += 1
    if (event === 'death') region.deaths += 1
    if (event === 'merger') region.mergerBursts += 1
    if (event === 'manual') {
        region.deaths += 1
        region.mergerBursts += 1
    }
}

function nearestRegion(x: number, y: number) {
    let best: RegionMemory | undefined
    let bestScore = Number.POSITIVE_INFINITY
    for (const region of regions.value) {
        const distance = Math.hypot(region.x - x, region.y - y)
        const score = distance / Math.max(1, region.radius)
        if (score < bestScore) {
            best = region
            bestScore = score
        }
    }
    return best
}

function regionById(id: number) {
    return regions.value.find(region => region.id === id)
}

function regionInfluence(region: RegionMemory, x: number, y: number) {
    const distance = Math.hypot(region.x - x, region.y - y)
    return clamp(1 - distance / Math.max(1, region.radius), 0, 1) ** 2
}

function regionAnchorScore(body: UniverseBody) {
    const metals = metalFraction(body.elements)
    const kindBonus = body.kind === 'star' ? 30 : body.kind === 'remnant' ? 24 : body.kind === 'blackHole' ? 18 : body.kind === 'dark' ? 20 : body.kind === 'gas' ? body.density * 12 : 0
    return body.mass + kindBonus + metals * 200
}

function addGasCluster(next: UniverseBody[], cx: number, cy: number, count: number, radius: number, metal: number) {
    for (let i = 0; i < count; i += 1) {
        const angle = rand() * TAU
        const r = Math.sqrt(rand()) * radius
        const x = cx + Math.cos(angle) * r
        const y = cy + Math.sin(angle) * r
        const orbit = swirlVelocity(x - cx, y - cy, 0.055)
        next.push(createBody({
            kind: 'gas',
            x,
            y,
            vx: orbit.vx + randBetween(-0.05, 0.05),
            vy: orbit.vy + randBetween(-0.05, 0.05),
            mass: randBetween(3.5, 8.5),
            radius: randBetween(6, 12),
            density: randBetween(0.42, 0.85),
            temperature: randBetween(120, 650),
            elements: enrichedElements(metal),
        }))
    }
}

function injectGasCloud() {
    const next = bodies.value.slice()
    const center = screenToWorld(width * 0.5, height * 0.5)
    addGasCluster(next, center.x + randBetween(-150, 150), center.y + randBetween(-110, 110), 64, 180, stats.value.meanMetallicity * 0.7)
    bodies.value = trimBodies(next)
    assignBodiesToRegions(bodies.value)
    simTick.value += 1
}

function seedHalo() {
    const next = bodies.value.slice()
    const center = screenToWorld(width * 0.5, height * 0.5)
    for (let i = 0; i < 64; i += 1) {
        const angle = rand() * TAU
        const r = 80 + rand() * 270
        const x = center.x + Math.cos(angle) * r
        const y = center.y + Math.sin(angle) * r
        const orbit = swirlVelocity(x - center.x, y - center.y, 0.035)
        next.push(createBody({
            kind: i % 3 === 0 ? 'gas' : 'dark',
            x,
            y,
            vx: orbit.vx,
            vy: orbit.vy,
            mass: i % 3 === 0 ? randBetween(4, 7) : randBetween(10, 18),
            radius: i % 3 === 0 ? randBetween(6, 10) : randBetween(3, 6),
            density: i % 3 === 0 ? 0.42 : 0,
            temperature: i % 3 === 0 ? randBetween(180, 820) : 24,
            elements: i % 3 === 0 ? enrichedElements(stats.value.meanMetallicity * 0.5) : primordialElements(0),
        }))
    }
    bodies.value = trimBodies(next)
    createOrEnrichRegion(center.x, center.y, 210, enrichedElements(stats.value.meanMetallicity * 0.7), 0.12, 1, 'birth')
    assignBodiesToRegions(bodies.value)
    simTick.value += 1
}

function triggerWave() {
    const center = screenToWorld(width * 0.5, height * 0.5)
    for (const body of bodies.value) {
        const dx = body.x - center.x
        const dy = body.y - center.y
        const dist = Math.max(12, Math.hypot(dx, dy))
        const strength = Math.max(0, 1 - dist / 520) * settings.feedback
        if (strength <= 0) continue
        body.vx += (dx / dist) * strength * 1.9
        body.vy += (dy / dist) * strength * 1.9
        if (body.kind === 'gas') body.temperature += strength * 7800
    }
    simTick.value += 1
}

function enrichRegion() {
    const center = screenToWorld(width * 0.5, height * 0.5)
    createOrEnrichRegion(center.x, center.y, 260, enrichedElements(0.055), 0.45, Math.max(2, stats.value.maxGeneration), 'manual')
    for (const body of bodies.value) {
        if (body.kind === 'dark') continue
        const dist = Math.hypot(body.x - center.x, body.y - center.y)
        const strength = Math.max(0, 1 - dist / 430)
        if (strength <= 0) continue
        enrich(body.elements, 0.018 * strength, 0.014 * strength, 0.006 * strength)
        if (body.kind === 'gas') body.temperature += strength * 1200
    }
    simTick.value += 1
}

function loop(timestamp: number) {
    const dt = lastTimestamp > 0 ? Math.min(0.033, (timestamp - lastTimestamp) / 1000) : 1 / 60
    lastTimestamp = timestamp
    if (isRunning.value) stepSimulation(dt)
    draw()
    animationFrame = requestAnimationFrame(loop)
}

function stepSimulation(frameDt: number) {
    const list = bodies.value
    const n = list.length
    if (n === 0) return

    const dt = Math.min(0.05, frameDt * settings.timeScale)
    cosmicAgeGyr.value += dt * 0.018
    const radiation = currentRadiationPressure()

    const ax = new Float32Array(n)
    const ay = new Float32Array(n)
    const density = new Float32Array(n)
    const haloDepth = new Float32Array(n)
    const compressionHeat = new Float32Array(n)
    const softening = 44
    const densityRange = 145
    const pressureRange = 60
    const gravityStrength = settings.gravity * 5.6

    for (let i = 0; i < n; i += 1) {
        const a = list[i]
        for (let j = i + 1; j < n; j += 1) {
            const b = list[j]
            const dx = b.x - a.x
            const dy = b.y - a.y
            const distSq = dx * dx + dy * dy + 0.001
            const dist = Math.sqrt(distSq)
            const invDist = 1 / dist

            if (settings.darkMatter || (a.kind !== 'dark' && b.kind !== 'dark')) {
                const g = gravityStrength / (distSq + softening * softening)
                ax[i] += dx * invDist * g * b.mass
                ay[i] += dy * invDist * g * b.mass
                ax[j] -= dx * invDist * g * a.mass
                ay[j] -= dy * invDist * g * a.mass
            }

            if (dist < densityRange) {
                const weight = (1 - dist / densityRange) ** 2
                if (a.kind === 'gas') density[i] += b.mass * weight
                if (b.kind === 'gas') density[j] += a.mass * weight
                if (a.kind === 'gas' && b.kind === 'dark') haloDepth[i] += b.mass * weight
                if (b.kind === 'gas' && a.kind === 'dark') haloDepth[j] += a.mass * weight
            }

            if (settings.pressureForces && dist < pressureRange && a.kind === 'gas' && b.kind === 'gas') {
                const overlap = (pressureRange - dist) / pressureRange
                const thermal = clamp(0.16 + (thermalPressure(a) + thermalPressure(b)) * 0.5, 0.1, 1.65)
                const localGradient = clamp(0.55 + Math.abs(a.density - b.density) * 0.16, 0.55, 1.35)
                const radiationSupport = 1 + radiation * 1.85
                const p = settings.pressure * overlap * overlap * thermal * localGradient * radiationSupport * 6.8
                ax[i] -= dx * invDist * p / Math.max(1, a.mass * 0.42)
                ay[i] -= dy * invDist * p / Math.max(1, a.mass * 0.42)
                compressionHeat[i] += p * 0.3
                ax[j] += dx * invDist * p / Math.max(1, b.mass * 0.42)
                ay[j] += dy * invDist * p / Math.max(1, b.mass * 0.42)
                compressionHeat[j] += p * 0.3
            }
        }
    }

    const swallowed = new Set<number>()
    evolveRegionMemory(dt)

    for (let i = 0; i < n; i += 1) {
        const body = list[i]
        if (body.kind === 'dark' && !settings.darkMatter) continue
        const localRegion = updateBodyRegion(body)
        if (localRegion) {
            exchangeBodyWithRegion(body, localRegion, dt)
            applyLocalAngularSupport(body, localRegion, dt)
        }

        body.density = mix(body.density, density[i] / 22, 0.08)
        if (localRegion) applySpiralDensityWave(body, localRegion, dt)

        if (body.kind === 'gas') {
            const regionMetal = localRegion ? metalFraction(localRegion.elements) : 0
            const feedbackHeat = localRegion ? localRegion.feedback * 160 : 0
            const haloCooling = clamp(haloDepth[i] / 42, 0, 1.8)
            const collapseHeat = body.density * (42 + settings.gravity * 58) + compressionHeat[i] * 128 + feedbackHeat + haloCooling * 18
            const metalCooling = 0.35 + body.elements.cno * 2.8 + body.elements.rock * 3.7 + body.elements.iron * 4.2 + regionMetal * 5.6
            const radiationFloor = 2200 + radiation * 19000
            const radiationHeat = Math.max(0, radiationFloor - body.temperature) * 0.045
            const radiativeLoss = settings.cooling * metalCooling * Math.sqrt(Math.max(1, body.temperature)) * (0.08 + body.density * 0.05 + haloCooling * 0.012)
            body.temperature = clamp(body.temperature + (collapseHeat + radiationHeat - radiativeLoss) * dt, 55, 1.5e6)
            const metalSeed = 1 + regionMetal * 3.2 + metalFraction(body.elements) * 1.4
            const feedbackBarrier = 1 + (localRegion?.feedback || 0) * 0.18
            const collapseGravity = 0.52 + settings.gravity * 0.92
            const radiationBarrier = 1 + radiation * 4.5
            const coldDense = (body.density + haloCooling * 0.18) * collapseGravity * (1.35 + body.mass * 0.08) * metalSeed / ((1 + Math.log10(body.temperature + 10) * 0.12) * feedbackBarrier * radiationBarrier)
            const starBirthTemperature = 18000 - radiation * 7000
            const starBirthChance = dt * coldDense * 0.35 * clamp(1 - radiation * 0.75, 0.08, 1)
            if (localRegion && localRegion.feedback > 0.02) applyRegionFeedbackPressure(body, localRegion, dt)
            if (coldDense > settings.starThreshold && body.temperature < starBirthTemperature && rand() < starBirthChance) {
                convertGasToStar(body, coldDense, localRegion || undefined)
            }
        }

        if (body.kind === 'star') {
            evolveStar(body, dt)
            accreteCircumstellarDisk(list, body, dt)
            if (body.age > body.lifetime) {
                finishStarLife(list, i)
            }
        }

        if (settings.blackHoles && body.kind === 'blackHole') {
            accreteIntoBlackHole(list, i, swallowed)
        }

        const boundary = WORLD_RADIUS * 1.35
        const boundaryDist = Math.hypot(body.x, body.y)
        if (boundaryDist > boundary) {
            const pull = (boundaryDist - boundary) / boundaryDist
            body.vx -= body.x * pull * 0.002
            body.vy -= body.y * pull * 0.002
        }

        body.vx += ax[i] * dt
        body.vy += ay[i] * dt
        const damping = body.kind === 'gas' ? 0.996 : 0.999
        body.vx *= damping
        body.vy *= damping
        body.x += body.vx * dt * 42
        body.y += body.vy * dt * 42
        body.flash = Math.max(0, body.flash - dt * 1.1)
        body.spin += dt * (0.3 + body.luminosity * 0.02)
    }

    if (settings.compactMergers) {
        resolveCompactMergers(list, swallowed)
    }

    if (swallowed.size > 0) bodies.value = list.filter((_, index) => !swallowed.has(index))
    if (bodies.value.length > MAX_BODIES) bodies.value = trimBodies(bodies.value)
    simTick.value += 1
}

function convertGasToStar(body: UniverseBody, collapseScore: number, region = regionById(body.regionId) || nearestRegion(body.x, body.y) || undefined) {
    const localMetal = region ? metalFraction(region.elements) : 0
    const inheritedGeneration = region ? region.generation + (localMetal > 0.002 || region.deaths > 0 ? 1 : 0) : body.generation
    body.kind = 'star'
    body.mass = clamp(body.mass * (1.12 + collapseScore * 0.22), 2.8, 35)
    body.birthMass = body.mass
    body.radius = clamp(2.5 + Math.sqrt(body.mass) * 1.25, 3, 13)
    body.density = 1.2 + collapseScore
    body.age = randBetween(0, 0.05)
    body.starStage = 'mainSequence'
    body.remnantType = 'none'
    body.generation = Math.max(1, body.generation, inheritedGeneration)
    body.birthMetallicity = Math.max(metalFraction(body.elements), localMetal)
    body.flash = 0.8
    tuneStar(body)
    body.temperature = starTemperature(body.starType, body.mass)
    body.luminosity = starLuminosity(body.starType, body.mass)
    body.vx *= 0.86
    body.vy *= 0.86
    const angularSeed = region ? clamp(Math.abs(region.spin) * 0.62 + region.virialSupport * 0.72, 0, 1.15) : 0
    const diskMaterial = clamp(0.18 + body.birthMetallicity * 18, 0.18, 1.55)
    const calmHostBoost = body.starType === 'red' || body.starType === 'yellow' ? 1.25 : 0.65
    body.diskMass = settings.showPlanets ? clamp(body.mass * angularSeed * diskMaterial * calmHostBoost * settings.planetFormation * 0.2, 0, 7.5) : 0
    body.systemStability = settings.showPlanets ? clamp(0.1 + angularSeed * 0.52 + body.birthMetallicity * 4.4 + (calmHostBoost - 0.65) * 0.16, 0, 0.88) : 0
    if (region) {
        body.regionId = region.id
        region.births += 1
        region.generation = Math.max(region.generation, body.generation)
        region.mass += body.mass
        blendElements(region.elements, body.elements, 0.035)
    }
}

function tuneStar(body: UniverseBody) {
    body.birthMass = body.birthMass || body.mass
    body.starStage = body.starStage === 'none' ? 'mainSequence' : body.starStage
    body.remnantType = 'none'
    if (body.birthMass > 18) {
        body.starType = 'giant'
        body.lifetime = randBetween(0.08, 0.28)
    }
    else if (body.birthMass > 10) {
        body.starType = 'blue'
        body.lifetime = randBetween(0.18, 0.75)
    }
    else if (body.birthMass > 5.2) {
        body.starType = 'yellow'
        body.lifetime = randBetween(3.4, 11)
    }
    else {
        body.starType = 'red'
        body.lifetime = randBetween(16, 55)
    }
}

function evolveStar(body: UniverseBody, dt: number) {
    const previousStage = body.starStage
    body.age += dt * stellarClockRate(body)
    updateStarStage(body)
    if (previousStage !== body.starStage) body.flash = 1

    burnStarFuel(body, dt)
    updateStarAppearance(body, dt)
    const metalMass = body.elements.cno + body.elements.rock + body.elements.iron
    if (settings.showPlanets && body.planets === 0 && body.starType !== 'blue' && body.starType !== 'giant' && body.age > 0.35 && metalMass > 0.012) {
        const diskFeed = clamp((metalMass - 0.01) * settings.planetFormation * (0.16 + body.systemStability * 0.28), 0, 0.08) * dt
        body.diskMass = clamp(body.diskMass + diskFeed, 0, 18)
    }
    body.flash = Math.max(0, body.flash - dt * 1.6)
}

function accreteCircumstellarDisk(list: UniverseBody[], star: UniverseBody, dt: number) {
    if (!settings.showPlanets || star.starType === 'blue' || star.starType === 'giant' || star.starStage === 'lateBurning') {
        star.systemStability = mix(star.systemStability, 0, clamp(dt * 0.35, 0, 0.2))
        star.diskMass = Math.max(0, star.diskMass - dt * 0.04)
        return
    }

    const captureRadius = clamp(95 + star.birthMass * 7 + star.birthMetallicity * 260, 90, 220)
    const region = regionById(star.regionId)
    const regionMetal = region ? metalFraction(region.elements) : 0
    const inheritedSupport = region ? clamp(region.virialSupport + Math.abs(region.spin) * 0.42, 0, 1.25) : 0
    let feed = 0
    let gasContacts = 0

    for (const gas of list) {
        if (gas.kind !== 'gas' || gas.mass < 0.7) continue
        const dx = gas.x - star.x
        const dy = gas.y - star.y
        const dist = Math.hypot(dx, dy)
        if (dist < star.radius * 3 || dist > captureRadius) continue

        const relVx = gas.vx - star.vx
        const relVy = gas.vy - star.vy
        const radialFlow = Math.abs(dx * relVx + dy * relVy) / Math.max(1, dist)
        const tangentialFlow = Math.abs(dx * relVy - dy * relVx) / Math.max(1, dist)
        const angularSupport = clamp(tangentialFlow / (0.18 + radialFlow + tangentialFlow) + inheritedSupport * 0.18, 0, 1)
        const coolGas = clamp((14000 - gas.temperature) / 14000, 0, 1)
        const metalHelp = 0.45 + (metalFraction(gas.elements) + regionMetal + star.birthMetallicity) * 7
        const influence = (1 - dist / captureRadius) ** 2
        const transfer = Math.min(Math.max(0, gas.mass - 0.55), dt * influence * angularSupport * coolGas * metalHelp * settings.cooling * settings.planetFormation * 0.28)
        if (transfer <= 0) continue

        gas.mass -= transfer * 0.55
        gas.temperature += transfer * 340
        star.diskMass += transfer
        blendElements(star.elements, gas.elements, clamp(transfer * 0.004, 0, 0.025))
        feed += transfer
        gasContacts += 1
    }

    const calmHost = star.starType === 'red' || star.starType === 'yellow'
    const diskTarget = calmHost
        ? clamp(0.24 + star.diskMass * 0.16 + star.birthMetallicity * 5.2 + Math.min(gasContacts, 8) * 0.045 + inheritedSupport * 0.24, 0, 1)
        : 0.12
    star.systemStability = mix(star.systemStability, diskTarget, clamp(dt * (0.7 + feed * 0.8), 0.02, 0.35))
    star.diskMass = clamp(star.diskMass - dt * (0.008 + star.planets * 0.004), 0, 18)

    const planetMaterial = star.birthMetallicity + metalFraction(star.elements) + regionMetal
    if (star.diskMass > 0.55 && star.systemStability > 0.36 && star.planets === 0 && planetMaterial > 0.004) {
        const chance = dt * settings.planetFormation * clamp(star.diskMass * 0.12 + planetMaterial * 1.7, 0.04, 0.85)
        if (rand() < chance) star.planets = Math.floor(randBetween(1, star.diskMass > 3.2 ? 9 : 5))
    }

    if (star.planets > 0 && star.diskMass > star.planets * 0.34 && star.systemStability > 0.5 && star.planets < 11 && planetMaterial > 0.006) {
        const chance = dt * settings.planetFormation * clamp(star.diskMass * 0.055, 0.02, 0.38)
        if (rand() < chance) star.planets += 1
    }
}

function finishStarLife(list: UniverseBody[], index: number) {
    const body = list[index]
    const fateMass = body.birthMass || body.mass
    if (fateMass > 8 && settings.stellarFeedback) {
        supernova(list, body)
    }
    else if (settings.stellarFeedback) {
        planetaryNebula(list, body)
    }

    if (fateMass > 22 && settings.blackHoles) {
        body.kind = 'blackHole'
        body.mass = clamp(fateMass * 0.34, 7, 34)
        body.radius = clamp(5 + Math.sqrt(body.mass) * 0.9, 6, 18)
        body.temperature = 1e7
        body.luminosity = 0
        body.planets = 0
        body.diskMass = 0
        body.systemStability = 0
        body.starType = 'none'
        body.starStage = 'none'
        body.remnantType = 'none'
        body.lifetime = 1e9
    }
    else if (fateMass > 8) {
        body.kind = 'remnant'
        body.remnantType = 'neutronStar'
        body.mass = clamp(1.25 + fateMass * 0.035, 1.35, settings.blackHoles ? 2.35 : 2.8)
        body.radius = 2.6
        body.temperature = 4.5e5
        body.luminosity = 0.14
        body.planets = 0
        body.diskMass = 0
        body.systemStability = 0
        body.starType = 'none'
        body.starStage = 'none'
        body.lifetime = 1e9
        body.flash = 1
    }
    else {
        body.kind = 'remnant'
        body.remnantType = 'whiteDwarf'
        body.mass = clamp(0.52 + fateMass * 0.09, 0.56, 1.38)
        body.radius = 3.7
        body.temperature = 13000 + fateMass * 900
        body.luminosity = 0.06
        body.planets = 0
        body.diskMass = 0
        body.systemStability = 0
        body.starType = 'none'
        body.starStage = 'none'
        body.lifetime = 1e9
        body.flash = 0.55
    }
    normalizeElements(body.elements)
}

function supernova(list: UniverseBody[], source: UniverseBody) {
    const yields = supernovaYields(source)
    const power = settings.feedback * yields.power
    enrich(source.elements, yields.cno, yields.rock, yields.iron)
    depositRegionYield(source, yields.cno, yields.rock, yields.iron, yields.radius, power, 'death')
    for (const body of list) {
        if (body.id === source.id || body.kind === 'dark') continue
        const dx = body.x - source.x
        const dy = body.y - source.y
        const dist = Math.max(16, Math.hypot(dx, dy))
        const strength = Math.max(0, 1 - dist / yields.radius) * power
        if (strength <= 0) continue
        body.vx += (dx / dist) * strength * 2.85
        body.vy += (dy / dist) * strength * 2.85
        body.flash = Math.max(body.flash, strength)
        if (body.kind === 'gas') body.temperature += strength * 165000
        enrich(body.elements, yields.cno * 0.22 * strength, yields.rock * 0.24 * strength, yields.iron * 0.2 * strength)
    }
}

function planetaryNebula(list: UniverseBody[], source: UniverseBody) {
    const power = settings.feedback * clamp(source.birthMass / 6, 0.15, 0.8)
    enrich(source.elements, 0.028 * power, 0.01 * power, 0.0015 * power)
    depositRegionYield(source, 0.028 * power, 0.01 * power, 0.0015 * power, 210, power, 'death')
    for (const body of list) {
        if (body.id === source.id || body.kind !== 'gas') continue
        const dx = body.x - source.x
        const dy = body.y - source.y
        const dist = Math.max(14, Math.hypot(dx, dy))
        const strength = Math.max(0, 1 - dist / 210) * power
        if (strength <= 0) continue
        body.vx += (dx / dist) * strength * 0.72
        body.vy += (dy / dist) * strength * 0.72
        body.temperature += strength * 9000
        body.flash = Math.max(body.flash, strength * 0.35)
        enrich(body.elements, 0.012 * strength, 0.0035 * strength, 0.0005 * strength)
    }
}

function resolveCompactMergers(list: UniverseBody[], swallowed: Set<number>) {
    for (let i = 0; i < list.length; i += 1) {
        const a = list[i]
        if (swallowed.has(i) || a.kind !== 'remnant' || a.remnantType !== 'neutronStar') continue
        for (let j = i + 1; j < list.length; j += 1) {
            const b = list[j]
            if (swallowed.has(j) || b.kind !== 'remnant' || b.remnantType !== 'neutronStar') continue
            const dx = b.x - a.x
            const dy = b.y - a.y
            const dist = Math.hypot(dx, dy)
            const capture = 20 + (a.mass + b.mass) * 4
            if (dist > capture) continue
            const relativeSpeed = Math.hypot(a.vx - b.vx, a.vy - b.vy)
            if (relativeSpeed > 2.8 && rand() > 0.25) continue

            swallowed.add(j)
            a.kind = settings.blackHoles && a.mass + b.mass > 3.05 ? 'blackHole' : 'remnant'
            a.remnantType = a.kind === 'blackHole' ? 'none' : 'neutronStar'
            a.mass = a.kind === 'blackHole' ? (a.mass + b.mass) * 0.86 : a.mass + b.mass * 0.72
            a.radius = a.kind === 'blackHole' ? clamp(5 + Math.sqrt(a.mass) * 0.9, 7, 16) : 3
            a.temperature = 1.2e7
            a.luminosity = 0
            a.flash = 1.6
            a.vx = (a.vx * a.mass + b.vx * b.mass) / Math.max(1e-6, a.mass + b.mass)
            a.vy = (a.vy * a.mass + b.vy * b.mass) / Math.max(1e-6, a.mass + b.mass)
            enrich(a.elements, 0.018, 0.052, 0.07)
            compactMergerBurst(list, a)
            break
        }
    }
}

function compactMergerBurst(list: UniverseBody[], source: UniverseBody) {
    const power = settings.feedback * 1.45
    depositRegionYield(source, 0.012, 0.052, 0.085, 270, power, 'merger')
    for (const body of list) {
        if (body.id === source.id || body.kind === 'dark') continue
        const dx = body.x - source.x
        const dy = body.y - source.y
        const dist = Math.max(12, Math.hypot(dx, dy))
        const strength = Math.max(0, 1 - dist / 270) * power
        if (strength <= 0) continue
        body.vx += (dx / dist) * strength * 1.75
        body.vy += (dy / dist) * strength * 1.75
        body.flash = Math.max(body.flash, strength)
        if (body.kind === 'gas') body.temperature += strength * 90000
        enrich(body.elements, 0.006 * strength, 0.024 * strength, 0.036 * strength)
    }
}

function stellarClockRate(body: UniverseBody) {
    const massRate = clamp(Math.sqrt(body.birthMass) * 0.18, 0.22, 1.65)
    if (body.starStage === 'lateBurning') return 0.9 + massRate * 1.2
    if (body.starStage === 'heliumBurning') return 0.62 + massRate * 0.7
    if (body.starStage === 'giantShell') return 0.45 + massRate * 0.42
    return 0.3 + massRate
}

function updateStarStage(body: UniverseBody) {
    const progress = stellarProgress(body)
    if (progress < 0.7) body.starStage = 'mainSequence'
    else if (progress < 0.84) body.starStage = 'giantShell'
    else if (progress < 0.96) body.starStage = 'heliumBurning'
    else body.starStage = 'lateBurning'
}

function burnStarFuel(body: UniverseBody, dt: number) {
    const rate = dt * settings.fusion * (0.0011 + body.birthMass * 0.00072)
    if (body.starStage === 'mainSequence') {
        const moved = transmute(body.elements, 'h', 'he', rate)
        if (body.birthMass > 10) transmute(body.elements, 'he', 'cno', moved * 0.08)
    }

    if (body.starStage === 'giantShell') {
        transmute(body.elements, 'h', 'he', rate * 0.62)
        transmute(body.elements, 'he', 'cno', rate * (body.birthMass > 4 ? 0.42 : 0.2))
    }

    if (body.starStage === 'heliumBurning') {
        transmute(body.elements, 'he', 'cno', rate * 0.9)
        if (body.birthMass > 7) transmute(body.elements, 'cno', 'rock', rate * 0.36)
    }

    if (body.starStage === 'lateBurning') {
        transmute(body.elements, 'he', 'cno', rate * 0.34)
        if (body.birthMass > 8) transmute(body.elements, 'cno', 'rock', rate * 0.82)
        if (body.birthMass > 13) transmute(body.elements, 'rock', 'iron', rate * 0.46)
        if (body.birthMass > 22) transmute(body.elements, 'rock', 'iron', rate * 0.7)
    }
}

function updateStarAppearance(body: UniverseBody, dt: number) {
    const baseTemp = starTemperature(body.starType, body.birthMass)
    const baseLuminosity = starLuminosity(body.starType, body.birthMass)
    let targetRadius = clamp(2.5 + Math.sqrt(body.birthMass) * 1.25, 3, 13)
    let targetTemperature = baseTemp
    let targetLuminosity = baseLuminosity

    if (body.starStage === 'giantShell') {
        targetRadius *= body.birthMass > 8 ? 2.1 : 2.8
        targetTemperature *= body.birthMass > 8 ? 0.78 : 0.58
        targetLuminosity *= body.birthMass > 8 ? 1.8 : 1.35
    }
    if (body.starStage === 'heliumBurning') {
        targetRadius *= body.birthMass > 8 ? 1.55 : 1.8
        targetTemperature *= body.birthMass > 8 ? 1.15 : 0.72
        targetLuminosity *= 1.6
    }
    if (body.starStage === 'lateBurning') {
        targetRadius *= body.birthMass > 13 ? 1.25 : 1.6
        targetTemperature *= body.birthMass > 13 ? 1.45 : 0.8
        targetLuminosity *= body.birthMass > 13 ? 2.4 : 1.25
    }

    const t = clamp(dt * 1.6, 0.04, 0.4)
    body.radius = mix(body.radius, targetRadius, t)
    body.temperature = mix(body.temperature, targetTemperature, t)
    body.luminosity = mix(body.luminosity, targetLuminosity, t)
}

function supernovaYields(source: UniverseBody) {
    const mass = source.birthMass || source.mass
    const fallback = clamp((mass - 18) / 16, 0, 0.65)
    return {
        cno: (0.04 + mass * 0.002) * (1 - fallback * 0.35),
        rock: (0.025 + Math.max(0, mass - 8) * 0.0024) * (1 - fallback * 0.2),
        iron: (0.008 + Math.max(0, mass - 12) * 0.0018) * (1 - fallback),
        power: clamp(mass / 13, 0.8, 3.6),
        radius: 360 + clamp(mass, 8, 30) * 11,
    }
}

function stellarProgress(body: UniverseBody) {
    return clamp(body.age / Math.max(0.001, body.lifetime), 0, 1.4)
}

function transmute(elements: ElementMix, from: keyof ElementMix, to: keyof ElementMix, amount: number) {
    const moved = Math.min(elements[from] * 0.12, Math.max(0, amount))
    elements[from] -= moved
    elements[to] += moved
    normalizeElements(elements)
    return moved
}

function accreteIntoBlackHole(list: UniverseBody[], index: number, swallowed: Set<number>) {
    const hole = list[index]
    for (let j = 0; j < list.length; j += 1) {
        if (j === index || swallowed.has(j)) continue
        const body = list[j]
        if (body.kind === 'dark') continue
        const dx = body.x - hole.x
        const dy = body.y - hole.y
        const dist = Math.hypot(dx, dy)
        const accretionRadius = hole.radius * 5 + Math.sqrt(hole.mass) * 2.5
        if (dist < accretionRadius) {
            swallowed.add(j)
            hole.mass += body.mass * 0.42
            hole.radius = clamp(5 + Math.sqrt(hole.mass) * 0.8, 7, 28)
            enrich(hole.elements, body.elements.cno * 0.02, body.elements.rock * 0.02, body.elements.iron * 0.02)
        }
        else if (dist < accretionRadius * 4) {
            const inv = 1 / Math.max(1, dist)
            body.vx -= dx * inv * 0.03
            body.vy -= dy * inv * 0.03
            if (body.kind === 'gas') body.temperature += 300
        }
    }
}

function resizeCanvas() {
    const canvas = canvasRef.value
    if (!canvas) return
    const rect = canvas.getBoundingClientRect()
    dpr = Math.max(1, Math.min(2, window.devicePixelRatio || 1))
    width = Math.max(1, rect.width)
    height = Math.max(1, rect.height)
    canvas.width = Math.round(width * dpr)
    canvas.height = Math.round(height * dpr)
    context = canvas.getContext('2d')
    if (context) context.setTransform(dpr, 0, 0, dpr, 0, 0)
    draw()
}

function draw() {
    const ctx = context
    if (!ctx) return
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
    drawBackground(ctx)
    drawScaleGrid(ctx)
    if (viewMode.value === 'gravity') drawGravityField(ctx)
    drawFilaments(ctx)
    if (viewMode.value === 'elements' || viewMode.value === 'systems' || settings.mttOverlay) drawRegionMemory(ctx)
    drawBodies(ctx)
    if (settings.mttOverlay) drawStabilityOverlay(ctx)
    drawCenterReticle(ctx)
}

function drawBackground(ctx: CanvasRenderingContext2D) {
    const gradient = ctx.createLinearGradient(0, 0, width, height)
    gradient.addColorStop(0, '#061018')
    gradient.addColorStop(0.42, '#101421')
    gradient.addColorStop(0.72, '#1b1420')
    gradient.addColorStop(1, '#0b1115')
    ctx.fillStyle = gradient
    ctx.fillRect(0, 0, width, height)

    ctx.save()
    ctx.globalAlpha = 0.08
    for (let i = 0; i < 180; i += 1) {
        const seed = i * 137.13
        const x = fract(Math.sin(seed) * 92374) * width
        const y = fract(Math.cos(seed * 1.73) * 67214) * height
        const r = 0.4 + fract(Math.sin(seed * 1.9) * 2000) * 1.2
        ctx.fillStyle = i % 5 === 0 ? '#ffe9a8' : '#d8f4ff'
        ctx.beginPath()
        ctx.arc(x, y, r, 0, TAU)
        ctx.fill()
    }
    ctx.restore()
}

function drawScaleGrid(ctx: CanvasRenderingContext2D) {
    ctx.save()
    ctx.globalAlpha = 0.11
    ctx.strokeStyle = '#c9f4ff'
    ctx.lineWidth = 1
    const spacing = 160 * camera.zoom
    const origin = worldToScreen(0, 0)
    for (let x = origin.x % spacing; x < width; x += spacing) {
        ctx.beginPath()
        ctx.moveTo(x, 0)
        ctx.lineTo(x, height)
        ctx.stroke()
    }
    for (let y = origin.y % spacing; y < height; y += spacing) {
        ctx.beginPath()
        ctx.moveTo(0, y)
        ctx.lineTo(width, y)
        ctx.stroke()
    }
    ctx.restore()
}

function drawGravityField(ctx: CanvasRenderingContext2D) {
    ctx.save()
    ctx.globalCompositeOperation = 'screen'
    for (const body of bodies.value) {
        if (body.kind === 'gas' && body.mass < 6) continue
        const p = worldToScreen(body.x, body.y)
        const r = Math.max(18, Math.sqrt(body.mass) * 18 * camera.zoom)
        const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, r)
        const color = body.kind === 'blackHole' ? '255, 183, 79' : body.kind === 'dark' ? '154, 116, 255' : '120, 240, 255'
        const alpha = body.kind === 'blackHole' ? 0.22 : 0.08
        g.addColorStop(0, `rgba(${color}, ${alpha})`)
        g.addColorStop(1, `rgba(${color}, 0)`)
        ctx.fillStyle = g
        ctx.beginPath()
        ctx.arc(p.x, p.y, r, 0, TAU)
        ctx.fill()
    }
    ctx.restore()
}

function drawFilaments(ctx: CanvasRenderingContext2D) {
    if (viewMode.value === 'temperature') return
    const massive = bodies.value
        .filter((body) => body.kind !== 'gas' && body.mass > 6)
        .slice(0, 150)

    ctx.save()
    ctx.lineWidth = 1
    for (let i = 0; i < massive.length; i += 1) {
        const a = massive[i]
        for (let j = i + 1; j < massive.length; j += 1) {
            const b = massive[j]
            const dist = Math.hypot(a.x - b.x, a.y - b.y)
            if (dist > 230) continue
            const alpha = (1 - dist / 230) * (viewMode.value === 'systems' ? 0.1 : 0.045)
            const pa = worldToScreen(a.x, a.y)
            const pb = worldToScreen(b.x, b.y)
            ctx.strokeStyle = `rgba(156, 224, 255, ${alpha})`
            ctx.beginPath()
            ctx.moveTo(pa.x, pa.y)
            ctx.lineTo(pb.x, pb.y)
            ctx.stroke()
        }
    }
    ctx.restore()
}

function drawRegionMemory(ctx: CanvasRenderingContext2D) {
    ctx.save()
    ctx.globalCompositeOperation = 'screen'
    for (const region of regions.value) {
        const p = worldToScreen(region.x, region.y)
        const metals = metalFraction(region.elements)
        const r = Math.max(18, region.radius * camera.zoom)
        const color = elementColor(region.elements)
        const alpha = clamp(0.025 + metals * 1.8 + region.feedback * 0.035, 0.025, 0.22)
        const fill = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, r)
        fill.addColorStop(0, withAlpha(color, alpha))
        fill.addColorStop(0.7, withAlpha(color, alpha * 0.22))
        fill.addColorStop(1, withAlpha(color, 0))
        ctx.fillStyle = fill
        ctx.beginPath()
        ctx.arc(p.x, p.y, r, 0, TAU)
        ctx.fill()

        if (region.generation > 1 || region.feedback > 0.08) {
            ctx.strokeStyle = withAlpha(color, clamp(0.08 + region.generation * 0.025 + region.feedback * 0.05, 0.08, 0.35))
            ctx.lineWidth = 1
            ctx.beginPath()
            ctx.arc(p.x, p.y, r * 0.58, 0, TAU)
            ctx.stroke()
        }
        if ((viewMode.value === 'matter' || viewMode.value === 'systems') && region.diskSettling > 0.28 && Math.abs(region.spin) > 0.12) {
            drawRegionSpiralArms(ctx, region, p, r, color)
        }
        if (viewMode.value === 'systems' && Math.abs(region.spin) > 0.12) {
            ctx.strokeStyle = withAlpha('#b9f7ff', clamp(0.08 + region.virialSupport * 0.22, 0.08, 0.32))
            ctx.lineWidth = 1.2
            const direction = region.spin < 0 ? -1 : 1
            for (let i = 0; i < 2; i += 1) {
                const start = region.spin * 2.8 + i * Math.PI
                ctx.beginPath()
                ctx.arc(p.x, p.y, r * (0.34 + i * 0.16), start, start + direction * Math.PI * 0.82, direction < 0)
                ctx.stroke()
            }
        }
    }
    ctx.restore()
}

function drawRegionSpiralArms(ctx: CanvasRenderingContext2D, region: RegionMemory, p: { x: number, y: number }, radius: number, color: string) {
    const armCount = region.mass > 260 ? 4 : 2
    const spinSign = region.spin < 0 ? -1 : 1
    const alpha = clamp(0.035 + region.diskSettling * 0.13 + region.virialSupport * 0.07, 0.04, viewMode.value === 'systems' ? 0.32 : 0.18)
    const maxRadius = Math.max(26, radius * 0.92)
    const minRadius = Math.max(10, radius * 0.16)
    ctx.save()
    ctx.globalCompositeOperation = 'screen'
    ctx.strokeStyle = withAlpha(viewMode.value === 'systems' ? '#b9f7ff' : color, alpha)
    ctx.lineWidth = viewMode.value === 'systems' ? 1.4 : 1
    for (let arm = 0; arm < armCount; arm += 1) {
        ctx.beginPath()
        for (let s = 0; s <= 46; s += 1) {
            const t = s / 46
            const rr = minRadius + (maxRadius - minRadius) * t
            const theta = region.spiralPhase / armCount + arm * TAU / armCount + spinSign * Math.log(1 + t * 5.8) * 1.35
            const wobble = 1 + Math.sin(t * 8 + region.id) * 0.035
            const x = p.x + Math.cos(theta) * rr * wobble
            const y = p.y + Math.sin(theta) * rr * wobble
            if (s === 0) ctx.moveTo(x, y)
            else ctx.lineTo(x, y)
        }
        ctx.stroke()
    }
    ctx.restore()
}

function drawBodies(ctx: CanvasRenderingContext2D) {
    const sorted = bodies.value.slice().sort((a, b) => drawOrder(a) - drawOrder(b))
    for (const body of sorted) {
        if (body.kind === 'dark' && !settings.darkMatter && viewMode.value !== 'gravity') continue
        if (viewMode.value === 'systems' && body.kind === 'gas' && body.density < 0.4) continue
        if (body.kind === 'dark') drawDarkMatter(ctx, body)
        if (body.kind === 'gas') drawGas(ctx, body)
        if (body.kind === 'star') drawStarBody(ctx, body)
        if (body.kind === 'remnant') drawRemnant(ctx, body)
        if (body.kind === 'blackHole') drawBlackHole(ctx, body)
    }
}

function drawDarkMatter(ctx: CanvasRenderingContext2D, body: UniverseBody) {
    const p = worldToScreen(body.x, body.y)
    const r = Math.max(1.4, body.radius * camera.zoom)
    const alpha = viewMode.value === 'gravity' ? 0.28 : 0.14
    ctx.save()
    ctx.globalCompositeOperation = 'screen'
    ctx.fillStyle = `rgba(145, 113, 255, ${alpha})`
    ctx.beginPath()
    ctx.arc(p.x, p.y, r * 2.4, 0, TAU)
    ctx.fill()
    ctx.fillStyle = `rgba(195, 176, 255, ${alpha * 0.7})`
    ctx.beginPath()
    ctx.arc(p.x, p.y, Math.max(0.8, r * 0.8), 0, TAU)
    ctx.fill()
    ctx.restore()
}

function drawGas(ctx: CanvasRenderingContext2D, body: UniverseBody) {
    const p = worldToScreen(body.x, body.y)
    const r = Math.max(3.5, body.radius * camera.zoom * (1 + body.density * 0.45))
    const color = bodyColor(body)
    ctx.save()
    ctx.globalCompositeOperation = 'screen'
    const g = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, r * 3.4)
    g.addColorStop(0, withAlpha(color, 0.22 + clamp(body.density * 0.18, 0, 0.35)))
    g.addColorStop(0.62, withAlpha(color, 0.08))
    g.addColorStop(1, withAlpha(color, 0))
    ctx.fillStyle = g
    ctx.beginPath()
    ctx.arc(p.x, p.y, r * 3.4, 0, TAU)
    ctx.fill()
    ctx.fillStyle = withAlpha(color, 0.34)
    ctx.beginPath()
    ctx.arc(p.x, p.y, r * 0.8, 0, TAU)
    ctx.fill()
    ctx.restore()
}

function drawStarBody(ctx: CanvasRenderingContext2D, body: UniverseBody) {
    const p = worldToScreen(body.x, body.y)
    const r = Math.max(2.2, body.radius * camera.zoom)
    const color = bodyColor(body)
    const flashBoost = 1 + body.flash * 0.8
    ctx.save()
    ctx.globalCompositeOperation = 'screen'
    const glow = ctx.createRadialGradient(p.x, p.y, 0, p.x, p.y, r * (5 + body.luminosity * 0.6) * flashBoost)
    glow.addColorStop(0, withAlpha(color, 0.42 + body.flash * 0.16))
    glow.addColorStop(0.24, withAlpha(color, 0.2 + body.flash * 0.1))
    glow.addColorStop(1, withAlpha(color, 0))
    ctx.fillStyle = glow
    ctx.beginPath()
    ctx.arc(p.x, p.y, r * (5 + body.luminosity * 0.6) * flashBoost, 0, TAU)
    ctx.fill()

    ctx.fillStyle = '#fff7d8'
    ctx.beginPath()
    ctx.arc(p.x, p.y, r * 0.7, 0, TAU)
    ctx.fill()
    ctx.fillStyle = color
    ctx.beginPath()
    ctx.arc(p.x, p.y, r, 0, TAU)
    ctx.fill()
    ctx.restore()

    if (settings.showPlanets && (body.planets > 0 || body.diskMass > 0.15)) drawPlanetSystem(ctx, body, p, r)
}

function drawPlanetSystem(ctx: CanvasRenderingContext2D, body: UniverseBody, p: { x: number, y: number }, starRadius: number) {
    if (viewMode.value !== 'matter' && viewMode.value !== 'systems') return
    ctx.save()
    const diskAlpha = clamp(0.035 + body.diskMass * 0.025 + body.systemStability * 0.08, 0.04, 0.24)
    const maxOrbit = Math.max(starRadius * 8, starRadius * (5.8 + Math.max(body.planets, 2) * 2.1 + body.diskMass * 0.28))
    ctx.translate(p.x, p.y)
    ctx.rotate(body.planetSeed)
    ctx.scale(1, 0.55)
    const disk = ctx.createRadialGradient(0, 0, starRadius * 1.8, 0, 0, maxOrbit)
    disk.addColorStop(0, `rgba(140, 232, 198, ${diskAlpha * 0.12})`)
    disk.addColorStop(0.45, `rgba(140, 232, 198, ${diskAlpha})`)
    disk.addColorStop(1, 'rgba(140, 232, 198, 0)')
    ctx.fillStyle = disk
    ctx.beginPath()
    ctx.arc(0, 0, maxOrbit, 0, TAU)
    ctx.fill()

    ctx.strokeStyle = viewMode.value === 'systems' ? 'rgba(210, 235, 255, 0.24)' : 'rgba(210, 235, 255, 0.1)'
    for (let i = 0; i < body.planets; i += 1) {
        const orbit = starRadius * (4.5 + i * 2.1)
        if (orbit < 6 || orbit > 70) continue
        ctx.beginPath()
        ctx.arc(0, 0, orbit, 0, TAU)
        ctx.stroke()
        const phase = body.spin * (0.16 / (i + 1)) + body.planetSeed + i * 1.9
        const x = Math.cos(phase) * orbit
        const y = Math.sin(phase) * orbit
        ctx.fillStyle = i % 3 === 0 ? '#9ae47f' : i % 3 === 1 ? '#8fc7ff' : '#d7b36b'
        ctx.beginPath()
        ctx.arc(x, y, Math.max(1, starRadius * 0.25), 0, TAU)
        ctx.fill()
    }
    ctx.restore()
}

function drawRemnant(ctx: CanvasRenderingContext2D, body: UniverseBody) {
    const p = worldToScreen(body.x, body.y)
    const r = Math.max(1.4, body.radius * camera.zoom)
    ctx.save()
    ctx.globalCompositeOperation = 'screen'
    ctx.fillStyle = bodyColor(body)
    ctx.beginPath()
    ctx.arc(p.x, p.y, r * 1.15, 0, TAU)
    ctx.fill()
    ctx.strokeStyle = 'rgba(230, 240, 255, 0.34)'
    ctx.beginPath()
    ctx.arc(p.x, p.y, r * 2.4, 0, TAU)
    ctx.stroke()
    if (body.remnantType === 'neutronStar') {
        ctx.strokeStyle = `rgba(133, 227, 255, ${0.22 + body.flash * 0.18})`
        ctx.beginPath()
        ctx.moveTo(p.x - r * 6 * Math.cos(body.spin), p.y - r * 6 * Math.sin(body.spin))
        ctx.lineTo(p.x + r * 6 * Math.cos(body.spin), p.y + r * 6 * Math.sin(body.spin))
        ctx.stroke()
    }
    ctx.restore()
}

function drawBlackHole(ctx: CanvasRenderingContext2D, body: UniverseBody) {
    const p = worldToScreen(body.x, body.y)
    const r = Math.max(4, body.radius * camera.zoom)
    ctx.save()
    ctx.globalCompositeOperation = 'screen'
    const disk = ctx.createRadialGradient(p.x, p.y, r * 0.7, p.x, p.y, r * 7)
    disk.addColorStop(0, 'rgba(255, 236, 179, 0.4)')
    disk.addColorStop(0.35, 'rgba(255, 137, 66, 0.22)')
    disk.addColorStop(1, 'rgba(255, 137, 66, 0)')
    ctx.fillStyle = disk
    ctx.beginPath()
    ctx.ellipse(p.x, p.y, r * 7, r * 2.2, body.spin * 0.25, 0, TAU)
    ctx.fill()

    ctx.globalCompositeOperation = 'source-over'
    ctx.fillStyle = '#020204'
    ctx.beginPath()
    ctx.arc(p.x, p.y, r * 1.5, 0, TAU)
    ctx.fill()
    ctx.strokeStyle = 'rgba(255, 225, 166, 0.6)'
    ctx.lineWidth = 1.5
    ctx.beginPath()
    ctx.arc(p.x, p.y, r * 2.1, 0, TAU)
    ctx.stroke()
    ctx.restore()
}

function drawStabilityOverlay(ctx: CanvasRenderingContext2D) {
    ctx.save()
    for (const body of bodies.value) {
        if (body.kind === 'gas' && body.density < 0.7) continue
        if (body.kind === 'dark') continue
        const closure = closureScore(body)
        if (closure < 0.46) continue
        const p = worldToScreen(body.x, body.y)
        const r = Math.max(6, (body.radius + closure * 14) * camera.zoom)
        ctx.strokeStyle = `rgba(133, 255, 190, ${0.06 + closure * 0.14})`
        ctx.lineWidth = 1
        ctx.beginPath()
        ctx.arc(p.x, p.y, r, 0, TAU)
        ctx.stroke()
    }
    ctx.restore()
}

function drawCenterReticle(ctx: CanvasRenderingContext2D) {
    const center = { x: width * 0.5, y: height * 0.5 }
    ctx.save()
    ctx.globalAlpha = 0.35
    ctx.strokeStyle = '#ffffff'
    ctx.lineWidth = 1
    ctx.beginPath()
    ctx.arc(center.x, center.y, 8, 0, TAU)
    ctx.stroke()
    ctx.beginPath()
    ctx.moveTo(center.x - 16, center.y)
    ctx.lineTo(center.x - 10, center.y)
    ctx.moveTo(center.x + 10, center.y)
    ctx.lineTo(center.x + 16, center.y)
    ctx.moveTo(center.x, center.y - 16)
    ctx.lineTo(center.x, center.y - 10)
    ctx.moveTo(center.x, center.y + 10)
    ctx.lineTo(center.x, center.y + 16)
    ctx.stroke()
    ctx.restore()
}

function bodyColor(body: UniverseBody) {
    if (viewMode.value === 'temperature') return temperatureColor(body.temperature)
    if (viewMode.value === 'elements') return elementColor(body.elements)
    if (viewMode.value === 'gravity') {
        if (body.kind === 'blackHole') return '#ffb24c'
        if (body.kind === 'dark') return '#8d74ff'
        return '#9ee7ff'
    }
    if (body.kind === 'gas') return body.density > 0.75 ? '#59f0c2' : '#5ec9ff'
    if (body.kind === 'remnant') return body.remnantType === 'neutronStar' ? '#83e3ff' : '#f0f6ff'
    if (body.kind === 'blackHole') return '#ff965d'
    if (body.starStage === 'giantShell') return '#ffad72'
    if (body.starStage === 'heliumBurning') return '#d1ecff'
    if (body.starStage === 'lateBurning') return '#ffe066'
    if (body.starType === 'red') return '#ff8f75'
    if (body.starType === 'blue' || body.starType === 'giant') return '#9cc8ff'
    return '#ffd778'
}

function temperatureColor(temperature: number) {
    const t = clamp((Math.log10(temperature + 1) - 1.5) / 6.5, 0, 1)
    if (t < 0.24) return mixColor('#5377ff', '#40e1ff', t / 0.24)
    if (t < 0.5) return mixColor('#40e1ff', '#79f07c', (t - 0.24) / 0.26)
    if (t < 0.72) return mixColor('#79f07c', '#ffd35e', (t - 0.5) / 0.22)
    return mixColor('#ffd35e', '#ff5b5b', (t - 0.72) / 0.28)
}

function elementColor(elements: ElementMix) {
    const metals = elements.cno + elements.rock + elements.iron
    if (elements.iron > 0.03) return '#ff6b5f'
    if (elements.rock > 0.035) return '#d9b35f'
    if (metals > 0.018) return '#cf7cff'
    if (elements.he > 0.3) return '#62e6af'
    return '#69c8ff'
}

function startPan(event: PointerEvent) {
    const canvas = canvasRef.value
    if (!canvas) return
    panState.active = true
    panState.pointerId = event.pointerId
    panState.lastX = event.clientX
    panState.lastY = event.clientY
    canvas.setPointerCapture(event.pointerId)
}

function movePan(event: PointerEvent) {
    if (!panState.active || event.pointerId !== panState.pointerId) return
    const dx = event.clientX - panState.lastX
    const dy = event.clientY - panState.lastY
    camera.x -= dx / camera.zoom
    camera.y -= dy / camera.zoom
    panState.lastX = event.clientX
    panState.lastY = event.clientY
}

function endPan(event: PointerEvent) {
    if (event.pointerId !== panState.pointerId) return
    panState.active = false
    panState.pointerId = -1
}

function handleWheel(event: WheelEvent) {
    const before = screenToWorld(event.offsetX, event.offsetY)
    const factor = event.deltaY > 0 ? 0.9 : 1.1
    camera.zoom = clamp(camera.zoom * factor, 0.18, 2.8)
    const after = screenToWorld(event.offsetX, event.offsetY)
    camera.x += before.x - after.x
    camera.y += before.y - after.y
}

function worldToScreen(x: number, y: number) {
    return {
        x: width * 0.5 + (x - camera.x) * camera.zoom,
        y: height * 0.5 + (y - camera.y) * camera.zoom,
    }
}

function screenToWorld(x: number, y: number) {
    return {
        x: camera.x + (x - width * 0.5) / camera.zoom,
        y: camera.y + (y - height * 0.5) / camera.zoom,
    }
}

function createBody(partial: Partial<UniverseBody> & { kind: BodyKind, x: number, y: number, vx: number, vy: number, mass: number, radius: number, temperature: number, elements: ElementMix }): UniverseBody {
    return {
        id: nextBodyId += 1,
        kind: partial.kind,
        starType: partial.starType || 'none',
        starStage: partial.starStage || (partial.kind === 'star' ? 'mainSequence' : 'none'),
        remnantType: partial.remnantType || 'none',
        x: partial.x,
        y: partial.y,
        vx: partial.vx,
        vy: partial.vy,
        mass: partial.mass,
        birthMass: partial.birthMass || partial.mass,
        radius: partial.radius,
        density: partial.density || 0,
        temperature: partial.temperature,
        age: partial.age || 0,
        lifetime: partial.lifetime || 1e9,
        luminosity: partial.luminosity || 0,
        flash: partial.flash || 0,
        planets: partial.planets || 0,
        diskMass: partial.diskMass || 0,
        systemStability: partial.systemStability || 0,
        planetSeed: rand() * TAU,
        spin: rand() * TAU,
        elements: normalizeElements({ ...partial.elements }),
        regionId: partial.regionId || 0,
        generation: partial.generation || (partial.kind === 'star' ? 1 : 1),
        birthMetallicity: partial.birthMetallicity || metalFraction(partial.elements),
    }
}

function seededDiskPoint(radius: number) {
    const angle = rand() * TAU
    const r = Math.sqrt(rand()) * radius
    return {
        x: Math.cos(angle) * r,
        y: Math.sin(angle) * r * 0.72,
    }
}

function seededUniformFieldPoint(index: number, total: number, radius: number, jitter: number) {
    const golden = Math.PI * (3 - Math.sqrt(5))
    const p = (index + 0.5 + randBetween(-0.18, 0.18)) / Math.max(1, total)
    const angle = index * golden + randBetween(-0.05, 0.05)
    const r = Math.sqrt(clamp(p, 0, 1)) * radius
    const wave = 1 + Math.sin(angle * 3.7 + index * 0.017) * 0.035 + Math.cos(angle * 2.1) * 0.025
    return {
        x: Math.cos(angle) * r * wave + randBetween(-radius * jitter * 0.018, radius * jitter * 0.018),
        y: Math.sin(angle) * r * wave + randBetween(-radius * jitter * 0.018, radius * jitter * 0.018),
    }
}

function haloScatterPoint(cx: number, cy: number, radius: number) {
    const angle = rand() * TAU
    const coreBias = rand() < 0.72 ? 1.65 : 0.82
    const r = radius * (rand() ** coreBias)
    const shear = 1 + Math.sin(angle * 2.3 + cx * 0.002) * 0.16
    return {
        x: cx + Math.cos(angle) * r * shear + randBetween(-radius * 0.035, radius * 0.035),
        y: cy + Math.sin(angle) * r * (1.08 - (shear - 1) * 0.35) + randBetween(-radius * 0.035, radius * 0.035),
    }
}

function seededCosmicWebPoint(radius: number) {
    if (rand() < 0.28) {
        const p = seededDiskPoint(radius * 0.92)
        return {
            x: p.x + randBetween(-radius * 0.08, radius * 0.08),
            y: p.y / 0.72 + randBetween(-radius * 0.08, radius * 0.08),
        }
    }

    const filament = Math.floor(rand() * 7)
    const angle = filament * TAU / 7 + randBetween(-0.22, 0.22)
    const along = randBetween(-radius, radius)
    const width = radius * randBetween(0.035, 0.16)
    const cross = randBetween(-width, width)
    const wave = Math.sin(along * 0.004 + filament * 1.7) * radius * 0.035
    let x = Math.cos(angle) * along - Math.sin(angle) * (cross + wave)
    let y = Math.sin(angle) * along + Math.cos(angle) * (cross + wave)
    const dist = Math.hypot(x, y)
    if (dist > radius) {
        const scale = radius / dist
        x *= scale
        y *= scale
    }
    return { x, y }
}

function localVortexFlow(x: number, y: number, strength: number) {
    const scale = 520
    const gx = Math.round(x / scale)
    const gy = Math.round(y / scale)
    const seed = Math.sin(gx * 127.1 + gy * 311.7) * 43758.5453
    const phase = fract(seed) * TAU
    const cx = gx * scale + Math.cos(phase) * scale * 0.22
    const cy = gy * scale + Math.sin(phase * 1.37) * scale * 0.22
    const dx = x - cx
    const dy = y - cy
    const dist = Math.max(12, Math.hypot(dx, dy))
    const envelope = clamp(1 - dist / (scale * 1.16), 0, 1) ** 2
    const sign = fract(seed * 1.91) > 0.5 ? 1 : -1
    const speed = strength * envelope * (0.45 + fract(seed * 2.23) * 0.55) * sign
    return {
        vx: -dy / dist * speed,
        vy: dx / dist * speed,
    }
}

function spiralPoint(index: number, total: number, arms: number, radius: number, jitter: number) {
    const p = index / Math.max(1, total - 1)
    const arm = index % arms
    const angle = arm * TAU / arms + p * 5.8 + randBetween(-0.22, 0.22)
    const r = Math.sqrt(p) * radius + jitter
    return {
        x: Math.cos(angle) * r + randBetween(-18, 18),
        y: Math.sin(angle) * r * 0.55 + randBetween(-18, 18),
    }
}

function swirlVelocity(x: number, y: number, strength: number) {
    return {
        vx: -y * strength,
        vy: x * strength,
    }
}

function circularVelocity(x: number, y: number, strength: number) {
    const dist = Math.max(40, Math.hypot(x, y))
    const speed = strength * Math.sqrt(dist) * 0.17
    return {
        vx: -y / dist * speed,
        vy: x / dist * speed,
    }
}

function primordialElements(metallicity: number): ElementMix {
    return normalizeElements({
        h: 0.748 - metallicity * 0.3,
        he: 0.252 - metallicity * 0.15,
        cno: metallicity * 0.52,
        rock: metallicity * 0.3,
        iron: metallicity * 0.18,
    })
}

function enrichedElements(metallicity: number): ElementMix {
    return normalizeElements({
        h: 0.738 - metallicity * 0.45,
        he: 0.262 - metallicity * 0.28,
        cno: metallicity * 0.44,
        rock: metallicity * 0.36,
        iron: metallicity * 0.2,
    })
}

function normalizeElements(elements: ElementMix) {
    elements.h = Math.max(0, elements.h)
    elements.he = Math.max(0, elements.he)
    elements.cno = Math.max(0, elements.cno)
    elements.rock = Math.max(0, elements.rock)
    elements.iron = Math.max(0, elements.iron)
    const total = Math.max(1e-8, elements.h + elements.he + elements.cno + elements.rock + elements.iron)
    elements.h /= total
    elements.he /= total
    elements.cno /= total
    elements.rock /= total
    elements.iron /= total
    return elements
}

function metalFraction(elements: ElementMix) {
    return elements.cno + elements.rock + elements.iron
}

function blendElements(target: ElementMix, source: ElementMix, weight: number) {
    const t = clamp(weight, 0, 1)
    target.h = mix(target.h, source.h, t)
    target.he = mix(target.he, source.he, t)
    target.cno = mix(target.cno, source.cno, t)
    target.rock = mix(target.rock, source.rock, t)
    target.iron = mix(target.iron, source.iron, t)
    normalizeElements(target)
}

function enrich(elements: ElementMix, cno: number, rock: number, iron: number) {
    elements.h *= 1 - Math.min(0.22, cno + rock + iron)
    elements.he *= 1 - Math.min(0.12, rock + iron)
    elements.cno += cno
    elements.rock += rock
    elements.iron += iron
    normalizeElements(elements)
}

function currentRadiationPressure() {
    simTick.value
    const eraScale = selectedPreset.value === 'uniform'
        ? 1
        : selectedPreset.value === 'nursery'
            ? 0.42
            : 0.06
    const ageDecay = Math.exp(-Math.max(0, cosmicAgeGyr.value - 0.02) / 0.34)
    return clamp(settings.radiationPressure * eraScale * ageDecay, 0, 1.6)
}

function thermalPressure(body: UniverseBody) {
    return clamp((Math.log10(body.temperature + 10) - 2) / 5 + body.density * 0.18, 0, 2)
}

function closureScore(body: UniverseBody) {
    if (body.kind === 'star') return clamp(0.58 + body.planets * 0.04 + body.density * 0.07, 0, 1)
    if (body.kind === 'blackHole') return 0.92
    if (body.kind === 'remnant') return 0.74
    if (body.kind === 'gas') return clamp(body.density * 0.62 + (1 - thermalPressure(body)) * 0.18, 0, 1)
    return 0
}

function starTemperature(starType: StarType, mass: number) {
    if (starType === 'giant') return 19000 + mass * 950
    if (starType === 'blue') return 8500 + mass * 820
    if (starType === 'yellow') return 4300 + mass * 260
    if (starType === 'red') return 2500 + mass * 180
    return 3000
}

function starLuminosity(starType: StarType, mass: number) {
    if (starType === 'giant') return 10 + mass * 1.2
    if (starType === 'blue') return 4 + mass * 0.5
    if (starType === 'yellow') return 0.8 + mass * 0.16
    if (starType === 'red') return 0.2 + mass * 0.04
    return 0
}

function drawOrder(body: UniverseBody) {
    if (body.kind === 'dark') return 0
    if (body.kind === 'gas') return 1
    if (body.kind === 'remnant') return 2
    if (body.kind === 'star') return 3
    return 4
}

function trimBodies(list: UniverseBody[]) {
    if (list.length <= MAX_BODIES) return list
    return list
        .slice()
        .sort((a, b) => bodyPriority(b) - bodyPriority(a))
        .slice(0, MAX_BODIES)
}

function bodyPriority(body: UniverseBody) {
    if (body.kind === 'blackHole') return 10000 + body.mass
    if (body.kind === 'star') return 5000 + body.mass + body.planets * 10
    if (body.kind === 'remnant') return 3500 + body.mass
    if (body.kind === 'gas') return 1000 + body.mass + body.density * 120
    return body.mass
}

function hashPreset(id: string) {
    let hash = 2166136261
    for (let i = 0; i < id.length; i += 1) {
        hash ^= id.charCodeAt(i)
        hash = Math.imul(hash, 16777619)
    }
    return hash >>> 0
}

function rand() {
    rngState = Math.imul(1664525, rngState) + 1013904223
    return (rngState >>> 0) / 4294967296
}

function randBetween(min: number, max: number) {
    return min + (max - min) * rand()
}

function clamp(value: number, min: number, max: number) {
    return Math.max(min, Math.min(max, value))
}

function mix(a: number, b: number, t: number) {
    return a + (b - a) * clamp(t, 0, 1)
}

function fract(value: number) {
    return value - Math.floor(value)
}

function mixColor(a: string, b: string, t: number) {
    const ca = hexToRgb(a)
    const cb = hexToRgb(b)
    return `rgb(${Math.round(mix(ca.r, cb.r, t))}, ${Math.round(mix(ca.g, cb.g, t))}, ${Math.round(mix(ca.b, cb.b, t))})`
}

function withAlpha(color: string, alpha: number) {
    if (color.startsWith('rgb(')) return color.replace('rgb(', 'rgba(').replace(')', `, ${alpha})`)
    const rgb = hexToRgb(color)
    return `rgba(${rgb.r}, ${rgb.g}, ${rgb.b}, ${alpha})`
}

function hexToRgb(hex: string) {
    const clean = hex.replace('#', '')
    const num = Number.parseInt(clean, 16)
    return {
        r: (num >> 16) & 255,
        g: (num >> 8) & 255,
        b: num & 255,
    }
}

function formatAge(value: number) {
    if (value < 1) return `${Math.round(value * 1000)} Myr`
    return `${value.toFixed(2)} Gyr`
}
</script>

<style scoped>
.universe-shell {
    position: fixed;
    inset: 0;
    overflow: hidden;
    background: #060a0d;
    color: #eef7ff;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.universe-canvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    cursor: grab;
    touch-action: none;
}

.universe-canvas:active {
    cursor: grabbing;
}

.topbar,
.control-panel,
.metrics-panel,
.legend,
.camera-help {
    position: absolute;
    z-index: 2;
    backdrop-filter: blur(18px);
    border: 1px solid rgba(218, 241, 255, 0.14);
    background: rgba(8, 13, 18, 0.72);
    box-shadow: 0 18px 60px rgba(0, 0, 0, 0.34);
}

.topbar {
    top: 16px;
    left: 16px;
    right: 16px;
    min-height: 72px;
    display: grid;
    grid-template-columns: auto 1fr auto;
    gap: 18px;
    align-items: center;
    padding: 12px 14px;
    border-radius: 8px;
}

.home-link,
.icon-button,
.preset-grid button,
.view-tabs button,
.action-grid button {
    border: 1px solid rgba(222, 243, 255, 0.16);
    background: rgba(255, 255, 255, 0.06);
    color: #f2fbff;
    transition: border-color 160ms ease, background 160ms ease, transform 160ms ease;
}

.home-link {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    height: 40px;
    padding: 0 12px;
    border-radius: 8px;
    text-decoration: none;
    font-size: 0.88rem;
}

.home-link:hover,
.icon-button:hover,
.preset-grid button:hover,
.view-tabs button:hover,
.action-grid button:hover {
    border-color: rgba(139, 228, 255, 0.55);
    background: rgba(83, 185, 255, 0.16);
}

.title-wrap {
    min-width: 0;
}

.title-row {
    display: flex;
    align-items: center;
    gap: 10px;
    min-width: 0;
    flex-wrap: wrap;
}

.title-icon {
    color: #8ce8c6;
    font-size: 1.35rem;
}

h1,
h2,
p {
    margin: 0;
}

h1 {
    font-size: clamp(1.15rem, 1.8vw, 1.75rem);
    line-height: 1.1;
    letter-spacing: 0;
}

.title-wrap p {
    margin-top: 6px;
    color: rgba(232, 246, 255, 0.72);
    font-size: 0.9rem;
    line-height: 1.35;
}

.mode-pill {
    display: inline-flex;
    align-items: center;
    height: 24px;
    padding: 0 8px;
    border-radius: 999px;
    background: rgba(94, 201, 255, 0.14);
    color: #aee9ff;
    font-size: 0.72rem;
    text-transform: uppercase;
}

.physics-pill {
    background: rgba(255, 207, 105, 0.16);
    color: #ffe2a1;
}

.mtt-pill {
    background: rgba(142, 255, 190, 0.12);
    color: #b9ffd4;
}

.top-actions {
    display: flex;
    gap: 8px;
}

.icon-button {
    width: 40px;
    height: 40px;
    display: inline-grid;
    place-items: center;
    border-radius: 8px;
    font-size: 1.25rem;
}

.control-panel,
.metrics-panel {
    top: 104px;
    bottom: 58px;
    width: min(334px, calc(100vw - 32px));
    overflow: auto;
    scrollbar-width: thin;
    border-radius: 8px;
}

.control-panel {
    left: 16px;
    padding: 14px;
}

.metrics-panel {
    right: 16px;
    padding: 14px;
}

.panel-section,
.metrics-panel section {
    padding: 12px 0;
    border-bottom: 1px solid rgba(230, 244, 255, 0.11);
}

.panel-section:first-child,
.metrics-panel section:first-child {
    padding-top: 0;
}

.panel-section:last-child,
.metrics-panel section:last-child {
    border-bottom: 0;
    padding-bottom: 0;
}

h2 {
    margin-bottom: 10px;
    color: #e9f7ff;
    font-size: 0.78rem;
    line-height: 1.2;
    text-transform: uppercase;
    letter-spacing: 0.08em;
}

.preset-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 8px;
}

.preset-grid button {
    min-height: 58px;
    border-radius: 8px;
    padding: 8px;
    text-align: left;
}

.preset-grid button span {
    display: inline-grid;
    place-items: center;
    width: 26px;
    height: 26px;
    margin-bottom: 5px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.1);
    color: #8ce8c6;
    font-size: 0.72rem;
    font-weight: 800;
}

.preset-grid button b {
    display: block;
    font-size: 0.84rem;
    line-height: 1.1;
}

.preset-grid button.active,
.view-tabs button.active {
    border-color: rgba(140, 232, 198, 0.65);
    background: rgba(72, 206, 154, 0.18);
}

.view-tabs {
    display: grid;
    grid-template-columns: repeat(5, minmax(0, 1fr));
    gap: 6px;
}

.view-tabs button {
    display: grid;
    place-items: center;
    min-width: 0;
    min-height: 46px;
    border-radius: 8px;
    padding: 5px 4px;
    font-size: 0.72rem;
}

.view-tabs button span {
    font-size: 1rem;
}

.controls label {
    display: grid;
    grid-template-columns: 78px minmax(0, 1fr) 44px;
    gap: 8px;
    align-items: center;
    margin: 8px 0;
    color: rgba(238, 248, 255, 0.78);
    font-size: 0.8rem;
}

.controls strong {
    text-align: right;
    font-size: 0.78rem;
}

input[type="range"] {
    width: 100%;
    accent-color: #8ce8c6;
}

.checkbox-row {
    display: flex;
    align-items: center;
    gap: 9px;
    margin: 8px 0;
    color: rgba(237, 248, 255, 0.8);
    font-size: 0.84rem;
}

.checkbox-row input {
    accent-color: #8ce8c6;
}

.action-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 8px;
}

.action-grid button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 7px;
    min-height: 38px;
    border-radius: 8px;
    padding: 0 8px;
    font-size: 0.78rem;
}

.metrics-panel p {
    color: rgba(234, 247, 255, 0.76);
    font-size: 0.88rem;
    line-height: 1.45;
}

.metric-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 8px;
    margin: 12px 0;
}

.metric {
    min-height: 62px;
    padding: 9px;
    border: 1px solid rgba(222, 243, 255, 0.13);
    border-radius: 8px;
    background: rgba(255, 255, 255, 0.055);
}

.metric span {
    display: block;
    margin-bottom: 6px;
    color: rgba(233, 248, 255, 0.58);
    font-size: 0.72rem;
    text-transform: uppercase;
}

.metric strong {
    font-size: 1rem;
    line-height: 1.1;
}

.ledger {
    display: grid;
    gap: 9px;
}

.ledger div {
    display: grid;
    grid-template-columns: 95px 58px minmax(0, 1fr);
    gap: 8px;
    align-items: center;
    color: rgba(233, 248, 255, 0.78);
    font-size: 0.8rem;
}

.ledger b {
    text-align: right;
    color: #f6fbff;
    font-size: 0.78rem;
}

.ledger i {
    display: block;
    height: 7px;
    min-width: 2px;
    border-radius: 999px;
    background: linear-gradient(90deg, #5ec9ff, #8ce8c6, #ffd778, #ff8f75);
}

.memory-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 8px;
}

.memory-list div {
    min-height: 48px;
    padding: 8px;
    border: 1px solid rgba(222, 243, 255, 0.12);
    border-radius: 8px;
    background: rgba(140, 232, 198, 0.055);
}

.memory-list span {
    display: block;
    margin-bottom: 5px;
    color: rgba(233, 248, 255, 0.58);
    font-size: 0.68rem;
    text-transform: uppercase;
}

.memory-list strong {
    color: #eafff5;
    font-size: 0.95rem;
}

.audit-list {
    display: grid;
    gap: 10px;
}

.audit-item {
    display: grid;
    grid-template-columns: 34px minmax(0, 1fr);
    gap: 9px;
    align-items: start;
    color: rgba(234, 247, 255, 0.74);
    font-size: 0.78rem;
    line-height: 1.35;
}

.audit-item i {
    display: inline-grid;
    place-items: center;
    width: 30px;
    height: 24px;
    border-radius: 999px;
    font-size: 0.67rem;
    font-style: normal;
    font-weight: 800;
    text-transform: uppercase;
}

.audit-item.native i {
    background: rgba(94, 201, 255, 0.16);
    color: #aee9ff;
}

.audit-item.mtt i {
    background: rgba(140, 232, 198, 0.14);
    color: #b9ffd4;
}

.audit-item.toy i {
    background: rgba(255, 211, 120, 0.16);
    color: #ffe0a0;
}

.legend,
.camera-help {
    bottom: 16px;
    min-height: 34px;
    display: flex;
    align-items: center;
    gap: 12px;
    padding: 0 12px;
    border-radius: 8px;
    color: rgba(236, 248, 255, 0.78);
    font-size: 0.78rem;
}

.legend {
    left: 16px;
    flex-wrap: wrap;
}

.camera-help {
    right: 16px;
}

.dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    margin-right: 5px;
    border-radius: 50%;
}

.dot.dark {
    background: #9678ff;
}

.dot.gas {
    background: #5ec9ff;
}

.dot.star {
    background: #ffd778;
}

.dot.remnant {
    background: #c8d1e6;
}

.dot.hole {
    background: #ff965d;
}

.dot.planet {
    background: #8ce8c6;
}

.separator {
    width: 1px;
    height: 14px;
    background: rgba(255, 255, 255, 0.22);
}

@media (max-width: 1100px) {
    .topbar {
        grid-template-columns: auto 1fr;
    }

    .top-actions {
        grid-column: 1 / -1;
    }

    .control-panel,
    .metrics-panel {
        top: auto;
        bottom: 60px;
        max-height: 38vh;
    }

    .control-panel {
        left: 12px;
    }

    .metrics-panel {
        right: 12px;
    }
}

@media (max-width: 760px) {
    .topbar {
        left: 10px;
        right: 10px;
        top: 10px;
        gap: 10px;
    }

    .title-wrap p,
    .mode-pill,
    .camera-help {
        display: none;
    }

    .control-panel,
    .metrics-panel {
        width: calc(50vw - 18px);
        bottom: 52px;
        max-height: 44vh;
        padding: 10px;
    }

    .view-tabs {
        grid-template-columns: repeat(2, minmax(0, 1fr));
    }

    .controls label {
        grid-template-columns: 1fr 48px;
    }

    .controls label input {
        grid-column: 1 / -1;
    }

    .metric-grid,
    .preset-grid,
    .action-grid {
        grid-template-columns: 1fr;
    }

    .legend {
        left: 10px;
        right: 10px;
        bottom: 10px;
        justify-content: center;
    }
}
</style>
