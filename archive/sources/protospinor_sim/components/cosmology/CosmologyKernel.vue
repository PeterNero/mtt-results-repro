<template>
    <section ref="shellRef" class="cosmo-shell">
        <canvas ref="canvasRef" class="cosmo-canvas"></canvas>

        <header class="topbar">
            <NuxtLink to="/" class="home-link" title="Home">
                <span class="i-tabler-arrow-left text-base"></span>
                <span>SandboxScience</span>
            </NuxtLink>
            <div class="title-wrap">
                <div class="title-row">
                    <span class="i-tabler-chart-arcs-3 title-icon"></span>
                    <h1>Cosmology Eras Lab</h1>
                    <span class="mode-pill">standard engine</span>
                    <span class="mode-pill mtt-pill">MTT encoding</span>
                </div>
                <p>Big Bang timeline driven by standard cosmology, with MTT bookkeeping shown as an interpretive layer.</p>
            </div>
            <div class="top-actions">
                <button class="icon-button" type="button" :title="isRunning ? 'Pause' : 'Run'" @click="toggleRunning">
                    <span :class="isRunning ? 'i-tabler-player-pause' : 'i-tabler-player-play'"></span>
                </button>
                <button class="icon-button" type="button" title="Reset to Big Bang edge" @click="resetTimeline">
                    <span class="i-tabler-refresh"></span>
                </button>
            </div>
        </header>

        <aside class="control-panel">
            <section class="panel-section">
                <h2>Era</h2>
                <div class="era-grid">
                    <button v-for="era in eraStops" :key="era.id" type="button" :class="{ active: era.id === currentEra.id }" @click="selectEra(era.id)">
                        <span>{{ era.short }}</span>
                        <b>{{ era.label }}</b>
                        <small>{{ eraTimeLabel(era.logTime) }}</small>
                    </button>
                </div>
            </section>

            <section class="panel-section">
                <h2>Timeline</h2>
                <label>
                    <span>log time</span>
                    <input v-model.number="logTime" type="range" :min="timelineMin" :max="timelineMax" step="0.02">
                    <strong>{{ logTime.toFixed(1) }}</strong>
                </label>
                <label>
                    <span>speed</span>
                    <input v-model.number="speed" type="range" min="0.15" max="1" step="0.05">
                    <strong>{{ speed.toFixed(2) }}</strong>
                </label>
                <div class="time-readout">
                    <span>{{ metrics.timeLabel }}</span>
                    <b>{{ metrics.temperatureLabel }}</b>
                </div>
            </section>

            <section class="panel-section">
                <h2>Layers</h2>
                <label class="checkbox-row">
                    <input v-model="layers.standard" type="checkbox">
                    <span>Standard cosmology</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="layers.qmSm" type="checkbox">
                    <span>QM/SM phase</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="layers.mtt" type="checkbox">
                    <span>MTT bookkeeping</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="layers.horizon" type="checkbox">
                    <span>Horizons and CMB</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="layers.records" type="checkbox">
                    <span>Stable records</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="layers.innerSplit" type="checkbox">
                    <span>Inner-world split</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="layers.scalePanes" type="checkbox">
                    <span>Four scale panes</span>
                </label>
            </section>

            <section class="panel-section audit">
                <h2>Source Audit</h2>
                <div class="source-item native">
                    <i>std</i>
                    <span>
                        <strong>Eras, expansion, CMB densities</strong>
                        <em>Planck-like flat LCDM baseline drives the density percentages.</em>
                    </span>
                </div>
                <div class="source-item derived">
                    <i>MTT</i>
                    <span>
                        <strong>Capacity, memory, release</strong>
                        <em>Book-inspired encoding overlay, not a replacement law.</em>
                    </span>
                </div>
                <div class="source-item scaffold">
                    <i>toy</i>
                    <span>
                        <strong>Animation and particle counts</strong>
                        <em>Visual sampling chosen for readability and performance.</em>
                    </span>
                </div>
            </section>
        </aside>

        <aside class="metrics-panel">
            <section>
                <h2>{{ currentEra.label }}</h2>
                <p>{{ currentEra.standard }}</p>
            </section>
            <section v-if="layers.qmSm">
                <h2>QM / SM</h2>
                <p>{{ currentEra.qm }}</p>
            </section>
            <section v-if="layers.mtt">
                <h2>MTT Encoding</h2>
                <p>{{ currentEra.mtt }}</p>
            </section>
            <section>
                <h2>Era Contents</h2>
                <div class="contents-list">
                    <div v-for="item in paneInventories" :key="item.label">
                        <strong>{{ item.label }}</strong>
                        <span>{{ item.text }}</span>
                    </div>
                </div>
            </section>
            <div class="metric-grid">
                <div class="metric">
                    <span>scale a</span>
                    <strong>{{ metrics.scaleLabel }}</strong>
                </div>
                <div class="metric">
                    <span>redshift z</span>
                    <strong>{{ metrics.redshiftLabel }}</strong>
                </div>
                <div class="metric">
                    <span>radiation</span>
                    <strong>{{ densityDisplay(metrics.radiation) }}</strong>
                </div>
                <div class="metric">
                    <span>matter</span>
                    <strong>{{ densityDisplay(metrics.matter) }}</strong>
                </div>
                <div class="metric">
                    <span>baryons</span>
                    <strong>{{ densityDisplay(metrics.baryons) }}</strong>
                </div>
                <div class="metric">
                    <span>dark matter</span>
                    <strong>{{ densityDisplay(metrics.darkMatter) }}</strong>
                </div>
                <div class="metric">
                    <span>dark energy</span>
                    <strong>{{ densityDisplay(metrics.darkEnergy) }}</strong>
                </div>
                <div class="metric">
                    <span>record load</span>
                    <strong>{{ percent(metrics.recordLoad) }}</strong>
                </div>
            </div>
        </aside>

        <div class="legend">
            <span><i class="dot radiation"></i> radiation</span>
            <span><i class="dot matter"></i> particles</span>
            <span><i class="dot solar"></i> stars</span>
            <span><i class="dot galaxy"></i> galaxies</span>
            <span><i class="dot cluster"></i> superclusters</span>
            <span><i class="dot record"></i> records</span>
        </div>
    </section>
</template>

<script setup lang="ts">
type EraStop = {
    id: string
    short: string
    label: string
    logTime: number
    tempLog: number
    standard: string
    qm: string
    mtt: string
    radiation: number
    matter: number
    darkEnergy: number
    anchors: number
    records: number
    capacity: number
    forgetting: number
    release: number
}

const TAU = Math.PI * 2
const timelineMin = -43
const timelineMax = 18
const minimumEraSeconds = 30
const todayLogSeconds = Math.log10(13.8e9 * 365.25 * 24 * 3600)
const cmbDensityToday = {
    radiation: 0.0000917,
    baryons: 0.0493,
    darkMatter: 0.2660,
    darkEnergy: 0.6846083,
}

const eraStops: EraStop[] = [
    {
        id: 'planck',
        short: 'P',
        label: 'Planck Edge',
        logTime: -43,
        tempLog: 32,
        standard: 'Known physics reaches an edge; a complete quantum gravity description is not supplied by the Standard Model.',
        qm: 'Quantum fields are not yet safely separable from geometry in a standard operational treatment.',
        mtt: 'The book cue is no stable public record yet: capacity and locality are not established enough to carry durable structure.',
        radiation: 1,
        matter: 0,
        darkEnergy: 0,
        anchors: 0,
        records: 0,
        capacity: 0.08,
        forgetting: 0.96,
        release: 0.2,
    },
    {
        id: 'inflation',
        short: 'I',
        label: 'Inflation',
        logTime: -35,
        tempLog: 27,
        standard: 'A rapid expansion stage flattens and stretches tiny fluctuations into horizon-scale seeds.',
        qm: 'Vacuum fluctuations are promoted into classical perturbation statistics after expansion.',
        mtt: 'Diagonal embedding appears as a branch-wide constraint: global coherence is cheap, local records are still scarce.',
        radiation: 0.82,
        matter: 0.01,
        darkEnergy: 0.17,
        anchors: 0.04,
        records: 0.02,
        capacity: 0.18,
        forgetting: 0.88,
        release: 0.36,
    },
    {
        id: 'reheating',
        short: 'R',
        label: 'Reheating',
        logTime: -32,
        tempLog: 25,
        standard: 'Inflationary energy is converted into a hot bath of particles and radiation.',
        qm: 'Fields repopulate accessible modes; thermalization becomes the useful description.',
        mtt: 'Release dominates: stored global order is paid out as propagating degrees of freedom.',
        radiation: 0.94,
        matter: 0.04,
        darkEnergy: 0.02,
        anchors: 0.1,
        records: 0.04,
        capacity: 0.24,
        forgetting: 0.82,
        release: 0.9,
    },
    {
        id: 'electroweak',
        short: 'EW',
        label: 'Electroweak Era',
        logTime: -12,
        tempLog: 15.3,
        standard: 'The hot universe supports electroweak physics before the later low-energy separation of forces.',
        qm: 'Gauge fields and relativistic particles dominate; masses and identities are temperature dependent.',
        mtt: 'Gauge freedom reads as description freedom under a locality constraint, before durable identity anchors are cheap.',
        radiation: 0.93,
        matter: 0.07,
        darkEnergy: 0,
        anchors: 0.18,
        records: 0.08,
        capacity: 0.34,
        forgetting: 0.72,
        release: 0.82,
    },
    {
        id: 'qgp',
        short: 'QG',
        label: 'Quark Plasma',
        logTime: -6,
        tempLog: 13,
        standard: 'Quarks, gluons, leptons, and photons form a dense relativistic plasma.',
        qm: 'Color confinement has not yet made isolated hadrons the right low-energy objects.',
        mtt: 'The visible labels are still poor records; transport is strong, identity is provisional.',
        radiation: 0.9,
        matter: 0.1,
        darkEnergy: 0,
        anchors: 0.24,
        records: 0.12,
        capacity: 0.42,
        forgetting: 0.64,
        release: 0.7,
    },
    {
        id: 'hadrons',
        short: 'H',
        label: 'Hadron Era',
        logTime: -4,
        tempLog: 12,
        standard: 'Cooling favors confined hadrons; protons and neutrons become usable matter carriers.',
        qm: 'QCD confinement turns color degrees of freedom into stable composite records.',
        mtt: 'Persistence becomes cheaper: internal cancellation can be hidden inside a durable outer label.',
        radiation: 0.85,
        matter: 0.15,
        darkEnergy: 0,
        anchors: 0.36,
        records: 0.22,
        capacity: 0.5,
        forgetting: 0.55,
        release: 0.58,
    },
    {
        id: 'bbn',
        short: 'N',
        label: 'Nucleosynthesis',
        logTime: 2.2,
        tempLog: 9.15,
        standard: 'Light nuclei form as the universe cools enough for deuterium and helium to survive.',
        qm: 'Nuclear reaction rates, weak freeze-out, and binding energies set primordial abundances.',
        mtt: 'Bound nuclear records appear: not every possible combination survives capacity and release tests.',
        radiation: 0.78,
        matter: 0.22,
        darkEnergy: 0,
        anchors: 0.46,
        records: 0.34,
        capacity: 0.58,
        forgetting: 0.48,
        release: 0.46,
    },
    {
        id: 'radiation',
        short: 'RAD',
        label: 'Radiation Domination',
        logTime: 8,
        tempLog: 6.1,
        standard: 'Photons and relativistic species control expansion; matter perturbations cannot yet grow freely.',
        qm: 'The photon-baryon fluid oscillates; scattering keeps light and matter tightly coupled.',
        mtt: 'Propagation wins over persistence: records are repeatedly overwritten by the coupled radiation bath.',
        radiation: 0.68,
        matter: 0.32,
        darkEnergy: 0,
        anchors: 0.5,
        records: 0.38,
        capacity: 0.62,
        forgetting: 0.42,
        release: 0.62,
    },
    {
        id: 'recombination',
        short: 'CMB',
        label: 'Recombination',
        logTime: 13.1,
        tempLog: 3.48,
        standard: 'Electrons bind with nuclei; photons decouple and the cosmic microwave background is released.',
        qm: 'Atomic states become the low-energy bookkeeping; photon mean free paths grow dramatically.',
        mtt: 'A major record boundary forms: light stops being repeatedly rewritten by charged matter.',
        radiation: 0.24,
        matter: 0.76,
        darkEnergy: 0,
        anchors: 0.65,
        records: 0.62,
        capacity: 0.7,
        forgetting: 0.3,
        release: 0.78,
    },
    {
        id: 'darkAges',
        short: 'DA',
        label: 'Dark Ages',
        logTime: 14.6,
        tempLog: 2.35,
        standard: 'Neutral gas expands and cools before the first luminous sources turn on.',
        qm: 'Atoms are stable but most matter is not yet arranged into stars or galaxies.',
        mtt: 'Records exist, but the universe has not yet built many visible re-use structures.',
        radiation: 0.1,
        matter: 0.9,
        darkEnergy: 0,
        anchors: 0.72,
        records: 0.58,
        capacity: 0.74,
        forgetting: 0.26,
        release: 0.28,
    },
    {
        id: 'stars',
        short: 'S',
        label: 'First Stars',
        logTime: 15.6,
        tempLog: 1.75,
        standard: 'Gravity collapses gas into the first stars, lighting the universe and reionizing gas.',
        qm: 'Atomic cooling, nuclear fusion, and radiative transport shape the first luminous objects.',
        mtt: 'Persistence and release cooperate: stars are durable anchors that also export energy and new records.',
        radiation: 0.04,
        matter: 0.95,
        darkEnergy: 0.01,
        anchors: 0.82,
        records: 0.74,
        capacity: 0.82,
        forgetting: 0.18,
        release: 0.6,
    },
    {
        id: 'galaxies',
        short: 'G',
        label: 'Galaxies',
        logTime: 16.8,
        tempLog: 0.95,
        standard: 'Matter domination allows structure growth into galaxies, clusters, and large-scale filaments.',
        qm: 'Microphysics supplies cooling, opacity, fusion, chemistry, and feedback inside gravitational structure.',
        mtt: 'Reusable hierarchy is the theme: stable local records nest inside larger compatibility geometry.',
        radiation: 0.01,
        matter: 0.92,
        darkEnergy: 0.07,
        anchors: 0.9,
        records: 0.86,
        capacity: 0.88,
        forgetting: 0.12,
        release: 0.42,
    },
    {
        id: 'today',
        short: 'NOW',
        label: 'Present',
        logTime: todayLogSeconds,
        tempLog: Math.log10(2.725),
        standard: 'The observed universe is old, cold, structured, and currently dark-energy dominated.',
        qm: 'SM/QM still governs local matter and radiation while GR governs large-scale geometry.',
        mtt: 'This is the book picture in mature form: many stable records survive because excess detail is forgotten.',
        radiation: 0.0001,
        matter: 0.315,
        darkEnergy: 0.685,
        anchors: 0.94,
        records: 0.92,
        capacity: 0.9,
        forgetting: 0.08,
        release: 0.34,
    },
    {
        id: 'future',
        short: 'F',
        label: 'Far Future',
        logTime: 18,
        tempLog: -0.35,
        standard: 'Continued accelerated expansion makes distant structures harder to access causally.',
        qm: 'Local bound systems can persist, but horizon-scale information becomes less reusable.',
        mtt: 'The bad-memory motif returns at the largest scale: what cannot stay mutually accessible drops out of the shared record.',
        radiation: 0,
        matter: 0.08,
        darkEnergy: 0.92,
        anchors: 0.82,
        records: 0.68,
        capacity: 0.7,
        forgetting: 0.45,
        release: 0.18,
    },
]

const shellRef = ref<HTMLElement | null>(null)
const canvasRef = ref<HTMLCanvasElement | null>(null)
const logTime = ref(timelineMin)
const speed = ref(1)
const isRunning = ref(true)
const frame = ref(0)
const layers = reactive({
    standard: true,
    qmSm: true,
    mtt: true,
    horizon: true,
    records: true,
    innerSplit: true,
    scalePanes: true,
})

let ctx: CanvasRenderingContext2D | null = null
let animationId = 0
let lastLoopTime = 0
let width = 0
let height = 0
let dpr = 1

const currentEra = computed(() => {
    let selected = eraStops[0]
    for (const era of eraStops) {
        if (logTime.value >= era.logTime) selected = era
        else break
    }
    return selected
})

const nextEra = computed(() => {
    const index = eraStops.findIndex((era) => era.id === currentEra.value.id)
    return eraStops[Math.min(eraStops.length - 1, index + 1)]
})

const eraBlend = computed(() => {
    const start = currentEra.value.logTime
    const end = nextEra.value.logTime
    if (end <= start) return 0
    return clamp01((logTime.value - start) / (end - start))
})

const eraSample = computed(() => interpolateEra(currentEra.value, nextEra.value, eraBlend.value))

const metrics = computed(() => {
    const sample = eraSample.value
    const temp = 10 ** sample.tempLog
    const scale = Math.min(1e4, 2.725 / Math.max(temp, 1e-9))
    const redshift = Math.max(0, (1 / Math.max(scale, 1e-12)) - 1)
    const density = densityFractions(scale)
    const propagation = clamp01(sample.radiation * 0.65 + sample.release * 0.35)
    const persistence = clamp01(sample.anchors * 0.55 + sample.records * 0.45)
    const recordLoad = clamp01(sample.records)
    return {
        ...sample,
        timeLabel: formatCosmicTime(logTime.value),
        temperatureLabel: formatTemperature(temp),
        scale,
        scaleLabel: formatScientific(scale),
        redshift,
        redshiftLabel: redshift > 1e5 ? formatScientific(redshift) : redshift.toLocaleString('en-US', { maximumFractionDigits: redshift > 100 ? 0 : 1 }),
        radiation: density.radiation,
        matter: density.matter,
        baryons: density.baryons,
        darkMatter: density.darkMatter,
        darkEnergy: density.darkEnergy,
        propagation,
        persistence,
        recordLoad,
    }
})

const paneInventories = computed(() => {
    const t = logTime.value
    return [
        { label: 'Particles', text: particleInventory(t) },
        { label: 'Solar', text: solarInventory(t) },
        { label: 'Galaxies', text: galaxyInventory(t) },
        { label: 'Superclusters', text: superclusterInventory(t) },
    ]
})

function interpolateEra(a: EraStop, b: EraStop, t: number) {
    return {
        tempLog: mix(a.tempLog, b.tempLog, t),
        radiation: mix(a.radiation, b.radiation, t),
        matter: mix(a.matter, b.matter, t),
        darkEnergy: mix(a.darkEnergy, b.darkEnergy, t),
        anchors: mix(a.anchors, b.anchors, t),
        records: mix(a.records, b.records, t),
        capacity: mix(a.capacity, b.capacity, t),
        forgetting: mix(a.forgetting, b.forgetting, t),
        release: mix(a.release, b.release, t),
    }
}

function densityFractions(scale: number) {
    const a = Math.max(scale, 1e-10)
    const radiation = cmbDensityToday.radiation / a ** 4
    const baryons = cmbDensityToday.baryons / a ** 3
    const darkMatter = cmbDensityToday.darkMatter / a ** 3
    const matter = baryons + darkMatter
    const darkEnergy = cmbDensityToday.darkEnergy
    const total = radiation + matter + darkEnergy
    return {
        radiation: radiation / total,
        matter: matter / total,
        baryons: baryons / total,
        darkMatter: darkMatter / total,
        darkEnergy: darkEnergy / total,
    }
}

function particleInventory(t: number) {
    if (t < -36) return 'quantum/inflationary field state; no stable particles'
    if (t < -32) return 'inflaton decay starting; stretched quantum fluctuations'
    if (t < -12) return 'hot radiation bath: gauge fields, quarks, leptons, photons'
    if (t < -6) return 'electroweak plasma: W/Z, gamma, quarks, gluons, leptons'
    if (t < -4) return 'quark-gluon plasma with photons, neutrinos, electrons, muons'
    if (t < 0) return 'hadronizing plasma: protons, neutrons, mesons, photons, leptons'
    if (t < 3.6) return 'BBN: protons, neutrons, deuterium, helium nuclei, photons, neutrinos'
    if (t < 12.9) return 'ionized plasma: nuclei plus free electrons, photons tightly coupled'
    if (t < 14.1) return 'recombination: neutral H/He forming, CMB photons decoupling'
    return 'neutral atoms, photons, neutrinos, baryons; later stars enrich elements'
}

function solarInventory(t: number) {
    if (t < 13.1) return 'none: too hot for atoms, stars, or solar systems'
    if (t < 15.25) return 'neutral H/He gas only; no stars yet'
    if (t < 16.0) return 'first Population III stars igniting from collapsing gas'
    if (t < 16.45) return 'stars and ionized bubbles; disks still rare in this view'
    if (t < todayLogSeconds) return 'stellar systems, disks, planets, metals from stellar generations'
    return 'long-lived stars, remnants, planets; star formation declining'
}

function galaxyInventory(t: number) {
    if (t < 13.1) return 'density seeds only; no neutral gas or galaxies'
    if (t < 15.4) return 'neutral gas falling into dark matter scaffolds'
    if (t < 16.0) return 'protogalactic gas clumps; first halos assembling'
    if (t < 16.85) return 'young galaxies forming by collapse and mergers'
    if (t < todayLogSeconds) return 'rotating galaxies, stars, gas, dark matter halos'
    return 'mature galaxies in expanding dark-energy dominated spacetime'
}

function superclusterInventory(t: number) {
    if (t < 13.1) return 'inflationary/acoustic seed pattern; no bound web yet'
    if (t < 16.25) return 'matter perturbations grow slowly; dark matter leads collapse'
    if (t < 17.2) return 'filaments, voids, galaxy groups, clusters assembling'
    if (t < todayLogSeconds) return 'cosmic web: clusters, superclusters, voids, dark matter'
    return 'web persists locally while dark energy stretches large separations'
}

function eraTimeLabel(logSeconds: number) {
    return formatCosmicTime(logSeconds)
}

function toggleRunning() {
    isRunning.value = !isRunning.value
}

function resetTimeline() {
    logTime.value = timelineMin
    isRunning.value = true
    lastLoopTime = 0
}

function selectEra(id: string) {
    const era = eraStops.find((entry) => entry.id === id)
    if (!era) return
    logTime.value = era.logTime
    lastLoopTime = 0
}

function resizeCanvas() {
    const canvas = canvasRef.value
    if (!canvas) return
    dpr = Math.min(window.devicePixelRatio || 1, 2)
    width = window.innerWidth
    height = window.innerHeight
    canvas.width = Math.floor(width * dpr)
    canvas.height = Math.floor(height * dpr)
    canvas.style.width = `${width}px`
    canvas.style.height = `${height}px`
    ctx = canvas.getContext('2d')
    ctx?.setTransform(dpr, 0, 0, dpr, 0, 0)
}

function loop(timestamp = 0) {
    const elapsedSeconds = lastLoopTime > 0 ? Math.min(0.1, (timestamp - lastLoopTime) / 1000) : 1 / 60
    lastLoopTime = timestamp
    if (isRunning.value) {
        const current = currentEra.value
        const next = nextEra.value
        const span = Math.max(0.001, next.logTime - current.logTime)
        const step = (span / minimumEraSeconds) * elapsedSeconds * Math.min(1, speed.value)
        logTime.value += step
        if (logTime.value >= timelineMax) {
            logTime.value = timelineMax
            isRunning.value = false
        }
    }
    frame.value += 1
    draw()
    animationId = requestAnimationFrame(loop)
}

function draw() {
    if (!ctx) return
    const context = ctx
    context.clearRect(0, 0, width, height)
    drawBackground(context)
    if (layers.scalePanes) drawScaleFrames(context)
    if (layers.innerSplit) drawInnerWorldSplit(context)
    if (layers.standard) drawExpansionField(context)
    if (layers.horizon) drawHorizon(context)
    if (layers.scalePanes) {
        drawScaleSimulations(context)
        drawPaneStatusLabels(context)
    } else {
        if (layers.standard) drawRadiation(context)
        if (layers.standard) drawMatter(context)
        if (layers.records) drawRecords(context)
        if (layers.qmSm) drawQuantumFoam(context)
    }
}

type Pane = {
    id: string
    label: string
    subtitle: string
    x: number
    y: number
    w: number
    h: number
}

function getScalePanes(): Pane[] {
    const left = width < 920 ? 12 : 370
    const right = width < 920 ? 12 : 354
    const top = width < 920 ? 66 : 86
    const bottom = width < 920 ? 52 : 72
    const gap = 12
    const availableW = Math.max(240, width - left - right)
    const availableH = Math.max(220, height - top - bottom)
    const columns = width < 760 ? 1 : 2
    const rows = columns === 1 ? 4 : 2
    const paneW = (availableW - gap * (columns - 1)) / columns
    const paneH = (availableH - gap * (rows - 1)) / rows
    const specs = [
        ['particles', 'Particles', 'fields, plasma, atoms'] as const,
        ['solar', 'Solar Systems', 'stars, disks, planets'] as const,
        ['galaxies', 'Galaxies', 'spin and structure'] as const,
        ['superclusters', 'Superclusters', 'filaments and voids'] as const,
    ]
    return specs.map(([id, label, subtitle], index) => {
        const column = columns === 1 ? 0 : index % 2
        const row = columns === 1 ? index : Math.floor(index / 2)
        return {
            id,
            label,
            subtitle,
            x: left + column * (paneW + gap),
            y: top + row * (paneH + gap),
            w: paneW,
            h: paneH,
        }
    })
}

function drawScaleFrames(context: CanvasRenderingContext2D) {
    for (const pane of getScalePanes()) {
        const gradient = context.createLinearGradient(pane.x, pane.y, pane.x + pane.w, pane.y + pane.h)
        gradient.addColorStop(0, 'rgba(9, 17, 27, 0.28)')
        gradient.addColorStop(1, 'rgba(20, 12, 22, 0.34)')
        context.fillStyle = gradient
        roundedRect(context, pane.x, pane.y, pane.w, pane.h, 8)
        context.fill()
        context.strokeStyle = 'rgba(134, 162, 172, 0.28)'
        context.lineWidth = 1
        roundedRect(context, pane.x, pane.y, pane.w, pane.h, 8)
        context.stroke()
        context.fillStyle = 'rgba(238, 247, 244, 0.92)'
        context.font = '800 12px system-ui, sans-serif'
        context.fillText(pane.label, pane.x + 12, pane.y + 18)
        context.fillStyle = 'rgba(203, 219, 214, 0.68)'
        context.font = '10px system-ui, sans-serif'
        context.fillText(pane.subtitle, pane.x + 12, pane.y + 33)
    }
}

function drawScaleSimulations(context: CanvasRenderingContext2D) {
    for (const pane of getScalePanes()) {
        context.save()
        roundedRect(context, pane.x, pane.y, pane.w, pane.h, 8)
        context.clip()
        if (pane.id === 'particles') drawParticleScale(context, pane)
        if (pane.id === 'solar') drawSolarScale(context, pane)
        if (pane.id === 'galaxies') drawGalaxyScale(context, pane)
        if (pane.id === 'superclusters') drawSuperclusterScale(context, pane)
        context.restore()
    }
}

function paneInventoryText(id: string) {
    if (id === 'particles') return particleInventory(logTime.value)
    if (id === 'solar') return solarInventory(logTime.value)
    if (id === 'galaxies') return galaxyInventory(logTime.value)
    return superclusterInventory(logTime.value)
}

function drawPaneStatusLabels(context: CanvasRenderingContext2D) {
    for (const pane of getScalePanes()) {
        const labelHeight = 38
        const gradient = context.createLinearGradient(pane.x, pane.y + pane.h - labelHeight, pane.x, pane.y + pane.h)
        gradient.addColorStop(0, 'rgba(7, 12, 19, 0)')
        gradient.addColorStop(0.28, 'rgba(7, 12, 19, 0.68)')
        gradient.addColorStop(1, 'rgba(7, 12, 19, 0.9)')
        context.fillStyle = gradient
        context.fillRect(pane.x + 1, pane.y + pane.h - labelHeight, pane.w - 2, labelHeight - 1)
        context.fillStyle = 'rgba(255, 242, 196, 0.9)'
        context.font = '10px system-ui, sans-serif'
        wrapCanvasText(context, paneInventoryText(pane.id), pane.x + 12, pane.y + pane.h - 25, pane.w - 24, 12, 2)
    }
}

function drawInnerWorldSplit(context: CanvasRenderingContext2D) {
    const strength = clamp01((8 - (logTime.value + 43)) / 8)
    const inflationEcho = smoothBand(logTime.value, -36.5, -31.2)
    if (strength <= 0.01 && inflationEcho <= 0.01) return
    const centerX = width * 0.52
    const centerY = height * 0.52
    const r = Math.min(width, height) * (0.06 + inflationEcho * 0.24 + strength * 0.12)
    context.save()
    context.globalCompositeOperation = 'lighter'
    for (const side of [-1, 1]) {
        const x = centerX + side * r * (0.32 + inflationEcho * 1.8)
        const lens = context.createRadialGradient(x, centerY, 0, x, centerY, r)
        lens.addColorStop(0, side < 0 ? `rgba(103, 232, 249, ${0.16 + strength * 0.22})` : `rgba(255, 220, 130, ${0.14 + strength * 0.2})`)
        lens.addColorStop(0.55, side < 0 ? `rgba(103, 232, 249, ${0.04 + inflationEcho * 0.08})` : `rgba(255, 128, 95, ${0.04 + inflationEcho * 0.08})`)
        lens.addColorStop(1, 'rgba(0, 0, 0, 0)')
        context.fillStyle = lens
        context.beginPath()
        context.ellipse(x, centerY, r * 0.75, r * 1.05, side * 0.26, 0, TAU)
        context.fill()
    }
    context.globalCompositeOperation = 'source-over'
    context.strokeStyle = `rgba(255, 255, 255, ${0.12 + strength * 0.24})`
    context.lineWidth = 1
    context.beginPath()
    context.arc(centerX, centerY, r * (0.92 + inflationEcho), 0, TAU)
    context.stroke()
    context.fillStyle = `rgba(238, 247, 244, ${0.22 + strength * 0.42})`
    context.font = '10px system-ui, sans-serif'
    context.textAlign = 'center'
    context.fillText(strength > 0.15 ? 'inner split before public records' : 'stretched seed constraints', centerX, centerY + r + 18)
    context.restore()
}

function drawBackground(context: CanvasRenderingContext2D) {
    const gradient = context.createLinearGradient(0, 0, width, height)
    gradient.addColorStop(0, '#05070c')
    gradient.addColorStop(0.45, '#0a1214')
    gradient.addColorStop(1, '#120b15')
    context.fillStyle = gradient
    context.fillRect(0, 0, width, height)

    const warm = context.createRadialGradient(width * 0.52, height * 0.5, 0, width * 0.52, height * 0.5, Math.max(width, height) * 0.62)
    warm.addColorStop(0, `rgba(255, 214, 128, ${0.04 + eraSample.value.radiation * 0.1})`)
    warm.addColorStop(0.45, `rgba(64, 207, 190, ${0.02 + eraSample.value.matter * 0.05})`)
    warm.addColorStop(1, 'rgba(0, 0, 0, 0)')
    context.fillStyle = warm
    context.fillRect(0, 0, width, height)
}

function drawExpansionField(context: CanvasRenderingContext2D) {
    const centerX = width * 0.52
    const centerY = height * 0.52
    const inflationStrength = smoothBand(logTime.value, -36.2, -31.2)
    const pulse = frame.value * (0.008 + inflationStrength * 0.08)
    const spacing = Math.max(18, Math.min(112, 34 + metrics.value.scale * 60 + inflationStrength * 54))
    context.save()
    context.lineWidth = 1 + inflationStrength * 1.8
    for (let i = -20; i <= 20; i++) {
        const offset = ((i + pulse) * spacing) % (spacing * 20)
        const alpha = 0.045 + metrics.value.darkEnergy * 0.045 + inflationStrength * 0.12
        context.strokeStyle = `rgba(112, 184, 175, ${alpha})`
        context.beginPath()
        context.moveTo(centerX + offset - spacing * 10, 0)
        context.lineTo(centerX + offset - spacing * 10, height)
        context.stroke()
        context.beginPath()
        context.moveTo(0, centerY + offset - spacing * 10)
        context.lineTo(width, centerY + offset - spacing * 10)
        context.stroke()
    }
    if (inflationStrength > 0.02) {
        context.strokeStyle = `rgba(255, 220, 130, ${0.18 + inflationStrength * 0.36})`
        for (let i = 0; i < 10; i++) {
            const radius = (frame.value * 5 + i * 58) % (Math.max(width, height) * 0.9)
            context.beginPath()
            context.arc(centerX, centerY, radius * (0.18 + inflationStrength), 0, TAU)
            context.stroke()
        }
    }
    context.restore()
}

function drawHorizon(context: CanvasRenderingContext2D) {
    const radius = Math.min(width, height) * (0.18 + 0.34 * clamp01((logTime.value + 43) / 61))
    const centerX = width * 0.52
    const centerY = height * 0.52
    context.save()
    context.lineWidth = 1.2
    context.strokeStyle = 'rgba(255, 236, 178, 0.32)'
    context.setLineDash([10, 10])
    context.beginPath()
    context.arc(centerX, centerY, radius, 0, TAU)
    context.stroke()
    context.setLineDash([])

    const cmbStrength = smoothBand(logTime.value, 12.9, 14.2)
    if (cmbStrength > 0.01) {
        context.lineWidth = 3
        context.strokeStyle = `rgba(255, 170, 95, ${0.16 + cmbStrength * 0.34})`
        context.beginPath()
        context.arc(centerX, centerY, radius * (0.78 + cmbStrength * 0.08), 0, TAU)
        context.stroke()
    }
    context.restore()
}

function drawRadiation(context: CanvasRenderingContext2D) {
    const count = Math.round(28 + metrics.value.radiation * 120)
    const centerX = width * 0.52
    const centerY = height * 0.52
    const spread = Math.max(width, height) * (0.16 + 0.56 * clamp01((logTime.value + 43) / 61))
    context.save()
    context.lineWidth = 1.1
    for (let i = 0; i < count; i++) {
        const seed = i * 19.739
        const angle = seed + frame.value * 0.006 * (1.5 + metrics.value.radiation)
        const radius = spread * fract(Math.sin(seed) * 4000 + frame.value * 0.0008)
        const x = centerX + Math.cos(angle) * radius
        const y = centerY + Math.sin(angle * 1.17) * radius * 0.72
        const wave = 9 + 28 * metrics.value.radiation
        context.strokeStyle = `rgba(255, 220, 130, ${0.06 + metrics.value.radiation * 0.22})`
        context.beginPath()
        for (let k = 0; k < 18; k++) {
            const p = k / 17
            const dx = (p - 0.5) * wave
            const dy = Math.sin(p * TAU * 2 + frame.value * 0.08 + seed) * 3.5
            const px = x + Math.cos(angle) * dx - Math.sin(angle) * dy
            const py = y + Math.sin(angle) * dx + Math.cos(angle) * dy
            if (k === 0) context.moveTo(px, py)
            else context.lineTo(px, py)
        }
        context.stroke()
    }
    context.restore()
}

function drawMatter(context: CanvasRenderingContext2D) {
    const centerX = width * 0.52
    const centerY = height * 0.52
    const count = Math.round(8 + metrics.value.matter * 90)
    const clustering = clamp01((metrics.value.records + metrics.value.anchors) * 0.5)
    const spread = Math.min(width, height) * (0.12 + 0.42 * clamp01((logTime.value + 30) / 48))
    context.save()
    for (let i = 0; i < count; i++) {
        const seed = i * 91.17
        const arm = i % 5
        const angle = seed + arm * 1.17 + frame.value * 0.0015
        const radius = spread * (0.08 + 0.92 * fract(Math.sin(seed) * 9000))
        const filament = clustering * Math.sin(angle * 2.2 + radius * 0.01)
        const x = centerX + Math.cos(angle + filament * 0.8) * radius
        const y = centerY + Math.sin(angle * 0.88 - filament * 0.7) * radius * 0.76
        const size = 1.5 + 5.5 * clustering * fract(Math.cos(seed) * 7000)
        const glow = context.createRadialGradient(x, y, 0, x, y, size * 5.5)
        glow.addColorStop(0, `rgba(103, 232, 249, ${0.2 + clustering * 0.25})`)
        glow.addColorStop(0.32, `rgba(111, 245, 190, ${0.12 + clustering * 0.2})`)
        glow.addColorStop(1, 'rgba(111, 245, 190, 0)')
        context.fillStyle = glow
        context.beginPath()
        context.arc(x, y, size * 5.5, 0, TAU)
        context.fill()
        context.fillStyle = 'rgba(222, 255, 246, 0.9)'
        context.beginPath()
        context.arc(x, y, Math.max(1.2, size * 0.62), 0, TAU)
        context.fill()
    }
    context.restore()
}

function drawRecords(context: CanvasRenderingContext2D) {
    const recordStrength = metrics.value.recordLoad
    if (recordStrength < 0.05) return
    const centerX = width * 0.52
    const centerY = height * 0.52
    const count = Math.round(10 + recordStrength * 48)
    context.save()
    context.strokeStyle = `rgba(255, 255, 255, ${0.04 + recordStrength * 0.1})`
    context.lineWidth = 0.9
    for (let i = 0; i < count; i++) {
        const seed = i * 63.31
        const angle = seed + Math.sin(frame.value * 0.003 + seed) * 0.2
        const radius = Math.min(width, height) * (0.07 + 0.45 * fract(Math.sin(seed) * 4000))
        const x = centerX + Math.cos(angle) * radius
        const y = centerY + Math.sin(angle * 1.03) * radius * 0.78
        const r = 4 + 12 * fract(Math.cos(seed) * 5000)
        context.beginPath()
        context.arc(x, y, r, 0, TAU)
        context.stroke()
    }
    context.restore()
}

function drawQuantumFoam(context: CanvasRenderingContext2D) {
    const strength = clamp01(1 - metrics.value.records)
    if (strength < 0.05) return
    context.save()
    for (let i = 0; i < 80; i++) {
        const seed = i * 12.989
        const x = fract(Math.sin(seed + frame.value * 0.003) * 43758.5453) * width
        const y = fract(Math.cos(seed * 1.61 + frame.value * 0.002) * 24634.6345) * height
        const r = 0.7 + strength * 2.6 * fract(Math.sin(seed) * 11000)
        context.fillStyle = `rgba(184, 138, 255, ${0.025 + strength * 0.08})`
        context.beginPath()
        context.arc(x, y, r, 0, TAU)
        context.fill()
    }
    context.restore()
}

function drawParticleScale(context: CanvasRenderingContext2D, pane: Pane) {
    const early = clamp01((4 - (logTime.value + 43)) / 4)
    const inflation = smoothBand(logTime.value, -36.2, -31.2)
    const plasma = smoothBand(logTime.value, -33, 9)
    const atoms = clamp01((logTime.value - 13.05) / 2.2)
    const cx = pane.x + pane.w * 0.5
    const cy = pane.y + pane.h * 0.55
    const base = Math.min(pane.w, pane.h)

    if (early > 0.01 || inflation > 0.01) {
        for (const side of [-1, 1]) {
            const x = cx + side * base * (0.08 + inflation * 0.24)
            const r = base * (0.18 + inflation * 0.2)
            const split = context.createRadialGradient(x, cy, 0, x, cy, r)
            split.addColorStop(0, side < 0 ? `rgba(103, 232, 249, ${0.22 + early * 0.26})` : `rgba(255, 220, 130, ${0.2 + early * 0.24})`)
            split.addColorStop(1, 'rgba(0, 0, 0, 0)')
            context.fillStyle = split
            context.beginPath()
            context.ellipse(x, cy, r * 0.58, r, side * 0.5, 0, TAU)
            context.fill()
        }
    }

    const count = Math.round(50 + metrics.value.radiation * 110 + plasma * 80)
    for (let i = 0; i < count; i++) {
        const seed = i * 37.721
        const spin = frame.value * (0.006 + plasma * 0.012)
        const angle = seed + spin
        const radius = base * (0.05 + 0.46 * fract(Math.sin(seed) * 7000 + frame.value * 0.0005))
        const x = cx + Math.cos(angle) * radius * (1 + inflation * 1.8)
        const y = cy + Math.sin(angle * 1.27) * radius * 0.68
        const kind = i % 6
        const alpha = 0.12 + metrics.value.radiation * 0.2
        context.fillStyle = kind < 2
            ? `rgba(255, 220, 130, ${alpha})`
            : kind < 4
                ? `rgba(103, 232, 249, ${0.1 + plasma * 0.22})`
                : `rgba(111, 245, 190, ${0.08 + atoms * 0.24})`
        context.beginPath()
        context.arc(x, y, 1.1 + atoms * 1.6 + fract(Math.cos(seed) * 5000) * 1.8, 0, TAU)
        context.fill()
        if (atoms > 0.25 && i % 13 === 0) {
            context.strokeStyle = `rgba(111, 245, 190, ${0.12 + atoms * 0.18})`
            context.beginPath()
            context.arc(x, y, 5 + atoms * 8, 0, TAU)
            context.stroke()
        }
    }

    if (atoms > 0.08) drawCoolingAtoms(context, pane, atoms)
    drawNucleosynthesisPackets(context, pane, smoothBand(logTime.value, 1.2, 3.6))
    drawPhotonDecoupling(context, pane, smoothBand(logTime.value, 12.9, 14.1))

    if (layers.qmSm) {
        const foam = clamp01(1 - metrics.value.records)
        context.strokeStyle = `rgba(184, 138, 255, ${0.04 + foam * 0.08})`
        context.lineWidth = 0.8
        for (let i = 0; i < 18; i++) {
            const y = pane.y + pane.h * (0.18 + i * 0.035)
            context.beginPath()
            for (let k = 0; k <= 36; k++) {
                const x = pane.x + (k / 36) * pane.w
                const dy = Math.sin(k * 0.75 + frame.value * 0.05 + i) * foam * 3
                if (k === 0) context.moveTo(x, y + dy)
                else context.lineTo(x, y + dy)
            }
            context.stroke()
        }
    }
}

function drawSolarScale(context: CanvasRenderingContext2D, pane: Pane) {
    const starBirth = smoothBand(logTime.value, 15.25, 16.55)
    const matureStars = clamp01((logTime.value - 15.85) / 1.55)
    const systems = clamp01((logTime.value - 16.45) / 1.45)
    const cx = pane.x + pane.w * 0.5
    const cy = pane.y + pane.h * 0.55
    const base = Math.min(pane.w, pane.h)

    if (logTime.value < 13.1) {
        drawDormantScaleMessage(context, pane, 'plasma era: no atoms or stars')
        drawHotPlasmaVeil(context, pane, 0.16 + metrics.value.radiation * 0.18)
        return
    }

    if (starBirth < 0.02 && matureStars < 0.02) {
        drawDormantScaleMessage(context, pane, 'neutral gas waits for collapse')
        drawGasCloud(context, pane, 0.16 + clamp01((logTime.value - 13.1) / 2.2) * 0.18)
        drawCollapseFlow(context, pane, clamp01((logTime.value - 14.55) / 1.35))
        return
    }

    drawGasCloud(context, pane, 0.08 + (1 - matureStars) * 0.16)
    drawCollapseFlow(context, pane, 0.35 + starBirth * 0.45)
    const starCount = Math.round(2 + starBirth * 10 + matureStars * 14)
    for (let i = 0; i < starCount; i++) {
        const seed = i * 87.23
        const angle = seed + frame.value * 0.0018
        const radius = base * (0.08 + fract(Math.sin(seed) * 3000) * 0.36)
        const x = cx + Math.cos(angle) * radius
        const y = cy + Math.sin(angle * 1.33) * radius * 0.62
        drawStar(context, x, y, 3 + 7 * fract(Math.cos(seed) * 5000), 0.35 + matureStars * 0.45)
        if (starBirth > 0.05) drawIgnitionFlash(context, x, y, starBirth, seed)
        if (systems > 0.12 && i % 3 === 0) drawPlanetaryDisk(context, x, y, 14 + systems * 26, angle)
    }
}

function drawGalaxyScale(context: CanvasRenderingContext2D, pane: Pane) {
    const galaxyBirth = smoothBand(logTime.value, 16.0, 17.75)
    const mature = clamp01((logTime.value - 16.85) / 1.65)
    const cx = pane.x + pane.w * 0.5
    const cy = pane.y + pane.h * 0.55
    const base = Math.min(pane.w, pane.h)

    if (logTime.value < 13.1) {
        drawDormantScaleMessage(context, pane, 'density seeds only')
        drawAcousticSeeds(context, pane, clamp01((logTime.value + 4) / 17) * 0.7)
        return
    }

    if (galaxyBirth < 0.03 && mature < 0.02) {
        drawDormantScaleMessage(context, pane, logTime.value < 15.4 ? 'neutral gas and dark scaffold' : 'protogalactic collapse')
        drawGasCloud(context, pane, 0.08 + clamp01((logTime.value - 13.1) / 2.6) * 0.08)
        drawInvisibleHalo(context, pane, clamp01((logTime.value - 13.2) / 2.8))
        drawMergerClumps(context, pane, clamp01((logTime.value - 15.45) / 1.1))
        return
    }

    drawInvisibleHalo(context, pane, 0.45 + mature * 0.35)
    drawMergerClumps(context, pane, Math.max(0, 1 - mature) * galaxyBirth)
    const galaxies = Math.round(1 + mature * 5)
    for (let g = 0; g < galaxies; g++) {
        const seed = g * 121.77
        const x = cx + Math.cos(seed) * base * 0.22 * mature
        const y = cy + Math.sin(seed * 1.4) * base * 0.14 * mature
        drawSpiralGalaxy(context, x, y, base * (0.18 + 0.08 * fract(seed)), seed + frame.value * 0.002 * (1 + mature), galaxyBirth)
    }
}

function drawSuperclusterScale(context: CanvasRenderingContext2D, pane: Pane) {
    const structure = clamp01((logTime.value - 16.25) / 2.05)
    const darkEnergySpread = clamp01((logTime.value - todayLogSeconds + 0.15) / 1.5)
    if (structure < 0.03) {
        drawDormantScaleMessage(context, pane, logTime.value < 13.1 ? 'acoustic horizon seeds' : 'matter perturbations growing')
        drawAcousticSeeds(context, pane, clamp01((logTime.value + 4) / 17))
        return
    }

    drawAcousticSeeds(context, pane, Math.max(0.12, 1 - structure * 0.35))
    const points = []
    for (let i = 0; i < 36; i++) {
        const seed = i * 53.819
        const x = pane.x + pane.w * (0.12 + 0.76 * fract(Math.sin(seed) * 8000))
        const y = pane.y + pane.h * (0.2 + 0.64 * fract(Math.cos(seed * 1.43) * 9000))
        const expansionPush = 1 + darkEnergySpread * 0.16
        const dx = x - (pane.x + pane.w * 0.5)
        const dy = y - (pane.y + pane.h * 0.55)
        points.push({
            x: mix(pane.x + pane.w * 0.5, pane.x + pane.w * 0.5 + dx * expansionPush, structure),
            y: mix(pane.y + pane.h * 0.55, pane.y + pane.h * 0.55 + dy * expansionPush, structure),
        })
    }

    context.save()
    context.lineWidth = 0.8 + structure * 1.2
    for (let i = 0; i < points.length; i++) {
        for (let j = i + 1; j < points.length; j++) {
            const a = points[i]
            const b = points[j]
            const distance = Math.hypot(a.x - b.x, a.y - b.y)
            if (distance > pane.w * (0.18 + darkEnergySpread * 0.06)) continue
            const alpha = (1 - distance / (pane.w * 0.24)) * structure * (0.14 - darkEnergySpread * 0.04)
            context.strokeStyle = `rgba(103, 232, 249, ${Math.max(0.015, alpha)})`
            context.beginPath()
            context.moveTo(a.x, a.y)
            context.lineTo(b.x, b.y)
            context.stroke()
        }
    }
    for (const point of points) {
        const glow = context.createRadialGradient(point.x, point.y, 0, point.x, point.y, 12 + structure * 14)
        glow.addColorStop(0, `rgba(255, 255, 255, ${0.18 + structure * 0.22})`)
        glow.addColorStop(0.45, `rgba(111, 245, 190, ${0.08 + structure * 0.16})`)
        glow.addColorStop(1, 'rgba(111, 245, 190, 0)')
        context.fillStyle = glow
        context.beginPath()
        context.arc(point.x, point.y, 12 + structure * 14, 0, TAU)
        context.fill()
    }
    context.strokeStyle = `rgba(20, 8, 30, ${0.18 + darkEnergySpread * 0.24})`
    context.lineWidth = 1.2
    for (let i = 0; i < 5; i++) {
        const seed = i * 17.11
        context.beginPath()
        context.ellipse(
            pane.x + pane.w * (0.2 + 0.6 * fract(Math.sin(seed) * 4000)),
            pane.y + pane.h * (0.25 + 0.55 * fract(Math.cos(seed) * 3000)),
            pane.w * (0.07 + 0.05 * fract(seed)),
            pane.h * (0.06 + 0.04 * fract(seed * 2.1)),
            seed,
            0,
            TAU,
        )
        context.stroke()
    }
    context.restore()
}

function drawGasCloud(context: CanvasRenderingContext2D, pane: Pane, alpha: number) {
    const cx = pane.x + pane.w * 0.5
    const cy = pane.y + pane.h * 0.55
    const r = Math.min(pane.w, pane.h) * 0.48
    const gradient = context.createRadialGradient(cx, cy, 0, cx, cy, r)
    gradient.addColorStop(0, `rgba(103, 232, 249, ${alpha})`)
    gradient.addColorStop(0.45, `rgba(255, 220, 130, ${alpha * 0.45})`)
    gradient.addColorStop(1, 'rgba(0, 0, 0, 0)')
    context.fillStyle = gradient
    context.beginPath()
    context.ellipse(cx, cy, r, r * 0.55, Math.sin(frame.value * 0.002) * 0.4, 0, TAU)
    context.fill()
}

function drawHotPlasmaVeil(context: CanvasRenderingContext2D, pane: Pane, alpha: number) {
    const cx = pane.x + pane.w * 0.5
    const cy = pane.y + pane.h * 0.55
    const base = Math.min(pane.w, pane.h)
    context.save()
    const gradient = context.createRadialGradient(cx, cy, 0, cx, cy, base * 0.52)
    gradient.addColorStop(0, `rgba(255, 220, 130, ${alpha})`)
    gradient.addColorStop(0.46, `rgba(255, 112, 90, ${alpha * 0.44})`)
    gradient.addColorStop(1, 'rgba(255, 112, 90, 0)')
    context.fillStyle = gradient
    context.beginPath()
    context.ellipse(cx, cy, base * 0.48, base * 0.3, 0, 0, TAU)
    context.fill()
    context.strokeStyle = `rgba(255, 220, 130, ${alpha * 0.62})`
    context.lineWidth = 0.8
    for (let i = 0; i < 12; i++) {
        const y = pane.y + pane.h * (0.24 + i * 0.038)
        context.beginPath()
        for (let k = 0; k <= 32; k++) {
            const x = pane.x + pane.w * (0.12 + k * 0.024)
            const dy = Math.sin(k * 0.8 + i + frame.value * 0.08) * 2.5
            if (k === 0) context.moveTo(x, y + dy)
            else context.lineTo(x, y + dy)
        }
        context.stroke()
    }
    context.restore()
}

function drawCoolingAtoms(context: CanvasRenderingContext2D, pane: Pane, strength: number) {
    const count = Math.round(5 + strength * 18)
    const base = Math.min(pane.w, pane.h)
    const cx = pane.x + pane.w * 0.5
    const cy = pane.y + pane.h * 0.55
    context.save()
    for (let i = 0; i < count; i++) {
        const seed = i * 49.31
        const angle = seed + frame.value * 0.0009
        const radius = base * (0.08 + 0.42 * fract(Math.sin(seed) * 7000))
        const x = cx + Math.cos(angle) * radius
        const y = cy + Math.sin(angle * 1.21) * radius * 0.66
        const orbit = 6 + strength * 13 * fract(Math.cos(seed) * 4000)
        context.strokeStyle = `rgba(111, 245, 190, ${0.1 + strength * 0.2})`
        context.lineWidth = 0.8
        context.beginPath()
        context.ellipse(x, y, orbit, orbit * 0.42, angle, 0, TAU)
        context.stroke()
        context.fillStyle = `rgba(255, 248, 220, ${0.58 + strength * 0.3})`
        context.beginPath()
        context.arc(x, y, 1.5 + strength, 0, TAU)
        context.fill()
        const electronAngle = frame.value * 0.025 + seed
        context.fillStyle = `rgba(103, 232, 249, ${0.46 + strength * 0.3})`
        context.beginPath()
        context.arc(x + Math.cos(electronAngle) * orbit, y + Math.sin(electronAngle) * orbit * 0.42, 1.3, 0, TAU)
        context.fill()
    }
    context.restore()
}

function drawNucleosynthesisPackets(context: CanvasRenderingContext2D, pane: Pane, strength: number) {
    if (strength <= 0.02) return
    const cx = pane.x + pane.w * 0.5
    const cy = pane.y + pane.h * 0.55
    const base = Math.min(pane.w, pane.h)
    context.save()
    for (let i = 0; i < 12; i++) {
        const seed = i * 31.41
        const angle = seed + frame.value * 0.004
        const radius = base * (0.08 + 0.38 * fract(Math.sin(seed) * 6000))
        const x = cx + Math.cos(angle) * radius
        const y = cy + Math.sin(angle * 1.19) * radius * 0.66
        const nucleons = i % 4 === 0 ? 4 : i % 3 === 0 ? 3 : 2
        const packetR = 3.2 + strength * 2.5
        context.strokeStyle = `rgba(255, 220, 130, ${0.16 + strength * 0.2})`
        context.lineWidth = 0.9
        context.beginPath()
        context.arc(x, y, packetR * 2.2, 0, TAU)
        context.stroke()
        for (let n = 0; n < nucleons; n++) {
            const a = n * TAU / nucleons + frame.value * 0.01
            context.fillStyle = n % 2 === 0 ? `rgba(103, 232, 249, ${0.62 + strength * 0.24})` : `rgba(255, 245, 190, ${0.62 + strength * 0.24})`
            context.beginPath()
            context.arc(x + Math.cos(a) * packetR, y + Math.sin(a) * packetR, 2.3, 0, TAU)
            context.fill()
        }
    }
    context.fillStyle = `rgba(255, 220, 130, ${0.45 + strength * 0.28})`
    context.font = '10px system-ui, sans-serif'
    context.textAlign = 'center'
    context.fillText('light nuclei survive', pane.x + pane.w * 0.5, pane.y + pane.h - 14)
    context.textAlign = 'left'
    context.restore()
}

function drawPhotonDecoupling(context: CanvasRenderingContext2D, pane: Pane, strength: number) {
    if (strength <= 0.02) return
    const cx = pane.x + pane.w * 0.5
    const cy = pane.y + pane.h * 0.55
    const base = Math.min(pane.w, pane.h)
    context.save()
    context.lineWidth = 1
    for (let i = 0; i < 28; i++) {
        const seed = i * 18.13
        const angle = seed + Math.sin(frame.value * 0.015 + seed) * 0.08
        const start = base * (0.05 + 0.08 * fract(seed))
        const end = base * (0.22 + strength * 0.36 + 0.12 * fract(Math.sin(seed) * 4000))
        const alpha = strength * (0.1 + 0.22 * fract(Math.cos(seed) * 5000))
        context.strokeStyle = `rgba(255, 220, 130, ${alpha})`
        context.beginPath()
        context.moveTo(cx + Math.cos(angle) * start, cy + Math.sin(angle) * start * 0.7)
        context.lineTo(cx + Math.cos(angle) * end, cy + Math.sin(angle) * end * 0.7)
        context.stroke()
    }
    context.strokeStyle = `rgba(255, 150, 90, ${0.18 + strength * 0.28})`
    context.lineWidth = 1.4
    context.beginPath()
    context.ellipse(cx, cy, base * (0.18 + strength * 0.16), base * (0.12 + strength * 0.1), 0, 0, TAU)
    context.stroke()
    context.restore()
}

function drawCollapseFlow(context: CanvasRenderingContext2D, pane: Pane, strength: number) {
    if (strength <= 0.02) return
    const cx = pane.x + pane.w * 0.5
    const cy = pane.y + pane.h * 0.55
    const base = Math.min(pane.w, pane.h)
    context.save()
    context.strokeStyle = `rgba(255, 220, 130, ${0.08 + strength * 0.18})`
    context.lineWidth = 0.9
    for (let i = 0; i < 14; i++) {
        const seed = i * 23.7
        const angle = seed + frame.value * 0.003
        const outer = base * (0.18 + 0.32 * fract(Math.sin(seed) * 6000))
        const inner = outer * (0.58 - strength * 0.22)
        context.beginPath()
        context.moveTo(cx + Math.cos(angle) * outer, cy + Math.sin(angle) * outer * 0.62)
        context.lineTo(cx + Math.cos(angle + strength * 0.18) * inner, cy + Math.sin(angle + strength * 0.18) * inner * 0.62)
        context.stroke()
    }
    context.restore()
}

function drawIgnitionFlash(context: CanvasRenderingContext2D, x: number, y: number, strength: number, seed: number) {
    const pulse = 0.5 + 0.5 * Math.sin(frame.value * 0.08 + seed)
    const radius = (8 + strength * 28) * pulse
    context.save()
    context.strokeStyle = `rgba(255, 245, 190, ${strength * (0.12 + pulse * 0.28)})`
    context.lineWidth = 1.2
    context.beginPath()
    context.arc(x, y, radius, 0, TAU)
    context.stroke()
    context.restore()
}

function drawMergerClumps(context: CanvasRenderingContext2D, pane: Pane, strength: number) {
    if (strength <= 0.02) return
    const cx = pane.x + pane.w * 0.5
    const cy = pane.y + pane.h * 0.55
    const base = Math.min(pane.w, pane.h)
    context.save()
    for (let i = 0; i < 9; i++) {
        const seed = i * 41.27
        const angle = seed + frame.value * 0.0025
        const wide = base * (0.35 + 0.15 * fract(Math.sin(seed) * 2000))
        const close = base * (0.08 + 0.14 * fract(Math.cos(seed) * 3000))
        const radius = mix(wide, close, strength)
        const x = cx + Math.cos(angle) * radius
        const y = cy + Math.sin(angle * 1.18) * radius * 0.62
        const glow = context.createRadialGradient(x, y, 0, x, y, 14 + strength * 18)
        glow.addColorStop(0, `rgba(103, 232, 249, ${0.14 + strength * 0.2})`)
        glow.addColorStop(1, 'rgba(103, 232, 249, 0)')
        context.fillStyle = glow
        context.beginPath()
        context.arc(x, y, 14 + strength * 18, 0, TAU)
        context.fill()
    }
    context.restore()
}

function drawInvisibleHalo(context: CanvasRenderingContext2D, pane: Pane, strength: number) {
    if (strength <= 0.02) return
    const cx = pane.x + pane.w * 0.5
    const cy = pane.y + pane.h * 0.55
    const base = Math.min(pane.w, pane.h)
    context.save()
    context.strokeStyle = `rgba(184, 138, 255, ${0.08 + strength * 0.14})`
    context.lineWidth = 1
    context.setLineDash([4, 7])
    for (let i = 0; i < 4; i++) {
        const r = base * (0.16 + i * 0.075 + strength * 0.06)
        context.beginPath()
        context.ellipse(cx, cy, r, r * (0.52 + i * 0.04), i * 0.28 + frame.value * 0.0008, 0, TAU)
        context.stroke()
    }
    context.setLineDash([])
    context.fillStyle = `rgba(184, 138, 255, ${0.2 + strength * 0.16})`
    context.font = '10px system-ui, sans-serif'
    context.textAlign = 'center'
    context.fillText('gravitational scaffold', cx, pane.y + pane.h - 14)
    context.textAlign = 'left'
    context.restore()
}

function drawAcousticSeeds(context: CanvasRenderingContext2D, pane: Pane, strength: number) {
    if (strength <= 0.02) return
    const cx = pane.x + pane.w * 0.5
    const cy = pane.y + pane.h * 0.55
    const base = Math.min(pane.w, pane.h)
    context.save()
    context.lineWidth = 0.9
    for (let i = 0; i < 7; i++) {
        const seed = i * 9.91
        const r = base * (0.1 + i * 0.055 + 0.02 * Math.sin(frame.value * 0.02 + seed))
        context.strokeStyle = `rgba(255, 220, 130, ${strength * (0.04 + i * 0.012)})`
        context.beginPath()
        context.ellipse(cx, cy, r, r * (0.55 + 0.06 * Math.sin(seed)), seed * 0.2, 0, TAU)
        context.stroke()
    }
    for (let i = 0; i < 18; i++) {
        const seed = i * 74.12
        const x = pane.x + pane.w * (0.14 + 0.72 * fract(Math.sin(seed) * 7000))
        const y = pane.y + pane.h * (0.22 + 0.6 * fract(Math.cos(seed) * 8000))
        context.fillStyle = `rgba(255, 255, 255, ${0.04 + strength * 0.09})`
        context.beginPath()
        context.arc(x, y, 1.2 + strength * 2.6 * fract(seed), 0, TAU)
        context.fill()
    }
    context.restore()
}

function drawDormantScaleMessage(context: CanvasRenderingContext2D, pane: Pane, text: string) {
    context.fillStyle = 'rgba(203, 219, 214, 0.5)'
    context.font = '11px system-ui, sans-serif'
    context.textAlign = 'center'
    context.fillText(text, pane.x + pane.w * 0.5, pane.y + pane.h * 0.55)
    context.textAlign = 'left'
}

function drawStar(context: CanvasRenderingContext2D, x: number, y: number, radius: number, alpha: number) {
    const glow = context.createRadialGradient(x, y, 0, x, y, radius * 7)
    glow.addColorStop(0, `rgba(255, 255, 235, ${alpha})`)
    glow.addColorStop(0.18, `rgba(255, 212, 110, ${alpha * 0.82})`)
    glow.addColorStop(1, 'rgba(255, 160, 80, 0)')
    context.fillStyle = glow
    context.beginPath()
    context.arc(x, y, radius * 7, 0, TAU)
    context.fill()
    context.fillStyle = 'rgba(255, 248, 220, 0.95)'
    context.beginPath()
    context.arc(x, y, radius, 0, TAU)
    context.fill()
}

function drawPlanetaryDisk(context: CanvasRenderingContext2D, x: number, y: number, radius: number, angle: number) {
    context.save()
    context.translate(x, y)
    context.rotate(angle)
    context.strokeStyle = 'rgba(255, 255, 255, 0.18)'
    context.lineWidth = 0.8
    for (let i = 1; i <= 3; i++) {
        context.beginPath()
        context.ellipse(0, 0, radius * (0.4 + i * 0.22), radius * (0.13 + i * 0.05), 0, 0, TAU)
        context.stroke()
    }
    for (let i = 0; i < 3; i++) {
        const p = frame.value * 0.015 * (i + 1) + i * 2.1
        context.fillStyle = i === 0 ? '#67e8f9' : i === 1 ? '#6ff5be' : '#fde68a'
        context.beginPath()
        context.arc(Math.cos(p) * radius * (0.46 + i * 0.16), Math.sin(p) * radius * (0.14 + i * 0.04), 1.7, 0, TAU)
        context.fill()
    }
    context.restore()
}

function drawSpiralGalaxy(context: CanvasRenderingContext2D, x: number, y: number, radius: number, rotation: number, alpha: number) {
    context.save()
    context.translate(x, y)
    context.rotate(rotation)
    const core = context.createRadialGradient(0, 0, 0, 0, 0, radius * 0.28)
    core.addColorStop(0, `rgba(255, 248, 220, ${0.45 + alpha * 0.35})`)
    core.addColorStop(1, 'rgba(255, 220, 130, 0)')
    context.fillStyle = core
    context.beginPath()
    context.arc(0, 0, radius * 0.32, 0, TAU)
    context.fill()
    context.lineWidth = 1.2
    for (let arm = 0; arm < 3; arm++) {
        const stars: Array<{ x: number, y: number, r: number, a: number }> = []
        context.strokeStyle = arm === 0 ? `rgba(103, 232, 249, ${0.14 + alpha * 0.22})` : `rgba(255, 255, 255, ${0.08 + alpha * 0.14})`
        context.beginPath()
        for (let i = 0; i < 78; i++) {
            const p = i / 77
            const angle = arm * TAU / 3 + p * 4.8
            const r = radius * p
            const px = Math.cos(angle) * r
            const py = Math.sin(angle) * r * 0.42
            if (i === 0) context.moveTo(px, py)
            else context.lineTo(px, py)
            if (i % 9 === 0) {
                stars.push({ x: px, y: py, r: 0.9 + p * 1.4, a: 0.12 + alpha * 0.22 })
            }
        }
        context.stroke()
        for (const star of stars) {
            context.fillStyle = `rgba(255, 245, 220, ${star.a})`
            context.beginPath()
            context.arc(star.x, star.y, star.r, 0, TAU)
            context.fill()
        }
    }
    context.restore()
}

function roundedRect(context: CanvasRenderingContext2D, x: number, y: number, w: number, h: number, r: number) {
    const radius = Math.min(r, w / 2, h / 2)
    context.beginPath()
    context.moveTo(x + radius, y)
    context.lineTo(x + w - radius, y)
    context.quadraticCurveTo(x + w, y, x + w, y + radius)
    context.lineTo(x + w, y + h - radius)
    context.quadraticCurveTo(x + w, y + h, x + w - radius, y + h)
    context.lineTo(x + radius, y + h)
    context.quadraticCurveTo(x, y + h, x, y + h - radius)
    context.lineTo(x, y + radius)
    context.quadraticCurveTo(x, y, x + radius, y)
}

function wrapCanvasText(context: CanvasRenderingContext2D, text: string, x: number, y: number, maxWidth: number, lineHeight: number, maxLines: number) {
    const words = text.split(' ')
    let line = ''
    let lines = 0
    for (const word of words) {
        const testLine = line ? `${line} ${word}` : word
        if (context.measureText(testLine).width > maxWidth && line) {
            context.fillText(lines === maxLines - 1 ? `${line}...` : line, x, y + lines * lineHeight)
            lines += 1
            line = word
            if (lines >= maxLines) return
        } else {
            line = testLine
        }
    }
    if (line && lines < maxLines) context.fillText(line, x, y + lines * lineHeight)
}

function smoothBand(value: number, start: number, end: number) {
    return clamp01((value - start) / Math.max(0.001, end - start)) * clamp01((end + 0.8 - value) / 0.8)
}

function formatCosmicTime(logSeconds: number) {
    const seconds = 10 ** logSeconds
    if (logSeconds < -30) return `10^${logSeconds.toFixed(1)} s`
    if (seconds < 1) return `${formatScientific(seconds)} s`
    if (seconds < 60) return `${seconds.toFixed(1)} s`
    const years = seconds / (365.25 * 24 * 3600)
    if (years < 1) return `${(seconds / 60).toFixed(1)} min`
    if (years < 1e3) return `${years.toFixed(1)} yr`
    if (years < 1e6) return `${(years / 1e3).toFixed(1)} kyr`
    if (years < 1e9) return `${(years / 1e6).toFixed(1)} Myr`
    return `${(years / 1e9).toFixed(2)} Gyr`
}

function formatTemperature(kelvin: number) {
    if (kelvin > 1e6 || kelvin < 0.01) return `${formatScientific(kelvin)} K`
    return `${kelvin.toLocaleString('en-US', { maximumFractionDigits: kelvin > 100 ? 0 : 2 })} K`
}

function formatScientific(value: number) {
    if (!Number.isFinite(value) || value === 0) return '0'
    const exponent = Math.floor(Math.log10(Math.abs(value)))
    const mantissa = value / 10 ** exponent
    return `${mantissa.toFixed(2)}e${exponent}`
}

function percent(value: number) {
    return `${Math.round(clamp01(value) * 100)}%`
}

function densityPercent(value: number) {
    const percentValue = clamp01(value) * 100
    if (percentValue === 0) return '0%'
    if (percentValue < 0.01) return `${percentValue.toFixed(3)}%`
    if (percentValue < 0.1) return `${percentValue.toFixed(2)}%`
    if (percentValue < 10) return `${percentValue.toFixed(1)}%`
    return `${percentValue.toFixed(1)}%`
}

function densityDisplay(value: number) {
    if (logTime.value < -32) return 'pre-LCDM'
    return densityPercent(value)
}

function clamp01(value: number) {
    return Math.max(0, Math.min(1, value))
}

function mix(a: number, b: number, t: number) {
    return a + (b - a) * clamp01(t)
}

function fract(value: number) {
    return value - Math.floor(value)
}

onMounted(() => {
    resizeCanvas()
    window.addEventListener('resize', resizeCanvas)
    animationId = requestAnimationFrame(loop)
})

onUnmounted(() => {
    window.removeEventListener('resize', resizeCanvas)
    cancelAnimationFrame(animationId)
})
</script>

<style scoped>
.cosmo-shell {
    position: relative;
    height: 100vh;
    overflow: hidden;
    background: #05070c;
    color: #eef7f4;
}

.cosmo-canvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
}

.topbar {
    position: absolute;
    top: 14px;
    left: 14px;
    right: 14px;
    display: grid;
    grid-template-columns: minmax(120px, 220px) 1fr auto;
    gap: 14px;
    align-items: center;
    pointer-events: none;
}

.home-link,
.top-actions,
.control-panel,
.metrics-panel {
    pointer-events: auto;
}

.home-link,
.icon-button,
.era-grid button {
    border: 1px solid rgba(134, 162, 172, 0.36);
    background: rgba(10, 16, 24, 0.76);
    color: #edfdf9;
    backdrop-filter: blur(10px);
}

.home-link {
    width: fit-content;
    display: inline-flex;
    align-items: center;
    gap: 8px;
    min-height: 34px;
    border-radius: 8px;
    padding: 0 12px;
    font-size: 13px;
    font-weight: 800;
}

.title-wrap {
    min-width: 0;
    text-align: center;
    text-shadow: 0 1px 3px rgba(0, 0, 0, 0.8);
}

.title-row {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
}

.title-row h1 {
    margin: 0;
    font-size: 21px;
    line-height: 1.1;
    font-weight: 900;
}

.title-icon {
    color: #67e8f9;
    font-size: 24px;
}

.mode-pill {
    border-radius: 7px;
    padding: 3px 7px;
    border: 1px solid rgba(103, 232, 249, 0.42);
    color: #b9f6ff;
    background: rgba(19, 94, 105, 0.24);
    font-size: 11px;
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
}

.mtt-pill {
    border-color: rgba(111, 245, 190, 0.42);
    color: #c4ffe8;
    background: rgba(18, 92, 66, 0.24);
}

.title-wrap p {
    margin: 5px 0 0;
    color: rgba(226, 242, 239, 0.76);
    font-size: 13px;
}

.top-actions {
    display: flex;
    justify-content: flex-end;
    gap: 8px;
}

.icon-button {
    display: grid;
    place-items: center;
    width: 36px;
    height: 36px;
    border-radius: 8px;
    font-size: 18px;
}

.home-link:hover,
.icon-button:hover,
.era-grid button:hover {
    background: rgba(24, 38, 56, 0.92);
    border-color: rgba(111, 245, 190, 0.55);
}

.control-panel,
.metrics-panel,
.legend {
    border: 1px solid rgba(134, 162, 172, 0.28);
    background: rgba(7, 12, 19, 0.78);
    backdrop-filter: blur(12px);
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.26);
}

.control-panel {
    position: absolute;
    left: 14px;
    top: 68px;
    width: min(336px, calc(100vw - 28px));
    max-height: calc(100vh - 92px);
    overflow: auto;
    display: grid;
    gap: 10px;
}

.panel-section {
    border-radius: 8px;
    padding: 12px;
    border: 1px solid rgba(134, 162, 172, 0.24);
    background: rgba(9, 17, 27, 0.62);
}

.panel-section h2,
.metrics-panel h2 {
    margin: 0 0 10px;
    color: #e2fbf5;
    font-size: 12px;
    line-height: 1;
    text-transform: uppercase;
    font-weight: 900;
}

.era-grid {
    display: grid;
    grid-template-columns: minmax(0, 1fr);
    gap: 6px;
    max-height: 340px;
    overflow: auto;
}

.era-grid button {
    min-width: 0;
    min-height: 38px;
    border-radius: 7px;
    padding: 6px 8px;
    display: grid;
    grid-template-columns: 38px minmax(0, 1fr) 78px;
    gap: 6px;
    align-items: center;
    text-align: left;
}

.era-grid button span {
    display: grid;
    place-items: center;
    min-height: 26px;
    border-radius: 5px;
    color: #05120f;
    background: #67e8f9;
    font-size: 11px;
    font-weight: 900;
}

.era-grid button b {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    font-size: 11px;
}

.era-grid button small {
    color: rgba(255, 242, 196, 0.78);
    font-size: 10px;
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
    text-align: right;
}

.era-grid button.active {
    border-color: rgba(255, 220, 130, 0.78);
    background: rgba(88, 67, 28, 0.58);
}

label {
    display: grid;
    grid-template-columns: 72px minmax(0, 1fr) 58px;
    gap: 9px;
    align-items: center;
    min-height: 32px;
    color: rgba(236, 247, 244, 0.82);
    font-size: 12px;
}

label strong {
    text-align: right;
    color: #fff2c4;
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
    font-size: 12px;
}

input[type="range"] {
    width: 100%;
    accent-color: #67e8f9;
}

.checkbox-row {
    grid-template-columns: 18px 1fr;
    gap: 8px;
}

.time-readout {
    margin-top: 8px;
    display: flex;
    justify-content: space-between;
    gap: 12px;
    color: rgba(226, 242, 239, 0.82);
    font-size: 12px;
}

.time-readout b {
    color: #fff2c4;
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
}

.source-item {
    display: grid;
    grid-template-columns: 46px minmax(0, 1fr);
    gap: 8px;
    align-items: center;
    margin-top: 8px;
    color: rgba(226, 242, 239, 0.82);
}

.source-item > i {
    border-radius: 999px;
    padding: 4px 5px;
    text-align: center;
    font-size: 9px;
    line-height: 1;
    font-style: normal;
    font-weight: 900;
    text-transform: uppercase;
    color: #04110e;
    background: #94a3b8;
}

.source-item.native > i {
    background: #67e8f9;
}

.source-item.derived > i {
    background: #6ff5be;
}

.source-item.scaffold > i {
    background: #fde68a;
}

.source-item span {
    min-width: 0;
    display: grid;
    gap: 2px;
}

.source-item strong {
    color: #edfdf9;
    font-size: 11px;
    line-height: 1.1;
}

.source-item em {
    color: rgba(203, 219, 214, 0.64);
    font-size: 10px;
    line-height: 1.18;
    font-style: normal;
}

.metrics-panel {
    position: absolute;
    right: 14px;
    top: 72px;
    width: min(322px, calc(100vw - 28px));
    max-height: calc(100vh - 214px);
    overflow: auto;
    border-radius: 8px;
    padding: 12px;
    display: grid;
    gap: 12px;
}

.metrics-panel section {
    display: grid;
    gap: 5px;
}

.metrics-panel p {
    margin: 0;
    color: rgba(226, 242, 239, 0.78);
    font-size: 12px;
    line-height: 1.35;
}

.contents-list {
    display: grid;
    gap: 7px;
}

.contents-list div {
    display: grid;
    grid-template-columns: 72px minmax(0, 1fr);
    gap: 8px;
    color: rgba(226, 242, 239, 0.76);
    font-size: 11px;
    line-height: 1.22;
}

.contents-list strong {
    color: #fff2c4;
    font-size: 11px;
}

.metric-grid {
    display: grid;
    gap: 7px;
}

.metric {
    display: flex;
    justify-content: space-between;
    gap: 12px;
    font-size: 12px;
    color: rgba(226, 242, 239, 0.78);
}

.metric strong {
    color: #fff;
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
}

.legend {
    position: absolute;
    left: 50%;
    bottom: 14px;
    transform: translateX(-50%);
    display: flex;
    gap: 14px;
    border-radius: 999px;
    padding: 8px 12px;
    font-size: 12px;
    color: rgba(238, 247, 244, 0.8);
}

.legend span {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    white-space: nowrap;
}

.dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    border-radius: 50%;
}

.dot.radiation {
    background: #ffd36d;
}

.dot.matter {
    background: #6ff5be;
}

.dot.solar {
    background: #fde68a;
}

.dot.galaxy {
    background: #67e8f9;
}

.dot.cluster {
    background: #b88aff;
}

.dot.record {
    background: #ffffff;
}

.dot.horizon {
    background: #ff9f6e;
}

@media (max-width: 920px) {
    .topbar {
        left: 10px;
        right: 10px;
        grid-template-columns: minmax(0, 1fr) auto;
    }

    .title-wrap {
        display: none;
    }

    .control-panel {
        left: 10px;
        top: auto;
        bottom: 52px;
        max-height: 48vh;
        width: calc(100vw - 20px);
    }

    .metrics-panel {
        top: 62px;
        right: 10px;
        width: min(260px, calc(100vw - 20px));
        max-height: 34vh;
    }

    .legend {
        display: none;
    }
}
</style>
