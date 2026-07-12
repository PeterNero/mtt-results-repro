<template>
    <section class="proto-lab">
        <header class="lab-topbar">
            <NuxtLink to="/" class="icon-link" title="Back to simulations" aria-label="Back to simulations">
                <span class="i-tabler-arrow-left"></span>
            </NuxtLink>
            <div class="title-block">
                <p>MTT visualizer</p>
                <h1>Proto-Spinor Process</h1>
            </div>
            <div class="topbar-actions">
                <button class="icon-button" type="button" :title="isRunning ? 'Pause' : 'Run'" @click="isRunning = !isRunning">
                    <span :class="isRunning ? 'i-tabler-player-pause' : 'i-tabler-player-play'"></span>
                </button>
                <button class="icon-button" type="button" title="Reset" @click="resetState">
                    <span class="i-tabler-refresh"></span>
                </button>
            </div>
        </header>

        <main class="lab-board">
            <section class="stage-card double-cover-card">
                <div class="card-heading">
                    <span class="heading-dot circle-dot"></span>
                    <div>
                        <p>internal carrier</p>
                        <h2>two-circle closure clock</h2>
                    </div>
                </div>

                <svg class="double-cover-svg" viewBox="0 0 760 420" role="img" aria-label="Two-circle proto-spinor closure clock">
                    <defs>
                        <linearGradient id="proto-plane" x1="0" y1="0" x2="1" y2="1">
                            <stop offset="0" stop-color="#27231e" />
                            <stop offset="1" stop-color="#11100f" />
                        </linearGradient>
                        <linearGradient id="nil-band" x1="0" y1="1" x2="0" y2="0">
                            <stop offset="0" stop-color="rgba(106, 220, 133, 0.18)" />
                            <stop offset="1" stop-color="rgba(106, 220, 133, 0.82)" />
                        </linearGradient>
                        <filter id="soft-glow">
                            <feGaussianBlur stdDeviation="7" result="coloredBlur" />
                            <feMerge>
                                <feMergeNode in="coloredBlur" />
                                <feMergeNode in="SourceGraphic" />
                            </feMerge>
                        </filter>
                    </defs>

                    <rect x="22" y="42" width="716" height="318" rx="18" fill="url(#proto-plane)" />
                    <path
                        v-for="line in planeGrid"
                        :key="line"
                        :d="`M 58 ${line} C 220 ${line - 28}, 540 ${line + 28}, 702 ${line}`"
                        fill="none"
                        stroke="rgba(244, 236, 220, 0.08)"
                        stroke-width="1.2"
                    />

                    <g transform="translate(216 206)">
                        <circle r="106" fill="rgba(83, 197, 255, 0.04)" stroke="rgba(83, 197, 255, 0.42)" stroke-width="3" />
                        <path :d="loopArcPath(106, firstLoopArc)" fill="none" stroke="#53c5ff" stroke-width="10" stroke-linecap="round" />
                        <circle :cx="firstDot.x" :cy="firstDot.y" r="13" fill="#53c5ff" filter="url(#soft-glow)" />
                        <text x="0" y="146" text-anchor="middle" class="svg-label">circle 1: open nil</text>
                    </g>

                    <g transform="translate(544 206)">
                        <circle r="106" fill="rgba(255, 139, 184, 0.04)" stroke="rgba(255, 139, 184, 0.42)" stroke-width="3" />
                        <path :d="loopArcPath(106, secondLoopArc)" fill="none" stroke="#ff8bb8" stroke-width="10" stroke-linecap="round" />
                        <circle :cx="secondDot.x" :cy="secondDot.y" r="13" fill="#ff8bb8" filter="url(#soft-glow)" />
                        <text x="0" y="146" text-anchor="middle" class="svg-label">circle 2: return closure</text>
                    </g>

                    <path d="M 331 206 C 370 174, 390 174, 429 206" fill="none" stroke="rgba(244, 236, 220, 0.3)" stroke-width="2" stroke-dasharray="7 8" />
                    <path d="M 424 196 L 441 206 L 424 216" fill="none" stroke="rgba(244, 236, 220, 0.48)" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" />

                    <g class="nil-lift" transform="translate(380 320)">
                        <line x1="-252" y1="0" x2="252" y2="0" stroke="rgba(244, 236, 220, 0.28)" stroke-width="2" />
                        <path :d="nilEnvelopePath" fill="url(#nil-band)" stroke="#6adc85" stroke-width="3" />
                        <line x1="0" y1="0" :y2="-nilHeight" stroke="#6adc85" stroke-width="5" stroke-linecap="round" />
                        <circle cx="0" :cy="-nilHeight" r="10" fill="#6adc85" filter="url(#soft-glow)" />
                        <text x="0" y="34" text-anchor="middle" class="svg-label">nil gap height</text>
                        <text x="0" :y="-Math.max(22, nilHeight + 18)" text-anchor="middle" class="svg-value">{{ displayPercent(nilGap) }}</text>
                    </g>

                    <g class="twist-mini" transform="translate(380 92)">
                        <path :d="lensRibbonUpper" fill="none" stroke="#f5c84c" stroke-width="8" stroke-linecap="round" />
                        <path :d="lensRibbonLower" fill="none" stroke="#9d7cff" stroke-width="5" stroke-linecap="round" />
                        <line
                            v-for="link in twistLinks"
                            :key="link.x"
                            :x1="link.x"
                            :y1="link.y1"
                            :x2="link.x"
                            :y2="link.y2"
                            stroke="rgba(245, 200, 76, 0.45)"
                            stroke-width="2"
                        />
                        <text x="0" y="-32" text-anchor="middle" class="svg-label">lens transport twist</text>
                    </g>
                </svg>
            </section>

            <section class="stage-card lanes-card">
                <div class="card-heading">
                    <span class="heading-dot lens-dot"></span>
                    <div>
                        <p>carrier decomposition</p>
                        <h2>circle, lens, nil</h2>
                    </div>
                </div>

                <div class="lane-list">
                    <article class="process-lane">
                        <div class="lane-title">
                            <span class="i-tabler-refresh-dot"></span>
                            <strong>C</strong>
                            <em>return bookkeeping</em>
                        </div>
                        <div class="two-turn-meter">
                            <div class="meter-track">
                                <i :style="{ width: `${twoTurnPercent}%` }"></i>
                            </div>
                            <div class="meter-stops">
                                <span>0</span>
                                <span>1 circle</span>
                                <span>2 circles</span>
                            </div>
                        </div>
                    </article>

                    <article class="process-lane">
                        <div class="lane-title">
                            <span class="i-tabler-route"></span>
                            <strong>L</strong>
                            <em>redundancy and transport twist</em>
                        </div>
                        <div class="phase-row">
                            <div class="phase-disc" :style="{ '--phase': `${lensDegrees}deg` }">
                                <i></i>
                            </div>
                            <div class="mini-readout">
                                <span>lens error</span>
                                <strong>{{ lensError.toFixed(2) }}</strong>
                            </div>
                        </div>
                    </article>

                    <article class="process-lane">
                        <div class="lane-title">
                            <span class="i-tabler-filter-check"></span>
                            <strong>N</strong>
                            <em>survivor gap and nil selection</em>
                        </div>
                        <div class="gap-bar">
                            <i :style="{ height: `${displayPercentNumber(nilGap)}%` }"></i>
                            <b :style="{ bottom: `${displayPercentNumber(nilCapacity)}%` }"></b>
                        </div>
                        <div class="meter-stops">
                            <span>closed</span>
                            <span>current {{ displayPercent(nilGap) }}</span>
                            <span>capacity {{ displayPercent(nilCapacity) }}</span>
                        </div>
                    </article>
                </div>
            </section>

            <section class="stage-card outcome-card">
                <div class="card-heading">
                    <span class="heading-dot outcome-dot"></span>
                    <div>
                        <p>projection output</p>
                        <h2>stationary sampled anchor</h2>
                    </div>
                </div>

                <div class="outcome-grid">
                    <div class="anchor-stage">
                        <div class="anchor-rings" :class="{ pulse: tickPulse > 0.18 }">
                            <span class="ring r1"></span>
                            <span class="ring r2"></span>
                            <span class="anchor-core" :style="{ opacity: 0.32 + sampledOutcome * 0.68 }"></span>
                        </div>
                        <div class="tick-caption">sampled only at two-circle tick</div>
                    </div>

                    <div class="gravity-stage">
                        <svg viewBox="0 0 360 210" role="img" aria-label="Elastic GR plane response">
                            <path
                                v-for="row in gravityRows"
                                :key="row"
                                :d="gravityPath(row)"
                                fill="none"
                                stroke="rgba(130, 158, 255, 0.28)"
                                stroke-width="2"
                            />
                            <path :d="gravitySurfacePath" fill="none" stroke="#829eff" stroke-width="4" stroke-linecap="round" />
                            <line x1="180" y1="28" x2="180" :y2="96 + planeDrop" stroke="#f5c84c" stroke-width="5" stroke-linecap="round" />
                            <circle cx="180" :cy="100 + planeDrop" :r="10 + sampledOutcome * 8" fill="#f5c84c" filter="url(#soft-glow)" />
                            <text x="180" y="188" text-anchor="middle" class="svg-label">elastic relaxation after pressure</text>
                        </svg>
                    </div>
                </div>
            </section>

            <section class="stage-card basis-card">
                <div class="card-heading">
                    <span class="heading-dot basis-dot"></span>
                    <div>
                        <p>research basis</p>
                        <h2>what this view encodes</h2>
                    </div>
                </div>
                <div class="basis-list">
                    <div v-for="item in basisItems" :key="item.term">
                        <strong>{{ item.term }}</strong>
                        <span>{{ item.detail }}</span>
                    </div>
                </div>
            </section>
        </main>

        <aside class="control-panel">
            <label class="preset-select">
                <span>Preset</span>
                <select v-model="selectedPresetKey">
                    <option v-for="preset in presets" :key="preset.key" :value="preset.key">
                        {{ preset.label }}
                    </option>
                </select>
            </label>

            <div class="segmented" aria-label="View mode">
                <button
                    v-for="option in modeOptions"
                    :key="option.value"
                    type="button"
                    :class="{ active: mode === option.value }"
                    @click="mode = option.value"
                >
                    {{ option.label }}
                </button>
            </div>

            <div class="slider-stack">
                <label v-for="control in controls" :key="control.key">
                    <span>
                        {{ control.label }}
                        <strong>{{ params[control.key].toFixed(2) }}</strong>
                    </span>
                    <input
                        v-model.number="params[control.key]"
                        type="range"
                        :min="control.min"
                        :max="control.max"
                        :step="control.step"
                    >
                </label>
            </div>
        </aside>

        <aside class="readout-panel">
            <div class="readout-grid">
                <div>
                    <span>turn</span>
                    <strong>{{ currentTurnLabel }}</strong>
                </div>
                <div>
                    <span>nil gap</span>
                    <strong>{{ nilGap.toFixed(2) }}</strong>
                </div>
                <div>
                    <span>lens error</span>
                    <strong>{{ lensError.toFixed(2) }}</strong>
                </div>
                <div>
                    <span>closure cost</span>
                    <strong>{{ closureCost.toFixed(2) }}</strong>
                </div>
                <div>
                    <span>history</span>
                    <strong>{{ loopHistory.toFixed(2) }}</strong>
                </div>
                <div>
                    <span>pressure</span>
                    <strong>{{ planePressure.toFixed(2) }}</strong>
                </div>
                <div>
                    <span>inertia</span>
                    <strong>{{ inertiaBaseline.toFixed(2) }}</strong>
                </div>
                <div>
                    <span>sample</span>
                    <strong>{{ sampledOutcome.toFixed(2) }}</strong>
                </div>
            </div>
        </aside>
    </section>
</template>

<script setup lang="ts">
type ProjectionMode = 'overview' | 'inner' | 'outcome'
type PresetKey = 'carrier' | 'photon' | 'neutrino' | 'electron' | 'quark' | 'majorana'
type ParamKey = 'nilCapacity' | 'lensCurvature' | 'returnStrength' | 'anchorStrength' | 'elasticity' | 'speed'

type Preset = {
    key: PresetKey
    label: string
    theta: number
    lensPhase: number
    params: Record<ParamKey, number>
}

const TAU = Math.PI * 2
const isRunning = ref(true)
const selectedPresetKey = ref<PresetKey>('carrier')
const mode = ref<ProjectionMode>('overview')

const params = reactive<Record<ParamKey, number>>({
    nilCapacity: 0.62,
    lensCurvature: 0.64,
    returnStrength: 0.72,
    anchorStrength: 0.62,
    elasticity: 0.58,
    speed: 0.62,
})

const state = reactive({
    thetaTotal: 0,
    lensPhase: 0,
    loopHistory: 0,
    loopPeak: 0,
    planePressure: 0,
    inertiaBaseline: 0,
    sampledOutcome: 0,
    tickPulse: 0,
})

const presets: Preset[] = [
    {
        key: 'carrier',
        label: 'Proto-spinor carrier',
        theta: 0,
        lensPhase: 0.26,
        params: {
            nilCapacity: 0.62,
            lensCurvature: 0.64,
            returnStrength: 0.72,
            anchorStrength: 0.62,
            elasticity: 0.58,
            speed: 0.62,
        },
    },
    {
        key: 'photon',
        label: 'Photon / null transport',
        theta: 0.18,
        lensPhase: 0.18,
        params: {
            nilCapacity: 0.16,
            lensCurvature: 0.18,
            returnStrength: 0.95,
            anchorStrength: 0.2,
            elasticity: 0.86,
            speed: 0.92,
        },
    },
    {
        key: 'neutrino',
        label: 'Neutrino / co-aligned',
        theta: 0.4,
        lensPhase: 0.42,
        params: {
            nilCapacity: 0.34,
            lensCurvature: 0.26,
            returnStrength: 0.9,
            anchorStrength: 0.36,
            elasticity: 0.78,
            speed: 0.64,
        },
    },
    {
        key: 'electron',
        label: 'Charged lepton / anchored',
        theta: 0.08,
        lensPhase: 0.64,
        params: {
            nilCapacity: 0.82,
            lensCurvature: 0.86,
            returnStrength: 0.74,
            anchorStrength: 0.9,
            elasticity: 0.48,
            speed: 0.52,
        },
    },
    {
        key: 'quark',
        label: 'Quark / partial anchor',
        theta: 0.2,
        lensPhase: 1.18,
        params: {
            nilCapacity: 0.7,
            lensCurvature: 1,
            returnStrength: 0.44,
            anchorStrength: 0.66,
            elasticity: 0.5,
            speed: 0.58,
        },
    },
    {
        key: 'majorana',
        label: 'Majorana / nil identified',
        theta: 0.52,
        lensPhase: 0.52,
        params: {
            nilCapacity: 0.5,
            lensCurvature: 0.24,
            returnStrength: 1,
            anchorStrength: 0.52,
            elasticity: 0.72,
            speed: 0.52,
        },
    },
]

const modeOptions: Array<{ label: string, value: ProjectionMode }> = [
    { label: 'Overview', value: 'overview' },
    { label: 'Inner', value: 'inner' },
    { label: 'Outcome', value: 'outcome' },
]

const controls: Array<{ key: ParamKey, label: string, min: number, max: number, step: number }> = [
    { key: 'nilCapacity', label: 'nil capacity', min: 0.05, max: 1, step: 0.01 },
    { key: 'lensCurvature', label: 'lens twist', min: 0, max: 1.2, step: 0.01 },
    { key: 'returnStrength', label: 'second return', min: 0, max: 1, step: 0.01 },
    { key: 'anchorStrength', label: 'anchor strength', min: 0, max: 1, step: 0.01 },
    { key: 'elasticity', label: 'GR elasticity', min: 0.1, max: 1, step: 0.01 },
    { key: 'speed', label: 'clock speed', min: 0, max: 1.4, step: 0.01 },
]

const basisItems = [
    {
        term: 'Pointwise internal world',
        detail: 'Each proto-point carries an internal carrier before spacetime encoding.',
    },
    {
        term: 'Double cover',
        detail: 'Neutrality closes only after two internal loops, giving proto-spinorial behavior.',
    },
    {
        term: 'C, L, N',
        detail: 'Circle tracks return, lens tracks transport redundancy, nil tracks survivor selection.',
    },
    {
        term: 'Gravity and inertia',
        detail: 'Residual closure bookkeeping becomes elastic pressure and coherent identity cost.',
    },
]

const planeGrid = [96, 136, 176, 216, 256, 296]
const gravityRows = [-46, -23, 0, 23, 46]
let animationId = 0
let lastTime = 0
let lastTickIndex = 0

const twoTurnPhase = computed(() => mod(state.thetaTotal, TAU * 2) / (TAU * 2))
const circleProgress = computed(() => twoTurnPhase.value * 2)
const firstProgress = computed(() => clamp(circleProgress.value))
const secondProgress = computed(() => clamp(circleProgress.value - 1))
const currentTurnLabel = computed(() => circleProgress.value < 1 ? '1 / 2' : '2 / 2')
const twoTurnPercent = computed(() => twoTurnPhase.value * 100)
const firstLoopArc = computed(() => circleProgress.value < 1 ? firstProgress.value : 1)
const secondLoopArc = computed(() => circleProgress.value < 1 ? 0 : secondProgress.value)
const nilCapacity = computed(() => params.nilCapacity)
const nilGap = computed(() => {
    const open = smoothstep(firstProgress.value)
    const close = smoothstep(secondProgress.value) * params.returnStrength
    return clamp(nilCapacity.value * (circleProgress.value <= 1 ? open : 1 - close))
})
const lensError = computed(() => {
    const returnCorrection = secondProgress.value * params.returnStrength * 0.38
    return clamp(Math.abs(Math.sin((state.lensPhase - state.thetaTotal * 0.5) * params.lensCurvature)) * (1 - returnCorrection))
})
const loopPerfectionError = computed(() => Math.abs(Math.sin(Math.PI * twoTurnPhase.value)))
const closureCost = computed(() => clamp(nilGap.value * 0.46 + lensError.value * 0.34 + loopPerfectionError.value * 0.2))
const anchoredCost = computed(() => clamp(closureCost.value * params.anchorStrength))
const lensDegrees = computed(() => (state.lensPhase / TAU) * 360)
const nilHeight = computed(() => 100 * nilGap.value)
const tickPulse = computed(() => state.tickPulse)
const planePressure = computed(() => state.planePressure)
const inertiaBaseline = computed(() => state.inertiaBaseline)
const sampledOutcome = computed(() => state.sampledOutcome)
const loopHistory = computed(() => state.loopHistory)
const planeDrop = computed(() => 56 * planePressure.value)
const firstDot = computed(() => polarPoint(106, Math.max(0.001, firstLoopArc.value) * TAU - Math.PI / 2))
const secondDot = computed(() => polarPoint(106, Math.max(0.001, secondLoopArc.value) * TAU - Math.PI / 2))
const nilEnvelopePath = computed(() => {
    const h = nilHeight.value
    return `M -246 0 C -166 ${-h * 0.18}, -82 ${-h}, 0 ${-h} C 82 ${-h}, 166 ${-h * 0.18}, 246 0 L 246 0 L -246 0 Z`
})
const lensRibbonUpper = computed(() => ribbonPath(1))
const lensRibbonLower = computed(() => ribbonPath(-1))
const twistLinks = computed(() => {
    const links: Array<{ x: number, y1: number, y2: number }> = []
    for (let index = -4; index <= 4; index += 1) {
        const x = index * 34
        const wave = Math.sin(index * 0.82 + state.lensPhase) * 20 * params.lensCurvature
        links.push({ x, y1: -wave, y2: wave })
    }
    return links
})
const gravitySurfacePath = computed(() => gravityPath(0))

watch(() => selectedPresetKey.value, applyPreset)

function applyPreset(key: PresetKey) {
    const preset = presets.find((item) => item.key === key) ?? presets[0]
    selectedPresetKey.value = preset.key
    Object.assign(params, preset.params)
    state.thetaTotal = preset.theta * TAU
    state.lensPhase = preset.lensPhase * TAU
    state.loopHistory = 0
    state.loopPeak = 0
    state.planePressure = 0
    state.inertiaBaseline = 0
    state.sampledOutcome = 0
    state.tickPulse = 0
    lastTickIndex = Math.floor(state.thetaTotal / (TAU * 2))
}

function resetState() {
    applyPreset(selectedPresetKey.value)
}

function mod(value: number, base: number) {
    return ((value % base) + base) % base
}

function clamp(value: number, min = 0, max = 1) {
    return Math.max(min, Math.min(max, value))
}

function smoothstep(value: number) {
    const x = clamp(value)
    return x * x * (3 - 2 * x)
}

function polarPoint(radius: number, angle: number) {
    return {
        x: Math.cos(angle) * radius,
        y: Math.sin(angle) * radius,
    }
}

function loopArcPath(radius: number, progress: number) {
    const p = clamp(progress)
    if (p <= 0) {
        return ''
    }
    const start = -Math.PI / 2
    const end = start + p * TAU
    const startPoint = polarPoint(radius, start)
    const endPoint = polarPoint(radius, end)
    const largeArc = p > 0.5 ? 1 : 0
    return `M ${startPoint.x.toFixed(2)} ${startPoint.y.toFixed(2)} A ${radius} ${radius} 0 ${largeArc} 1 ${endPoint.x.toFixed(2)} ${endPoint.y.toFixed(2)}`
}

function ribbonPath(strand: 1 | -1) {
    const points: string[] = []
    for (let i = 0; i <= 80; i += 1) {
        const t = i / 80
        const x = -168 + t * 336
        const envelope = Math.sin(t * Math.PI)
        const y = Math.sin(t * Math.PI * 4 + state.lensPhase) * 22 * params.lensCurvature * strand * envelope
        points.push(`${i === 0 ? 'M' : 'L'} ${x.toFixed(1)} ${y.toFixed(1)}`)
    }
    return points.join(' ')
}

function gravityPath(row: number) {
    const drop = planeDrop.value
    const y = 106 + row
    const left = 18
    const right = 342
    const depth = drop * (1 - Math.min(0.75, Math.abs(row) / 70))
    return `M ${left} ${y} C 104 ${y - 10}, 132 ${y + depth}, 180 ${y + depth} C 228 ${y + depth}, 256 ${y - 10}, ${right} ${y}`
}

function displayPercent(value: number) {
    return `${Math.round(clamp(value) * 100)}%`
}

function displayPercentNumber(value: number) {
    return Math.round(clamp(value) * 100)
}

function update(delta: number) {
    const previousTheta = state.thetaTotal
    const previousTick = lastTickIndex
    if (isRunning.value && params.speed > 0) {
        const step = delta * 0.001 * params.speed
        state.thetaTotal += step * TAU * 0.16
        state.lensPhase += step * (0.28 + params.lensCurvature * 0.22)
    }

    const advance = clamp(Math.abs(state.thetaTotal - previousTheta) / (TAU * 2), 0, 0.08)
    const divergence = closureCost.value
    state.loopHistory = clamp(state.loopHistory + divergence * advance * 2.2)
    state.loopPeak = Math.max(state.loopPeak, divergence)

    const tickIndex = Math.floor(state.thetaTotal / (TAU * 2))
    if (tickIndex > previousTick) {
        const sampledPressure = clamp((state.loopHistory * 0.64 + state.loopPeak * 0.36) * (0.46 + (1 - params.elasticity) * 0.42))
        state.planePressure = sampledPressure
        state.sampledOutcome = clamp(anchoredCost.value * (0.42 + sampledPressure * 0.58))
        state.inertiaBaseline = clamp(state.inertiaBaseline + sampledPressure * (0.2 + params.anchorStrength * 0.42))
        state.tickPulse = 1
        state.loopHistory = divergence * 0.04
        state.loopPeak = divergence
    }
    lastTickIndex = tickIndex

    const relax = delta * 0.001 * (0.16 + params.elasticity * 0.62)
    state.planePressure = Math.max(0, state.planePressure - relax * 0.72)
    state.inertiaBaseline = Math.max(0, state.inertiaBaseline - relax * 0.12)
    state.tickPulse = Math.max(0, state.tickPulse - relax * 2.2)
}

function frame(time: number) {
    const delta = lastTime ? Math.min(48, time - lastTime) : 16
    lastTime = time
    update(delta)
    animationId = window.requestAnimationFrame(frame)
}

onMounted(() => {
    applyPreset(selectedPresetKey.value)
    animationId = window.requestAnimationFrame(frame)
})

onUnmounted(() => {
    window.cancelAnimationFrame(animationId)
})
</script>

<style scoped lang="scss">
.proto-lab {
    position: relative;
    min-height: 100vh;
    overflow: hidden;
    color: #f4ecdc;
    background:
        radial-gradient(circle at 18% 16%, rgba(83, 197, 255, 0.14), transparent 34%),
        radial-gradient(circle at 82% 18%, rgba(245, 200, 76, 0.11), transparent 30%),
        linear-gradient(135deg, #11100f 0%, #17130f 48%, #0f1114 100%);
}

.lab-topbar,
.control-panel,
.readout-panel,
.stage-card {
    border: 1px solid rgba(244, 236, 220, 0.13);
    border-radius: 8px;
    background: rgba(18, 17, 16, 0.78);
    box-shadow: 0 18px 42px rgba(0, 0, 0, 0.34);
    backdrop-filter: blur(18px);
}

.lab-topbar {
    position: absolute;
    z-index: 4;
    top: 18px;
    left: 18px;
    right: 18px;
    display: grid;
    grid-template-columns: 42px minmax(0, 1fr) auto;
    gap: 14px;
    align-items: center;
    min-height: 64px;
    padding: 10px 12px;
}

.title-block {
    min-width: 0;

    p {
        margin: 0;
        color: rgba(244, 236, 220, 0.56);
        font-size: 0.72rem;
        font-weight: 750;
        letter-spacing: 0;
        text-transform: uppercase;
    }

    h1 {
        margin: 2px 0 0;
        overflow: hidden;
        color: #f4ecdc;
        font-size: clamp(1.15rem, 2.1vw, 1.75rem);
        font-weight: 850;
        line-height: 1.05;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
}

.topbar-actions {
    display: flex;
    gap: 8px;
}

.icon-link,
.icon-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    width: 42px;
    height: 42px;
    border: 1px solid rgba(244, 236, 220, 0.14);
    border-radius: 8px;
    color: #f4ecdc;
    background: rgba(244, 236, 220, 0.08);
    transition: background 140ms ease, border-color 140ms ease, transform 140ms ease;

    span {
        font-size: 1.25rem;
    }

    &:hover {
        border-color: rgba(83, 197, 255, 0.48);
        background: rgba(83, 197, 255, 0.14);
        transform: translateY(-1px);
    }
}

.lab-board {
    position: relative;
    z-index: 1;
    display: grid;
    grid-template-columns: minmax(420px, 1.5fr) minmax(320px, 0.8fr);
    grid-template-rows: minmax(390px, 1fr) minmax(245px, 0.64fr);
    gap: 14px;
    width: min(1440px, calc(100vw - 420px));
    min-height: calc(100vh - 120px);
    padding: 104px 18px 18px;
}

.stage-card {
    min-width: 0;
    min-height: 0;
    padding: 16px;
}

.double-cover-card {
    display: grid;
    grid-template-rows: auto minmax(0, 1fr);
}

.lanes-card,
.outcome-card,
.basis-card {
    display: grid;
    gap: 14px;
    align-content: start;
}

.card-heading {
    display: flex;
    gap: 10px;
    align-items: center;
    min-width: 0;

    p,
    h2 {
        margin: 0;
    }

    p {
        color: rgba(244, 236, 220, 0.52);
        font-size: 0.7rem;
        font-weight: 800;
        text-transform: uppercase;
    }

    h2 {
        color: #f4ecdc;
        font-size: 1rem;
        font-weight: 850;
    }
}

.heading-dot {
    width: 13px;
    height: 13px;
    border-radius: 50%;
    box-shadow: 0 0 20px currentColor;
}

.circle-dot {
    color: #53c5ff;
    background: #53c5ff;
}

.lens-dot {
    color: #f5c84c;
    background: #f5c84c;
}

.outcome-dot {
    color: #ff8bb8;
    background: #ff8bb8;
}

.basis-dot {
    color: #6adc85;
    background: #6adc85;
}

.double-cover-svg {
    width: 100%;
    height: 100%;
    min-height: 330px;
}

.svg-label {
    fill: rgba(244, 236, 220, 0.66);
    font: 700 18px Inter, ui-sans-serif, system-ui, sans-serif;
}

.svg-value {
    fill: #6adc85;
    font: 850 20px Inter, ui-sans-serif, system-ui, sans-serif;
}

.lane-list {
    display: grid;
    gap: 12px;
}

.process-lane {
    display: grid;
    gap: 10px;
    min-height: 114px;
    padding: 12px;
    border: 1px solid rgba(244, 236, 220, 0.1);
    border-radius: 8px;
    background: rgba(244, 236, 220, 0.045);
}

.lane-title {
    display: grid;
    grid-template-columns: 28px 32px minmax(0, 1fr);
    gap: 8px;
    align-items: center;

    span {
        color: rgba(244, 236, 220, 0.68);
        font-size: 1.25rem;
    }

    strong {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        height: 28px;
        border-radius: 50%;
        color: #11100f;
        background: #f4ecdc;
        font-size: 0.92rem;
        font-weight: 900;
    }

    em {
        overflow: hidden;
        color: rgba(244, 236, 220, 0.78);
        font-size: 0.82rem;
        font-style: normal;
        font-weight: 750;
        text-overflow: ellipsis;
        white-space: nowrap;
    }
}

.two-turn-meter {
    display: grid;
    gap: 8px;
}

.meter-track {
    height: 16px;
    overflow: hidden;
    border: 1px solid rgba(244, 236, 220, 0.12);
    border-radius: 999px;
    background: rgba(244, 236, 220, 0.08);

    i {
        display: block;
        height: 100%;
        border-radius: inherit;
        background: linear-gradient(90deg, #53c5ff 0%, #53c5ff 49%, #ff8bb8 51%, #ff8bb8 100%);
        transition: width 90ms linear;
    }
}

.meter-stops {
    display: flex;
    justify-content: space-between;
    color: rgba(244, 236, 220, 0.52);
    font-size: 0.68rem;
    font-weight: 700;
}

.phase-row {
    display: grid;
    grid-template-columns: 82px minmax(0, 1fr);
    gap: 12px;
    align-items: center;
}

.phase-disc {
    position: relative;
    width: 70px;
    height: 70px;
    border: 1px solid rgba(245, 200, 76, 0.35);
    border-radius: 50%;
    background: radial-gradient(circle, rgba(245, 200, 76, 0.1), rgba(244, 236, 220, 0.02));

    i {
        position: absolute;
        top: 50%;
        left: 50%;
        width: 30px;
        height: 4px;
        border-radius: 999px;
        background: #f5c84c;
        transform: translateY(-50%) rotate(var(--phase));
        transform-origin: 0 50%;
        box-shadow: 0 0 16px rgba(245, 200, 76, 0.58);
    }
}

.mini-readout {
    display: grid;
    gap: 4px;

    span {
        color: rgba(244, 236, 220, 0.52);
        font-size: 0.7rem;
        font-weight: 800;
        text-transform: uppercase;
    }

    strong {
        color: #f4ecdc;
        font-size: 1.4rem;
        font-weight: 900;
        font-variant-numeric: tabular-nums;
    }
}

.gap-bar {
    position: relative;
    width: 100%;
    height: 56px;
    border: 1px solid rgba(106, 220, 133, 0.2);
    border-radius: 8px;
    background: linear-gradient(180deg, rgba(106, 220, 133, 0.1), rgba(106, 220, 133, 0.02));

    i {
        position: absolute;
        right: 0;
        bottom: 0;
        left: 0;
        border-radius: 0 0 7px 7px;
        background: linear-gradient(180deg, rgba(106, 220, 133, 0.82), rgba(106, 220, 133, 0.24));
        transition: height 90ms linear;
    }

    b {
        position: absolute;
        right: 0;
        left: 0;
        height: 2px;
        background: #f5c84c;
        box-shadow: 0 0 12px rgba(245, 200, 76, 0.58);
    }
}

.outcome-grid {
    display: grid;
    grid-template-columns: minmax(190px, 0.8fr) minmax(230px, 1fr);
    gap: 14px;
    align-items: stretch;
}

.anchor-stage,
.gravity-stage {
    min-height: 210px;
    border: 1px solid rgba(244, 236, 220, 0.1);
    border-radius: 8px;
    background: rgba(244, 236, 220, 0.04);
}

.anchor-stage {
    display: grid;
    grid-template-rows: minmax(142px, 1fr) auto;
    place-items: center;
    padding: 14px;
}

.anchor-rings {
    position: relative;
    width: 142px;
    height: 142px;

    span {
        position: absolute;
        border-radius: 50%;
    }

    &.pulse .r2 {
        animation: pulse-ring 520ms ease-out;
    }
}

.ring {
    inset: 0;
    border: 1px solid rgba(255, 139, 184, 0.36);
}

.r1 {
    inset: 26px;
    border-color: rgba(83, 197, 255, 0.42);
}

.anchor-core {
    inset: 50px;
    background: #f4ecdc;
    box-shadow: 0 0 28px rgba(255, 139, 184, 0.72);
}

.tick-caption {
    color: rgba(244, 236, 220, 0.58);
    font-size: 0.74rem;
    font-weight: 750;
    text-align: center;
    text-transform: uppercase;
}

.gravity-stage {
    padding: 8px;

    svg {
        width: 100%;
        height: 100%;
    }
}

.basis-list {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 10px;

    div {
        min-height: 88px;
        padding: 12px;
        border: 1px solid rgba(244, 236, 220, 0.1);
        border-radius: 8px;
        background: rgba(244, 236, 220, 0.045);
    }

    strong,
    span {
        display: block;
    }

    strong {
        color: #f4ecdc;
        font-size: 0.82rem;
        font-weight: 850;
    }

    span {
        margin-top: 6px;
        color: rgba(244, 236, 220, 0.62);
        font-size: 0.76rem;
        font-weight: 620;
        line-height: 1.35;
    }
}

.control-panel,
.readout-panel {
    position: absolute;
    z-index: 4;
    right: 18px;
    width: 360px;
    padding: 14px;
}

.control-panel {
    top: 104px;
}

.readout-panel {
    bottom: 18px;
}

.preset-select {
    display: grid;
    gap: 6px;
    margin-bottom: 10px;

    span {
        color: rgba(244, 236, 220, 0.58);
        font-size: 0.72rem;
        font-weight: 800;
        text-transform: uppercase;
    }

    select {
        width: 100%;
        min-height: 38px;
        padding: 0 10px;
        border: 1px solid rgba(244, 236, 220, 0.14);
        border-radius: 8px;
        color: #f4ecdc;
        background: rgba(244, 236, 220, 0.08);
        font-size: 0.84rem;
        font-weight: 760;
        outline: none;
    }

    option {
        color: #11100f;
    }
}

.segmented {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 4px;
    padding: 4px;
    border: 1px solid rgba(244, 236, 220, 0.1);
    border-radius: 8px;
    background: rgba(244, 236, 220, 0.06);

    button {
        min-height: 34px;
        border-radius: 6px;
        color: rgba(244, 236, 220, 0.72);
        font-size: 0.78rem;
        font-weight: 750;
        transition: color 140ms ease, background 140ms ease;

        &.active {
            color: #11100f;
            background: #f5c84c;
        }
    }
}

.slider-stack {
    display: grid;
    gap: 9px;
    margin-top: 14px;

    label {
        display: grid;
        gap: 5px;
    }

    span {
        display: flex;
        justify-content: space-between;
        color: rgba(244, 236, 220, 0.66);
        font-size: 0.76rem;
        font-weight: 690;
    }

    strong {
        color: #f4ecdc;
        font-variant-numeric: tabular-nums;
    }

    input {
        width: 100%;
        accent-color: #53c5ff;
    }
}

.readout-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 8px;

    div {
        min-height: 48px;
        padding: 7px 9px;
        border: 1px solid rgba(244, 236, 220, 0.1);
        border-radius: 8px;
        background: rgba(244, 236, 220, 0.05);
    }

    span,
    strong {
        display: block;
    }

    span {
        color: rgba(244, 236, 220, 0.52);
        font-size: 0.68rem;
        font-weight: 800;
        text-transform: uppercase;
    }

    strong {
        margin-top: 2px;
        color: #f4ecdc;
        font-size: 0.94rem;
        font-weight: 870;
        font-variant-numeric: tabular-nums;
    }
}

@keyframes pulse-ring {
    0% {
        opacity: 1;
        transform: scale(0.8);
    }

    100% {
        opacity: 0.2;
        transform: scale(1.18);
    }
}

@media (max-width: 1180px) {
    .proto-lab {
        overflow: auto;
    }

    .lab-board {
        grid-template-columns: 1fr;
        grid-template-rows: auto;
        width: auto;
        padding-right: 18px;
        padding-bottom: 520px;
    }

    .control-panel,
    .readout-panel {
        right: 18px;
        left: 18px;
        width: auto;
    }

    .control-panel {
        top: auto;
        bottom: 252px;
    }
}

@media (max-width: 760px) {
    .lab-topbar {
        grid-template-columns: 38px minmax(0, 1fr) auto;
        min-height: 58px;
    }

    .icon-link,
    .icon-button {
        width: 38px;
        height: 38px;
    }

    .lab-board {
        padding-top: 94px;
    }

    .outcome-grid,
    .basis-list {
        grid-template-columns: 1fr;
    }
}
</style>
