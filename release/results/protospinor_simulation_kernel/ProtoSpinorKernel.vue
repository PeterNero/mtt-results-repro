<template>
    <section ref="shellRef" class="proto-shell">
        <canvas ref="canvasRef" class="proto-canvas" @pointerdown="onPointerDown" @pointermove="onPointerMove" @pointerup="onPointerUp" @pointerleave="onPointerUp" @wheel.prevent="onCanvasWheel"></canvas>

        <header class="topbar">
            <NuxtLink to="/" class="home-link" title="Home">
                <span class="i-tabler-arrow-left text-base"></span>
                <span>SandboxScience</span>
            </NuxtLink>
            <div class="title-wrap">
                <div class="title-row">
                    <span class="i-tabler-atom-2 title-icon"></span>
                    <h1>Proto-Spinor Kernel</h1>
                    <span class="mode-pill" :title="engineHint">{{ engineMode }}</span>
                    <span class="mode-pill interpretive-pill" :title="labelHint">labels: interp.</span>
                </div>
                <p>MTT-native carrier state in an extended upper world, with standard names used as readable overlays.</p>
            </div>
            <div class="top-actions">
                <button class="icon-button" type="button" :title="isRunning ? 'Pause' : 'Run'" @click="toggleRunning">
                    <span :class="isRunning ? 'i-tabler-player-pause' : 'i-tabler-player-play'"></span>
                </button>
                <button class="icon-button" type="button" title="Reset" @click="resetSimulation">
                    <span class="i-tabler-refresh"></span>
                </button>
            </div>
        </header>

        <aside class="control-panel">
            <section class="panel-section">
                <h2>Preset</h2>
                <div class="segmented">
                    <button v-for="preset in presets" :key="preset.id" type="button" :class="{ active: activePreset === preset.id }" @click="selectPreset(preset.id)">
                        {{ preset.label }}
                    </button>
                </div>
            </section>

            <section class="panel-section">
                <h2>Build</h2>
                <div class="build-actions">
                    <button type="button" title="Clear all particles and events" @click="clearSimulation">
                        <span class="i-tabler-trash"></span>
                        <b>Clear</b>
                    </button>
                    <button type="button" title="Inject a local zero-net-momentum energy pulse into nearby carriers" @click="addEnergyPulse">
                        <span class="i-tabler-flame"></span>
                        <b>Energy</b>
                    </button>
                    <button type="button" title="Add one unresolved proto-spinor primitive" @click="addEntity('primitive')">
                        <span class="i-tabler-sparkles"></span>
                        <b>Primitive</b>
                    </button>
                    <button type="button" title="Add one positive stable charge primitive" @click="addEntity('positive')">
                        <span class="i-tabler-plus"></span>
                        <b>Charge</b>
                    </button>
                    <button type="button" title="Add one negative stable charge primitive" @click="addEntity('negative')">
                        <span class="i-tabler-minus"></span>
                        <b>Charge</b>
                    </button>
                    <button type="button" title="Add one free interpretive electron carrier; net arena charge changes by -1" @click="addEntity('electron')">
                        <span class="i-tabler-bolt"></span>
                        <b>e-</b>
                    </button>
                    <button type="button" title="Add a conserved electron-positron pair" @click="addEntity('electronPair')">
                        <span class="i-tabler-arrows-exchange"></span>
                        <b>e-/e+</b>
                    </button>
                    <button type="button" title="Add a conserved positron-electron pair" @click="addEntity('positron')">
                        <span class="i-tabler-plus"></span>
                        <b>e+</b>
                    </button>
                    <button type="button" title="Add an interpretive muon label with compensating recoil" @click="addEntity('muon')">
                        <span class="i-tabler-wave-saw-tool"></span>
                        <b>mu-</b>
                    </button>
                    <button type="button" title="Add an interpretive anti-muon label with compensating recoil" @click="addEntity('antimuon')">
                        <span class="i-tabler-wave-sine"></span>
                        <b>mu+</b>
                    </button>
                    <button type="button" title="Add an interpretive neutrino and anti-neutrino pair" @click="addEntity('neutrino')">
                        <span class="i-tabler-circle-dashed"></span>
                        <b>nu</b>
                    </button>
                    <button type="button" title="Add an interpretive anti-neutrino and neutrino pair" @click="addEntity('antineutrino')">
                        <span class="i-tabler-circle-dashed-check"></span>
                        <b>anti-nu</b>
                    </button>
                    <button type="button" title="Add an interpretive photon label on a neutral wave carrier" @click="addEntity('photon')">
                        <span class="i-tabler-sun-electricity"></span>
                        <b>gamma</b>
                    </button>
                    <button type="button" title="Add an interpretive up-quark carrier with compensating recoil" @click="addEntity('upQuark')">
                        <span class="i-tabler-triangle"></span>
                        <b>u</b>
                    </button>
                    <button type="button" title="Add an interpretive down-quark carrier with compensating recoil" @click="addEntity('downQuark')">
                        <span class="i-tabler-triangle-inverted"></span>
                        <b>d</b>
                    </button>
                    <button type="button" title="Add one free interpretive proton carrier; net arena charge changes by +1" @click="addEntity('proton')">
                        <span class="i-tabler-circle-plus"></span>
                        <b>p+</b>
                    </button>
                    <button type="button" title="Add an interpretive neutron label on a neutral RGB triplet" @click="addEntity('neutron')">
                        <span class="i-tabler-circle"></span>
                        <b>n</b>
                    </button>
                    <button type="button" title="Add one full 24-carrier atom seed" @click="addEntity('atom')">
                        <span class="i-tabler-atom"></span>
                        <b>Atom</b>
                    </button>
                    <button type="button" title="Add a clustered multi-packet atom seed" @click="addEntity('bigAtom')">
                        <span class="i-tabler-circles"></span>
                        <b>Big Atom</b>
                    </button>
                    <button type="button" title="Add an interpretive protium label from MTT carriers" @click="addEntity('hydrogen')">
                        <span class="i-tabler-atom"></span>
                        <b>H</b>
                    </button>
                    <button type="button" title="Add an interpretive deuterium label from MTT carriers" @click="addEntity('deuterium')">
                        <span class="i-tabler-atom"></span>
                        <b>D</b>
                    </button>
                    <button type="button" title="Add an interpretive tritium label from MTT carriers" @click="addEntity('tritium')">
                        <span class="i-tabler-atom"></span>
                        <b>T</b>
                    </button>
                    <button type="button" title="Add an interpretive helium-4 label from MTT carriers" @click="addEntity('helium4')">
                        <span class="i-tabler-atom-2"></span>
                        <b>He-4</b>
                    </button>
                    <button type="button" title="Add an interpretive H2 label with shared carrier closure" @click="addEntity('h2')">
                        <span class="i-tabler-circles"></span>
                        <b>H2</b>
                    </button>
                    <button type="button" title="Add an interpretive H2O label with two bent closure bonds" @click="addEntity('water')">
                        <span class="i-tabler-droplet"></span>
                        <b>H2O</b>
                    </button>
                    <button type="button" title="Add an interpretive six-water cluster seed" @click="addEntity('waterCluster')">
                        <span class="i-tabler-droplets"></span>
                        <b>H2O x6</b>
                    </button>
                </div>
            </section>

            <section class="panel-section">
                <h2>Kernel</h2>
                <label>
                    <span>Particles</span>
                    <input v-model.number="settings.particleCount" type="range" min="24" max="1608" step="24" @change="resetSimulation">
                    <strong>{{ settings.particleCount }}</strong>
                </label>
                <label>
                    <span>Circle</span>
                    <input v-model.number="settings.circleStrength" type="range" min="0" max="2.4" step="0.05">
                    <strong>{{ settings.circleStrength.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Lens</span>
                    <input v-model.number="settings.lensStrength" type="range" min="0" max="2.6" step="0.05">
                    <strong>{{ settings.lensStrength.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Nil gate</span>
                    <input v-model.number="settings.nilThreshold" type="range" min="0.10" max="0.95" step="0.01">
                    <strong>{{ settings.nilThreshold.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Capacity</span>
                    <input v-model.number="settings.capacity" type="range" min="0.2" max="1.6" step="0.02">
                    <strong>{{ settings.capacity.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Gravity</span>
                    <input v-model.number="settings.gravityStrength" type="range" min="0" max="1.4" step="0.02">
                    <strong>{{ settings.gravityStrength.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Upper</span>
                    <input v-model.number="settings.projectionDepth" type="range" min="0" max="1.4" step="0.02">
                    <strong>{{ settings.projectionDepth.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Time</span>
                    <input v-model.number="settings.timeCurvature" type="range" min="0" max="1.0" step="0.02">
                    <strong>{{ settings.timeCurvature.toFixed(2) }}</strong>
                </label>
            </section>

            <section class="panel-section">
                <h2>Toy Constants</h2>
                <label class="checkbox-row" title="Use an explicit toy energy ledger to nudge EM, Pauli, quark-string, nuclear, bond, and photon behavior">
                    <input v-model="physicsLedgerEnabled" type="checkbox">
                    <span>Energy ledger</span>
                </label>
                <label>
                    <span>Ledger F</span>
                    <input v-model.number="settings.physicsLedgerStrength" type="range" min="0" max="1.4" step="0.02">
                    <strong>{{ settings.physicsLedgerStrength.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Source</span>
                    <input v-model.number="settings.sourceCoupling" type="range" min="0.35" max="2.4" step="0.02">
                    <strong>{{ settings.sourceCoupling.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Return</span>
                    <input v-model.number="settings.upperWorldCoupling" type="range" min="0.35" max="2.4" step="0.02">
                    <strong>{{ settings.upperWorldCoupling.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Spread</span>
                    <input v-model.number="settings.carrierSpread" type="range" min="0.45" max="2.6" step="0.02">
                    <strong>{{ settings.carrierSpread.toFixed(2) }}</strong>
                </label>
            </section>

            <section class="panel-section">
                <h2>Measure</h2>
                <label class="checkbox-row">
                    <input v-model="lookingGlassEnabled" type="checkbox">
                    <span>Looking glass</span>
                </label>
                <div class="measure-tabs">
                    <button type="button" :class="{ active: measurementKind === 'projector' }" title="Local branch projection" @click="measurementKind = 'projector'">
                        Project
                    </button>
                    <button type="button" :class="{ active: measurementKind === 'interference' }" title="Coherence-preserving phase probe" @click="measurementKind = 'interference'">
                        Phase
                    </button>
                    <button type="button" :class="{ active: measurementKind === 'whichPath' }" title="Strong which-path detector" @click="measurementKind = 'whichPath'">
                        Path
                    </button>
                    <button type="button" :class="{ active: measurementKind === 'split' }" title="Two-lobe split detector" @click="measurementKind = 'split'">
                        Split
                    </button>
                </div>
                <label>
                    <span>Radius</span>
                    <input v-model.number="settings.measurementRadius" type="range" min="36" max="180" step="2">
                    <strong>{{ settings.measurementRadius.toFixed(0) }}</strong>
                </label>
                <label>
                    <span>Focus</span>
                    <input v-model.number="settings.measurementStrength" type="range" min="0" max="1.4" step="0.02">
                    <strong>{{ settings.measurementStrength.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Entangle</span>
                    <input v-model.number="settings.entanglementStrength" type="range" min="0" max="1.4" step="0.02">
                    <strong>{{ settings.entanglementStrength.toFixed(2) }}</strong>
                </label>
            </section>

            <section class="panel-section">
                <h2>View</h2>
                <div class="view-tabs">
                    <button type="button" :class="{ active: layerView === 'spinor' }" title="Internal spinor view" @click="layerView = 'spinor'">
                        Spinor
                    </button>
                    <button type="button" :class="{ active: layerView === 'particle' }" title="Physical particle view" @click="layerView = 'particle'">
                        Particle
                    </button>
                    <button type="button" :class="{ active: layerView === 'atom' }" title="Atom composite view" @click="layerView = 'atom'">
                        Atom
                    </button>
                    <button type="button" :class="{ active: layerView === 'orbital' }" title="Visible cloud from upper-world carrier state" @click="layerView = 'orbital'">
                        Cloud
                    </button>
                </div>
                <div v-if="layerView === 'orbital'" class="orbital-tabs">
                    <button type="button" :class="{ active: orbitalSampleMode === 'raw' }" title="Use visible electron offsets relative to detected nuclei" @click="setOrbitalSampleMode('raw')">
                        Visible
                    </button>
                    <button type="button" :class="{ active: orbitalSampleMode === 'guided' }" title="Use calibrated proto-spinor upper-world carrier samples" @click="setOrbitalSampleMode('guided')">
                        Upper
                    </button>
                </div>
                <div class="toggle-row">
                    <button type="button" :class="{ active: viewMode === 'mode' }" @click="viewMode = 'mode'">Mode</button>
                    <button type="button" :class="{ active: viewMode === 'nil' }" @click="viewMode = 'nil'">Nil</button>
                    <button type="button" :class="{ active: viewMode === 'phase' }" @click="viewMode = 'phase'">Phase</button>
                    <button type="button" :class="{ active: viewMode === 'cost' }" @click="viewMode = 'cost'">Cost</button>
                    <button type="button" :class="{ active: viewMode === 'pressure' }" @click="viewMode = 'pressure'">Stress</button>
                </div>
                <label class="checkbox-row">
                    <input v-model="showLinks" type="checkbox">
                    <span>Show composite links</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="showWaves" type="checkbox">
                    <span>Show unresolved waves</span>
                </label>
                <label class="checkbox-row" title="Visual only; the Entangle slider changes the kernel dynamics.">
                    <input v-model="showEntanglement" type="checkbox">
                    <span>Show entangle links</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="showQuarkBinding" type="checkbox">
                    <span>Show quark binding</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="showGeometryField" type="checkbox">
                    <span>Show geometry field</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="showProjectionEvents" type="checkbox">
                    <span>Show projection events</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="showLookingGlassOverlay" type="checkbox">
                    <span>Show looking glass</span>
                </label>
                <label v-if="isSmPreset() && layerView === 'particle'" class="checkbox-row">
                    <input v-model="showSmMarkers" type="checkbox">
                    <span>Show SM markers</span>
                </label>
                <label v-if="layerView === 'atom' || layerView === 'orbital'" class="checkbox-row">
                    <input v-model="showAtomCarrierField" type="checkbox">
                    <span>Inside carriers</span>
                </label>
                <label v-if="layerView === 'atom' || layerView === 'orbital'" class="checkbox-row">
                    <input v-model="showMolecularBonds" type="checkbox">
                    <span>Show bonds</span>
                </label>
                <label v-if="layerView === 'atom' || layerView === 'orbital'" class="checkbox-row">
                    <input v-model="showAtomNuclei" type="checkbox">
                    <span>Show nuclei</span>
                </label>
                <label v-if="layerView === 'atom' || layerView === 'orbital'" class="checkbox-row">
                    <input v-model="showAtomShells" type="checkbox">
                    <span>Show shells</span>
                </label>
                <label v-if="layerView === 'atom' || layerView === 'orbital'" class="checkbox-row">
                    <input v-model="showAtomLabels" type="checkbox">
                    <span>Show labels</span>
                </label>
                <label v-if="layerView === 'atom'" class="checkbox-row">
                    <input v-model="showAtomHalos" type="checkbox">
                    <span>Show atom halos</span>
                </label>
                <label v-if="layerView === 'orbital'" class="checkbox-row">
                    <input v-model="showOrbitalReference" type="checkbox">
                    <span>Reference overlay</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="stirField" type="checkbox">
                    <span>Pointer stirs field</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="dragArena" type="checkbox">
                    <span>Drag arena</span>
                </label>
                <label>
                    <span>Zoom</span>
                    <input v-model.number="camera.zoom" type="range" min="0.35" max="3" step="0.05">
                    <strong>{{ camera.zoom.toFixed(2) }}x</strong>
                </label>
                <div class="zoom-actions">
                    <button type="button" title="Zoom out" @click="zoomBy(0.84)">
                        <span class="i-tabler-zoom-out"></span>
                    </button>
                    <button type="button" title="Reset zoom" @click="resetCamera">
                        <span class="i-tabler-focus-centered"></span>
                    </button>
                    <button type="button" title="Zoom in" @click="zoomBy(1.18)">
                        <span class="i-tabler-zoom-in"></span>
                    </button>
                </div>
            </section>

            <section class="panel-section">
                <h2>Engine</h2>
                <div class="engine-status">
                    <span class="i-tabler-cpu"></span>
                    <strong>CPU active</strong>
                    <em>GPU is the right next option for larger particle counts, but this MTT kernel still runs on CPU.</em>
                </div>
            </section>
        </aside>

        <aside class="metrics-panel">
            <div v-for="metric in metricCards" :key="metric.label" class="metric">
                <span>{{ metric.label }}</span>
                <strong>{{ metric.value }}</strong>
            </div>
        </aside>

        <aside v-if="isSmPreset()" class="sm-rail">
            <section class="sm-legend">
                <h2>SM Overlay</h2>
                <div v-for="item in smLegendItems" :key="item.label" class="sm-legend-item">
                    <i :style="{ background: item.color, boxShadow: `0 0 14px ${item.glow}` }"></i>
                    <span>{{ item.label }}</span>
                </div>
            </section>

            <section class="invariant-ledger">
                <h2>Invariant Ledger</h2>
                <div v-for="item in invariantLedger" :key="item.label" class="ledger-item" :class="item.status">
                    <i></i>
                    <span>
                        <strong>{{ item.label }}</strong>
                        <em>{{ item.detail }}</em>
                    </span>
                    <b>{{ item.value }}</b>
                </div>
            </section>

            <section class="source-audit">
                <h2>Source Audit</h2>
                <div v-for="item in sourceAudit" :key="item.label" class="source-item" :class="item.kind">
                    <i>{{ item.kind }}</i>
                    <span>
                        <strong>{{ item.label }}</strong>
                        <em>{{ item.detail }}</em>
                    </span>
                </div>
            </section>
        </aside>

        <div class="legend">
            <span v-for="item in layerLegend" :key="item.label">
                <i class="dot" :style="{ background: item.color, boxShadow: `0 0 10px ${item.glow}` }"></i>{{ item.label }}
            </span>
        </div>
    </section>
</template>

<script setup lang="ts">
type Mode = 0 | 1 | 2 | 3
type PresetId = 'balanced' | 'basins' | 'composites' | 'partition' | 'sm' | 'oneAtom'
type LayerView = 'spinor' | 'particle' | 'atom' | 'orbital'
type ViewMode = 'mode' | 'nil' | 'phase' | 'cost' | 'pressure'
type MeasurementKind = 'projector' | 'interference' | 'whichPath' | 'split'
type MeasurementState = 'unresolved' | 'focused' | 'anchored'
type SpawnKind = 'primitive' | 'positive' | 'negative' | 'electron' | 'electronPair' | 'positron' | 'muon' | 'antimuon' | 'neutrino' | 'antineutrino' | 'photon' | 'upQuark' | 'downQuark' | 'proton' | 'neutron' | 'atom' | 'bigAtom' | 'hydrogen' | 'deuterium' | 'tritium' | 'helium4' | 'h2' | 'water' | 'waterCluster'
type BranchWeights = [number, number, number]
type SmKind = 'generic' | 'electron' | 'positron' | 'muon' | 'antimuon' | 'neutrino' | 'antineutrino' | 'quarkR' | 'quarkG' | 'quarkB' | 'photon' | 'gluon'
type GaugeColor = 'none' | 'red' | 'green' | 'blue'
type Chirality = 'L' | 'R'
type LedgerStatus = 'pass' | 'warn' | 'fail'
type SourceKind = 'native' | 'derived' | 'scaffold'
type OrbitalKind = 'none' | '1s' | '2s' | '2p'
type OrbitalSampleMode = 'raw' | 'guided'
type QuarkFlavor = 'up' | 'down'
type NucleonKind = 'proton' | 'neutron'
type AtomicSpawnKind = 'hydrogen' | 'deuterium' | 'tritium' | 'helium4'
type AtomicElementKind = AtomicSpawnKind | 'oxygen16'

interface ProtoParticle {
    seedIndex: number
    packetId: number
    x: number
    y: number
    z: number
    vx: number
    vy: number
    vz: number
    theta: number
    phaseTotal: number
    theta0: number
    sigma: number
    sigmaTotal: number
    sigma0: number
    lens: -1 | 0 | 1
    nil: -1 | 0 | 1 | 2
    J: number
    coherence: number
    recurrence: number
    neutrality: number
    pressure: number
    massLoad: number
    properTime: number
    timeRate: number
    entanglementId: number
    entanglementPhase: number
    branchWeights: BranchWeights
    measurement: MeasurementState
    lastMeasuredFrame: number
    smKind: SmKind
    electricCharge: number
    hypercharge: number
    weakIso: number
    color: GaugeColor
    chirality: Chirality
    spin: number
    gamma: number
    mode: Mode
    age: number
    lastTurn: number
    lastSigmaTurn: number
    radius: number
}

interface ProjectionEvent {
    x: number
    y: number
    radius: number
    maxRadius: number
    life: number
    maxLife: number
    hue: number
    width: number
}

interface EntanglementSummary {
    id: number
    count: number
    phaseX: number
    phaseY: number
    sigmaX: number
    sigmaY: number
    lensSum: number
    nilCounts: BranchWeights
    anchorCount: number
    coherenceSum: number
    meanPhase: number
    meanSigma: number
    coherence: number
    selectedNil: 0 | 1 | 2
}

interface EntanglementState {
    summaries: Map<number, EntanglementSummary>
    members: Map<number, number[]>
}

interface MttOccupancyCell {
    key: string
    indices: number[]
    x: number
    y: number
    z: number
}

interface MttOccupancyState {
    costs: Float32Array
    cellKeys: string[]
    cells: Map<string, MttOccupancyCell>
    activeCells: number
    meanCost: number
}

interface PresetConfig {
    id: PresetId
    label: string
    particles: number
    circleStrength: number
    lensStrength: number
    nilThreshold: number
    capacity: number
    phaseDrift: number
    compositeBias: number
    gravityStrength: number
    projectionDepth: number
    timeCurvature: number
    entanglementStrength: number
    measurementStrength: number
    measurementRadius: number
    sourceCoupling: number
    upperWorldCoupling: number
    carrierSpread: number
    physicsLedgerStrength: number
}

interface InvariantEntry {
    label: string
    detail: string
    value: string
    status: LedgerStatus
}

interface SourceAuditEntry {
    label: string
    detail: string
    kind: SourceKind
}

interface ColorClosureStats {
    groups: number
    closed: number
    closure: number
}

interface MeasurementProfile {
    gain: number
    kind: MeasurementKind
    branch?: 0 | 1 | 2
}

interface MttClosureCost {
    total: number
    phase: number
    nil: number
    lens: number
    capacity: number
    winding: number
    compression: number
}

interface PhysicsEnergyLedger {
    kinetic: number
    coulomb: number
    confinement: number
    nuclear: number
    pauli: number
    orbital: number
    bond: number
    photon: number
    total: number
}

interface AtomComposite {
    id: number
    x: number
    y: number
    z: number
    protons: number
    neutrons: number
    electrons: number
    charge: number
    stability: number
    radius: number
    nucleusIds: number[]
    electronIds: number[]
    clusterId: number
}

interface DeclaredAtom {
    id: number
    label: string
    protons: number
    neutrons: number
    nucleusIds: number[]
    electronIds: number[]
    bondIds: number[]
    x: number
    y: number
    z: number
    shellRadius: number
    moleculeId: number
}

interface DeclaredBond {
    id: number
    label: string
    atomIds: [number, number]
    electronIds: number[]
    restLength: number
    order: number
    stability: number
    freeEnergy: number
    boundEnergy: number
    binding: number
    moleculeId: number
}

interface WaterMolecule {
    moleculeId: number
    oxygen: DeclaredAtom
    leftHydrogen: DeclaredAtom
    rightHydrogen: DeclaredAtom
}

interface BindingEnergy {
    free: number
    bound: number
    binding: number
    stability: number
}

interface BaryonCandidate extends BindingEnergy {
    id: number
    kind: NucleonKind
    indices: number[]
    charge: number
    center: { x: number, y: number, z: number }
}

interface BondClosureEnergy extends BindingEnergy {
    distance: number
    bridge: number
    repulsion: number
    pressure: number
}

interface OrbitalSample {
    atomId: number
    dx: number
    dy: number
    dz: number
    weight: number
    age: number
    branch: 0 | 1 | 2
    theta: number
    kind: OrbitalKind
    mode: OrbitalSampleMode
}

const TAU = Math.PI * 2
const canvasRef = ref<HTMLCanvasElement | null>(null)
const shellRef = ref<HTMLElement | null>(null)
const isRunning = ref(true)
const showLinks = ref(true)
const showWaves = ref(true)
const showEntanglement = ref(true)
const showQuarkBinding = ref(true)
const showGeometryField = ref(true)
const showProjectionEvents = ref(true)
const showLookingGlassOverlay = ref(true)
const showSmMarkers = ref(true)
const showAtomCarrierField = ref(false)
const showMolecularBonds = ref(true)
const showAtomNuclei = ref(true)
const showAtomShells = ref(true)
const showAtomLabels = ref(true)
const showAtomHalos = ref(true)
const showOrbitalReference = ref(false)
const stirField = ref(true)
const dragArena = ref(true)
const physicsLedgerEnabled = ref(true)
const lookingGlassEnabled = ref(true)
const measurementKind = ref<MeasurementKind>('projector')
const orbitalSampleMode = ref<OrbitalSampleMode>('raw')
const layerView = ref<LayerView>('particle')
const viewMode = ref<ViewMode>('mode')
const activePreset = ref<PresetId>('balanced')
const engineMode = 'CPU'
const engineHint = 'Current kernel is CPU-backed. A true GPU mode should move pair forces, carrier updates, and reductions into WebGPU buffers.'
const labelHint = 'Standard physics names are interpretive overlays on top of the MTT carrier state, not derived particle identifications yet.'

const camera = reactive({
    zoom: 1,
    x: 0,
    y: 0,
})

const presets: PresetConfig[] = [
    { id: 'balanced', label: 'Balanced', particles: 360, circleStrength: 1.05, lensStrength: 1.15, nilThreshold: 0.54, capacity: 0.92, phaseDrift: 0.006, compositeBias: 0.55, gravityStrength: 0.32, projectionDepth: 0.72, timeCurvature: 0.46, entanglementStrength: 0.74, measurementStrength: 0.82, measurementRadius: 94, sourceCoupling: 1, upperWorldCoupling: 1, carrierSpread: 1, physicsLedgerStrength: 0.36 },
    { id: 'basins', label: 'Nil Basins', particles: 408, circleStrength: 0.85, lensStrength: 0.85, nilThreshold: 0.42, capacity: 0.72, phaseDrift: 0.004, compositeBias: 0.3, gravityStrength: 0.22, projectionDepth: 0.82, timeCurvature: 0.36, entanglementStrength: 0.68, measurementStrength: 0.76, measurementRadius: 108, sourceCoupling: 0.9, upperWorldCoupling: 1.18, carrierSpread: 1.08, physicsLedgerStrength: 0.34 },
    { id: 'composites', label: 'Composites', particles: 432, circleStrength: 0.75, lensStrength: 1.85, nilThreshold: 0.62, capacity: 0.98, phaseDrift: 0.005, compositeBias: 1.0, gravityStrength: 0.46, projectionDepth: 0.68, timeCurvature: 0.58, entanglementStrength: 0.86, measurementStrength: 0.72, measurementRadius: 90, sourceCoupling: 1.1, upperWorldCoupling: 0.92, carrierSpread: 0.98, physicsLedgerStrength: 0.46 },
    { id: 'partition', label: 'Partition', particles: 360, circleStrength: 1.45, lensStrength: 1.25, nilThreshold: 0.68, capacity: 0.56, phaseDrift: 0.009, compositeBias: 0.15, gravityStrength: 0.18, projectionDepth: 0.96, timeCurvature: 0.5, entanglementStrength: 0.92, measurementStrength: 0.94, measurementRadius: 116, sourceCoupling: 0.86, upperWorldCoupling: 1.35, carrierSpread: 1.18, physicsLedgerStrength: 0.28 },
    { id: 'sm', label: 'SM Overlay', particles: 384, circleStrength: 1.42, lensStrength: 2.24, nilThreshold: 0.38, capacity: 1.34, phaseDrift: 0.006, compositeBias: 1.16, gravityStrength: 0.06, projectionDepth: 0.62, timeCurvature: 0.14, entanglementStrength: 0.82, measurementStrength: 0.18, measurementRadius: 104, sourceCoupling: 0.75, upperWorldCoupling: 1.8, carrierSpread: 1.5, physicsLedgerStrength: 0.62 },
    { id: 'oneAtom', label: 'One Atom', particles: 24, circleStrength: 1.42, lensStrength: 2.35, nilThreshold: 0.44, capacity: 1.42, phaseDrift: 0.004, compositeBias: 1.35, gravityStrength: 0.02, projectionDepth: 0.72, timeCurvature: 0.18, entanglementStrength: 1.06, measurementStrength: 0.28, measurementRadius: 126, sourceCoupling: 0.95, upperWorldCoupling: 1.62, carrierSpread: 1.82, physicsLedgerStrength: 0.72 },
]

const smLegendItems = [
    { label: 'interp U(1) charge', color: '#67e8f9', glow: 'rgba(103, 232, 249, 0.45)' },
    { label: 'interp SU(2) neutral', color: '#a5b4fc', glow: 'rgba(165, 180, 252, 0.42)' },
    { label: 'interp SU(3) triplet', color: 'linear-gradient(90deg, #ef4444, #22c55e, #3b82f6)', glow: 'rgba(255, 255, 255, 0.28)' },
    { label: 'interp quark Q', color: '#22c55e', glow: 'rgba(34, 197, 94, 0.45)' },
    { label: 'interp gamma wave', color: '#fde68a', glow: 'rgba(253, 230, 138, 0.5)' },
    { label: 'interp gluon link', color: '#c084fc', glow: 'rgba(192, 132, 252, 0.5)' },
]

const settings = reactive({
    particleCount: 720,
    circleStrength: 1.05,
    lensStrength: 1.15,
    nilThreshold: 0.54,
    capacity: 0.92,
    phaseDrift: 0.006,
    compositeBias: 0.55,
    gravityStrength: 0.32,
    projectionDepth: 0.72,
    timeCurvature: 0.46,
    entanglementStrength: 0.74,
    measurementStrength: 0.82,
    measurementRadius: 94,
    sourceCoupling: 1,
    upperWorldCoupling: 1,
    carrierSpread: 1,
    physicsLedgerStrength: 0.5,
})

const metrics = reactive({
    anchors: 0,
    cancellation: 0,
    nil0: 0,
    nil1: 0,
    nil2: 0,
    meanJ: 0,
    meanCoherence: 0,
    meanPressure: 0,
    meanTimeRate: 1,
    meanDepth: 0,
    composites: 0,
    partitions: 0,
    entangled: 0,
    measured: 0,
    netCharge: 0,
    kineticEnergy: 0,
    netMomentum: 0,
    energyInput: 0,
    captureBoundEnergy: 0,
    captureRadiatedEnergy: 0,
    capturePhotons: 0,
    ledgerTotalEnergy: 0,
    ledgerEnergyDrift: 0,
    ledgerCoulombEnergy: 0,
    ledgerConfinementEnergy: 0,
    ledgerNuclearEnergy: 0,
    ledgerPauliEnergy: 0,
    ledgerOrbitalEnergy: 0,
    ledgerBondEnergy: 0,
    ledgerPhotonEnergy: 0,
    colorClosure: 0,
    leftShare: 0,
    meanGamma: 1,
    atomProtons: 0,
    atomNeutrons: 0,
    atomElectrons: 0,
    atomCandidates: 0,
    neutralAtoms: 0,
    atomClusters: 0,
    atomBonds: 0,
    molecules: 0,
    moleculeBendError: -1,
    baryonSamples: 0,
    boundBaryons: 0,
    baryonBinding: 0,
    bondBinding: 0,
    bondEnergy: 0,
    activationEnergy: 0,
    releasedEnergy: 0,
    mttOccupancyCells: 0,
    mttOccupancyCost: 0,
    orbitalSamples: 0,
    orbitalState: 'n/a',
    orbitalRadialError: -1,
    orbitalLobeBalance: -1,
})

const invariantState = reactive({
    baselineCharge: 0,
    chargeDrift: 0,
    qIdentity: 1,
    colorClosure: 0,
    colorGroups: 0,
    chiralityRule: 1,
    mediatorRule: 1,
    projectorRule: 1,
    mttClosureSamples: 0,
    mttClosureCost: 0,
    mttPhaseReturn: 1,
    mttNilBudget: 1,
    mttLensBalance: 1,
    mttWindingReturn: 1,
})

const metricCards = computed(() => {
    const cards = [
        { label: 'Particles', value: particles.length.toString() },
        { label: 'Anchors', value: metrics.anchors.toString() },
        { label: 'Cancel', value: metrics.cancellation.toString() },
        { label: 'Nil 0/1/2', value: `${metrics.nil0}/${metrics.nil1}/${metrics.nil2}` },
        { label: 'Mean J', value: metrics.meanJ.toFixed(3) },
        { label: 'Coherence', value: metrics.meanCoherence.toFixed(3) },
        { label: 'Stress', value: metrics.meanPressure.toFixed(3) },
        { label: 'Time', value: metrics.meanTimeRate.toFixed(3) },
        { label: 'Depth', value: metrics.meanDepth.toFixed(3) },
        { label: 'Composites', value: metrics.composites.toString() },
        { label: 'Entangled', value: metrics.entangled.toString() },
        { label: 'Measured', value: metrics.measured.toString() },
        { label: 'Partitions', value: metrics.partitions.toString() },
        { label: 'K energy', value: metrics.kineticEnergy.toFixed(1) },
        { label: 'Net p', value: metrics.netMomentum.toFixed(2) },
    ]

    if (layerView.value === 'atom' || layerView.value === 'orbital') {
        cards.unshift(
            { label: 'Atoms', value: metrics.atomCandidates.toString() },
            { label: 'Neutral', value: metrics.neutralAtoms.toString() },
            { label: 'Protons', value: metrics.atomProtons.toString() },
            { label: 'Neutrons', value: metrics.atomNeutrons.toString() },
            { label: 'Electrons', value: metrics.atomElectrons.toString() },
            { label: 'Lumps', value: metrics.atomClusters.toString() },
            { label: 'Bonds', value: metrics.atomBonds.toString() },
            { label: 'Molecules', value: metrics.molecules.toString() },
            { label: 'Bend err', value: metrics.moleculeBendError >= 0 ? `${metrics.moleculeBendError.toFixed(1)} deg` : 'n/a' },
            { label: 'Baryons', value: `${metrics.boundBaryons}/${metrics.baryonSamples}` },
            { label: 'Q bind', value: metrics.baryonBinding.toFixed(2) },
            { label: 'Bond bind', value: metrics.bondBinding.toFixed(2) },
            { label: 'Activate', value: metrics.activationEnergy.toFixed(2) },
            { label: 'Released', value: metrics.releasedEnergy.toFixed(2) },
        )
    }

    if (layerView.value === 'orbital') {
        cards.unshift(
            { label: 'Source', value: orbitalSampleMode.value === 'raw' ? 'Visible' : 'Upper' },
            { label: 'Samples', value: metrics.orbitalSamples.toString() },
            { label: 'Carrier', value: metrics.orbitalState },
        )

        if (showOrbitalReference.value) {
            cards.unshift(
                { label: 'Ref err', value: metrics.orbitalRadialError >= 0 ? `${Math.round(metrics.orbitalRadialError * 100)}%` : 'n/a' },
                { label: 'Split', value: metrics.orbitalLobeBalance >= 0 ? metrics.orbitalLobeBalance.toFixed(2) : 'n/a' },
            )
        }
    }

    if (isSmPreset()) {
        if (layerView.value !== 'atom' && layerView.value !== 'orbital') {
            cards.push(
                { label: 'Baryons', value: `${metrics.boundBaryons}/${metrics.baryonSamples}` },
                { label: 'Q bind', value: metrics.baryonBinding.toFixed(2) },
            )
        }

        cards.push(
            { label: 'Net Q', value: metrics.netCharge.toFixed(2) },
            { label: 'Pulse', value: metrics.energyInput.toFixed(1) },
            { label: 'Bound E', value: metrics.captureBoundEnergy.toFixed(2) },
            { label: 'Rad E', value: metrics.captureRadiatedEnergy.toFixed(2) },
            { label: 'γ cap', value: metrics.capturePhotons.toString() },
            { label: 'E total', value: metrics.ledgerTotalEnergy.toFixed(1) },
            { label: 'E drift', value: metrics.ledgerEnergyDrift.toFixed(2) },
            { label: 'U EM', value: metrics.ledgerCoulombEnergy.toFixed(2) },
            { label: 'U qcd', value: metrics.ledgerConfinementEnergy.toFixed(2) },
            { label: 'U Pauli', value: metrics.ledgerPauliEnergy.toFixed(2) },
            { label: 'U orb', value: metrics.ledgerOrbitalEnergy.toFixed(2) },
            { label: 'U nuc', value: metrics.ledgerNuclearEnergy.toFixed(2) },
            { label: 'U bond', value: metrics.ledgerBondEnergy.toFixed(2) },
            { label: 'E γ', value: metrics.ledgerPhotonEnergy.toFixed(2) },
            { label: 'Occ cells', value: metrics.mttOccupancyCells.toString() },
            { label: 'Occ cost', value: metrics.mttOccupancyCost.toFixed(3) },
            { label: 'Color OK', value: `${Math.round(metrics.colorClosure * 100)}%` },
            { label: 'L share', value: `${Math.round(metrics.leftShare * 100)}%` },
            { label: 'Gamma', value: metrics.meanGamma.toFixed(2) },
        )
    }

    return cards
})

const layerLegend = computed(() => {
    if (layerView.value === 'spinor') {
        const legend = [
            { label: 'theta carrier', color: '#6ff5be', glow: 'rgba(111, 245, 190, 0.45)' },
            { label: 'sigma carrier', color: '#b88aff', glow: 'rgba(184, 138, 255, 0.45)' },
            { label: 'nil basin', color: '#ffd273', glow: 'rgba(255, 210, 115, 0.42)' },
        ]
        if (showLookingGlassOverlay.value && lookingGlassEnabled.value) {
            legend.push({ label: 'looking glass', color: '#fff2be', glow: 'rgba(255, 242, 190, 0.42)' })
        }
        return legend
    }

    if (layerView.value === 'atom') {
        return [
            ...(showAtomNuclei.value ? [
                { label: 'nucleus', color: '#fb7185', glow: 'rgba(251, 113, 133, 0.45)' },
                { label: 'neutron load', color: '#cbd5e1', glow: 'rgba(203, 213, 225, 0.38)' },
            ] : []),
            ...(showAtomShells.value ? [{ label: 'electron shell', color: '#67e8f9', glow: 'rgba(103, 232, 249, 0.45)' }] : []),
            ...(showMolecularBonds.value ? [{ label: 'molecular bond', color: '#fde68a', glow: 'rgba(253, 230, 138, 0.42)' }] : []),
            ...(showAtomHalos.value ? [{ label: 'stability halo', color: '#67e8f9', glow: 'rgba(103, 232, 249, 0.32)' }] : []),
            ...(showAtomCarrierField.value ? [{ label: 'carrier field', color: '#96b1cd', glow: 'rgba(150, 177, 205, 0.34)' }] : []),
        ]
    }

    if (layerView.value === 'orbital') {
        const legend = [
            { label: orbitalSampleMode.value === 'raw' ? 'visible samples' : 'upper-world samples', color: '#67e8f9', glow: 'rgba(103, 232, 249, 0.45)' },
        ]
        if (showAtomNuclei.value) {
            legend.push({ label: 'nucleus', color: '#fb7185', glow: 'rgba(251, 113, 133, 0.45)' })
        }
        if (showOrbitalReference.value) {
            legend.splice(1, 0, { label: 'reference overlay', color: '#fde68a', glow: 'rgba(253, 230, 138, 0.42)' })
        }
        if (showMolecularBonds.value) {
            legend.push({ label: 'molecular bond', color: '#fde68a', glow: 'rgba(253, 230, 138, 0.42)' })
        }
        if (showLookingGlassOverlay.value && lookingGlassEnabled.value) {
            legend.push({ label: 'looking glass', color: '#fff2be', glow: 'rgba(255, 242, 190, 0.42)' })
        }
        return legend
    }

    const legend = [
        { label: 'projected anchors', color: '#6ff5be', glow: 'rgba(111, 245, 190, 0.45)' },
    ]
    if (showProjectionEvents.value) {
        legend.push({ label: 'projection events', color: '#b88aff', glow: 'rgba(184, 138, 255, 0.45)' })
    }
    if (showWaves.value) {
        legend.push({ label: 'unresolved waves', color: '#96b1cd', glow: 'rgba(150, 177, 205, 0.34)' })
    }
    if (showLookingGlassOverlay.value && lookingGlassEnabled.value) {
        legend.push({ label: 'looking glass', color: '#fff2be', glow: 'rgba(255, 242, 190, 0.42)' })
    }
    return legend
})

const invariantLedger = computed<InvariantEntry[]>(() => {
    if (!isSmPreset()) return []

    const chargeDelta = Math.abs(invariantState.chargeDrift)
    const colorValue = invariantState.colorGroups > 0
        ? `${Math.round(invariantState.colorClosure * 100)}%`
        : 'n/a'
    const hasClosureSamples = invariantState.mttClosureSamples > 0
    const energyScale = Math.max(1, Math.abs(metrics.ledgerTotalEnergy))
    const energyDriftShare = Math.abs(metrics.ledgerEnergyDrift) / energyScale

    return [
        {
            label: 'U(1) charge',
            detail: 'net Q conserved after source add',
            value: formatSignedCharge(invariantState.chargeDrift),
            status: chargeDelta < 0.001 ? 'pass' : chargeDelta < 0.1 ? 'warn' : 'fail',
        },
        {
            label: 'Arena charge',
            detail: 'current net Q may be nonzero',
            value: metrics.netCharge.toFixed(2),
            status: Math.abs(metrics.netCharge) < 0.001 ? 'pass' : 'warn',
        },
        {
            label: 'Q=T3+Y/2',
            detail: 'interpretive EW bookkeeping',
            value: `${Math.round(invariantState.qIdentity * 100)}%`,
            status: scoreStatus(invariantState.qIdentity, 0.995, 0.96),
        },
        {
            label: 'SU(3) singlets',
            detail: 'interpretive RGB closure',
            value: colorValue,
            status: invariantState.colorGroups > 0 ? scoreStatus(invariantState.colorClosure, 0.995, 0.84) : 'warn',
        },
        {
            label: 'Quark binding',
            detail: 'carrier cost favors RGB',
            value: metrics.baryonSamples > 0 ? `${metrics.boundBaryons}/${metrics.baryonSamples}` : 'n/a',
            status: metrics.baryonSamples > 0
                ? metrics.boundBaryons === metrics.baryonSamples && metrics.baryonBinding > 0.04 ? 'pass' : metrics.baryonBinding > 0 ? 'warn' : 'fail'
                : 'warn',
        },
        {
            label: 'Bond binding',
            detail: 'carrier bridge lowers cost',
            value: declaredBonds.length > 0 ? metrics.bondBinding.toFixed(2) : 'n/a',
            status: declaredBonds.length > 0
                ? metrics.bondBinding > 0.08 ? 'pass' : metrics.bondBinding > 0 ? 'warn' : 'fail'
                : 'warn',
        },
        {
            label: 'Release barrier',
            detail: 'activation paid, binding released',
            value: metrics.releasedEnergy > 0 ? `${metrics.releasedEnergy.toFixed(2)}/${metrics.activationEnergy.toFixed(2)}` : 'n/a',
            status: metrics.releasedEnergy > 0
                ? metrics.releasedEnergy + metrics.activationEnergy > 0.12 ? 'pass' : 'warn'
                : 'warn',
        },
        {
            label: 'Energy ledger',
            detail: 'toy Hamiltonian drift',
            value: metrics.ledgerEnergyDrift.toFixed(2),
            status: energyDriftShare < 0.16 ? 'pass' : energyDriftShare < 0.42 ? 'warn' : 'fail',
        },
        {
            label: 'Chirality',
            detail: 'interpretive L/R labels',
            value: `${Math.round(invariantState.chiralityRule * 100)}%`,
            status: scoreStatus(invariantState.chiralityRule, 0.995, 0.96),
        },
        {
            label: 'Mediators',
            detail: 'interpretive spin-1 labels',
            value: `${Math.round(invariantState.mediatorRule * 100)}%`,
            status: scoreStatus(invariantState.mediatorRule, 0.995, 0.96),
        },
        {
            label: 'Projectors',
            detail: 'carrier finite nil map',
            value: `${Math.round(invariantState.projectorRule * 100)}%`,
            status: scoreStatus(invariantState.projectorRule, 0.995, 0.96),
        },
        {
            label: 'MTT J',
            detail: '-grad closure response',
            value: hasClosureSamples ? invariantState.mttClosureCost.toFixed(3) : 'n/a',
            status: hasClosureSamples ? costStatus(invariantState.mttClosureCost, 0.18, 0.34) : 'warn',
        },
        {
            label: 'Phase return',
            detail: 'recurrence/winding ledger',
            value: `${Math.round(invariantState.mttPhaseReturn * 100)}%`,
            status: scoreStatus(invariantState.mttPhaseReturn, 0.78, 0.58),
        },
        {
            label: 'Nil budget',
            detail: 'carrier basin selected',
            value: `${Math.round(invariantState.mttNilBudget * 100)}%`,
            status: scoreStatus(invariantState.mttNilBudget, 0.82, 0.62),
        },
        {
            label: 'Lens balance',
            detail: 'charge/lens bookkeeping',
            value: `${Math.round(invariantState.mttLensBalance * 100)}%`,
            status: scoreStatus(invariantState.mttLensBalance, 0.92, 0.74),
        },
        {
            label: 'Return flow',
            detail: 'upper carrier recurrence',
            value: `${Math.round(invariantState.mttWindingReturn * 100)}%`,
            status: scoreStatus(invariantState.mttWindingReturn, 0.58, 0.36),
        },
    ]
})

const sourceAudit = computed<SourceAuditEntry[]>(() => {
    if (!isSmPreset()) return []

    const declaredStructureCount = declaredAtoms.length + declaredBonds.length
    return [
        {
            label: 'Circle/lens/nil kernel',
            detail: 'theta, sigma, lens, nil, J, recurrence',
            kind: 'native',
        },
        {
            label: 'Gauge-locality response',
            detail: 'phase/lens/color constraints on carriers',
            kind: 'derived',
        },
        {
            label: 'Fermion occupancy',
            detail: `${metrics.mttOccupancyCells} active cells, cost ${metrics.mttOccupancyCost.toFixed(3)}`,
            kind: 'derived',
        },
        {
            label: 'SM particle names',
            detail: 'labels for reading the carrier state',
            kind: 'scaffold',
        },
        {
            label: 'Declared atoms/molecules',
            detail: declaredStructureCount > 0 ? `${declaredAtoms.length} atoms, ${declaredBonds.length} bonds` : 'none in current scene',
            kind: declaredStructureCount > 0 ? 'scaffold' : 'derived',
        },
        {
            label: 'Energy ledger',
            detail: 'diagnostic toy Hamiltonian, not calibrated conservation',
            kind: 'scaffold',
        },
    ]
})

let ctx: CanvasRenderingContext2D | null = null
let particles: ProtoParticle[] = []
let projectionEvents: ProjectionEvent[] = []
let atomComposites: AtomComposite[] = []
let declaredAtoms: DeclaredAtom[] = []
let declaredBonds: DeclaredBond[] = []
let orbitalSamples: OrbitalSample[] = []
let animationId = 0
const ARENA_SCALE = 2.4
const MAX_PAIR_INTERACTIONS = 85000
const CAPTURE_PHOTON_ENTANGLEMENT_ID = -2
const MAX_CAPTURE_PHOTONS = 12
let viewportWidth = 1
let viewportHeight = 1
let width = 1
let height = 1
let dpr = 1
let pointer = { active: false, id: -1, x: 0, y: 0, lastX: 0, lastY: 0, screenX: 0, screenY: 0, lastScreenX: 0, lastScreenY: 0, dragMode: 'field' as 'field' | 'pan' }
let lookingGlass = { active: false, x: 0, y: 0, pulseUntil: -1 }
let frame = 0
let geometry = { x: 0, y: 0, z: 0, load: 0, pressure: 0 }
let energyPulseResidue = 0
let captureBoundResidue = 0
let captureRadiatedResidue = 0
let physicsEnergyBaseline: number | null = null
let physicsEnergyBaselineWarmupUntil = 0
const capturePhotonLastByPacket = new Map<number, number>()
const inferredElectronCaptures = new Map<number, { nucleusId: number, strength: number, lastFrame: number, lastPhotonFrame: number }>()
let manualEmptyWorld = false
let nextDeclaredAtomId = 10000
let nextDeclaredBondId = 20000
let nextDeclaredMoleculeId = 30000
const MAX_ORBITAL_SAMPLES = 3600
const ORBITAL_SAMPLE_LIFE = 1500
const RAW_ORBITAL_SAMPLE_LIFE = 840

function applyPresetSettings(preset: PresetConfig) {
    settings.particleCount = preset.particles
    settings.circleStrength = preset.circleStrength
    settings.lensStrength = preset.lensStrength
    settings.nilThreshold = preset.nilThreshold
    settings.capacity = preset.capacity
    settings.phaseDrift = preset.phaseDrift
    settings.compositeBias = preset.compositeBias
    settings.gravityStrength = preset.gravityStrength
    settings.projectionDepth = preset.projectionDepth
    settings.timeCurvature = preset.timeCurvature
    settings.entanglementStrength = preset.entanglementStrength
    settings.measurementStrength = preset.measurementStrength
    settings.measurementRadius = preset.measurementRadius
    settings.sourceCoupling = preset.sourceCoupling
    settings.upperWorldCoupling = preset.upperWorldCoupling
    settings.carrierSpread = preset.carrierSpread
    settings.physicsLedgerStrength = preset.physicsLedgerStrength
}

function selectPreset(id: PresetId) {
    activePreset.value = id
    const preset = presets.find(item => item.id === id) ?? presets[0]
    applyPresetSettings(preset)
    resetSimulation()
}

function applyInitialPresetFromQuery() {
    const params = new URLSearchParams(window.location.search)
    const requested = params.get('preset')
    const requestedView = params.get('view')
    const requestedOrbital = params.get('orbital')
    if (requested === 'sm') selectPreset('sm')
    if (requested === 'oneAtom') selectPreset('oneAtom')
    if (requestedView === 'spinor' || requestedView === 'particle' || requestedView === 'atom' || requestedView === 'orbital') layerView.value = requestedView
    if (requestedOrbital === 'raw' || requestedOrbital === 'guided') setOrbitalSampleMode(requestedOrbital)
}

function resetSimulation() {
    manualEmptyWorld = false
    clearRuntimeState()
    seedParticles()
}

function resetMetricState() {
    Object.assign(metrics, {
        anchors: 0,
        cancellation: 0,
        nil0: 0,
        nil1: 0,
        nil2: 0,
        meanJ: 0,
        meanCoherence: 0,
        meanPressure: 0,
        meanTimeRate: 1,
        meanDepth: 0,
        composites: 0,
        partitions: 0,
        entangled: 0,
        measured: 0,
        netCharge: totalElectricCharge(),
        kineticEnergy: 0,
        netMomentum: 0,
        energyInput: 0,
        captureBoundEnergy: 0,
        captureRadiatedEnergy: 0,
        capturePhotons: 0,
        ledgerTotalEnergy: 0,
        ledgerEnergyDrift: 0,
        ledgerCoulombEnergy: 0,
        ledgerConfinementEnergy: 0,
        ledgerNuclearEnergy: 0,
        ledgerPauliEnergy: 0,
        ledgerOrbitalEnergy: 0,
        ledgerBondEnergy: 0,
        ledgerPhotonEnergy: 0,
        colorClosure: 0,
        leftShare: 0,
        meanGamma: 1,
        atomProtons: 0,
        atomNeutrons: 0,
        atomElectrons: 0,
        atomCandidates: 0,
        neutralAtoms: 0,
        atomClusters: 0,
        atomBonds: 0,
        molecules: 0,
        moleculeBendError: -1,
        baryonSamples: 0,
        boundBaryons: 0,
        baryonBinding: 0,
        bondBinding: 0,
        bondEnergy: 0,
        activationEnergy: 0,
        releasedEnergy: 0,
        mttOccupancyCells: 0,
        mttOccupancyCost: 0,
        orbitalSamples: 0,
        orbitalState: 'n/a',
        orbitalRadialError: -1,
        orbitalLobeBalance: -1,
    })
}

function clearRuntimeState() {
    particles = []
    projectionEvents = []
    atomComposites = []
    declaredAtoms = []
    declaredBonds = []
    orbitalSamples = []
    nextDeclaredAtomId = 10000
    nextDeclaredBondId = 20000
    nextDeclaredMoleculeId = 30000
    energyPulseResidue = 0
    captureBoundResidue = 0
    captureRadiatedResidue = 0
    physicsEnergyBaseline = null
    physicsEnergyBaselineWarmupUntil = frame + 36
    capturePhotonLastByPacket.clear()
    inferredElectronCaptures.clear()
    geometry = { x: width * 0.5, y: height * 0.5, z: 0, load: 0, pressure: 0 }
    resetMetricState()
}

function clearSimulation() {
    manualEmptyWorld = true
    clearRuntimeState()
    captureInvariantBaseline()
}

function toggleRunning() {
    isRunning.value = !isRunning.value
}

function resetOrbitalSamples() {
    orbitalSamples = []
    updateOrbitalMetrics()
}

function setOrbitalSampleMode(mode: OrbitalSampleMode) {
    if (orbitalSampleMode.value === mode) return
    orbitalSampleMode.value = mode
    resetOrbitalSamples()
}

function nextSeedIndex() {
    return particles.reduce((max, particle) => Math.max(max, particle.seedIndex), -1) + 1
}

function nextPacketId() {
    return particles.reduce((max, particle) => Math.max(max, particle.packetId), -1) + 1
}

function nextPacketSeedBase() {
    return Math.ceil(nextSeedIndex() / 24) * 24
}

function spawnSite() {
    const center = screenToWorld(viewportWidth * 0.5, viewportHeight * 0.5)
    const index = Math.max(0, nextSeedIndex())
    const angle = TAU * ((index * 0.38196601125) % 1)
    const radius = Math.min(34, 8 + (index % 5) * 5)
    return {
        x: center.x + Math.cos(angle) * radius,
        y: center.y + Math.sin(angle) * radius,
        z: 0,
    }
}

function offsetPoint(site: { x: number, y: number, z: number }, radius: number, angle: number, z = 0) {
    return {
        x: site.x + Math.cos(angle) * radius,
        y: site.y + Math.sin(angle) * radius,
        z: site.z + z,
    }
}

function pushManualParticle(params: {
    seedIndex?: number
    packetId?: number
    smKind?: SmKind
    x: number
    y: number
    z?: number
    theta?: number
    sigma?: number
    lens?: -1 | 0 | 1
    nil?: -1 | 0 | 1 | 2
    mode?: Mode
    electricCharge?: number
    hypercharge?: number
    weakIso?: number
    color?: GaugeColor
    chirality?: Chirality
    spin?: number
    coherence?: number
    recurrence?: number
    J?: number
    massLoad?: number
    entanglementId?: number
    entanglementPhase?: number
    vx?: number
    vy?: number
    vz?: number
    radius?: number
    measurement?: MeasurementState
    lastMeasuredFrame?: number
}) {
    const seedIndex = params.seedIndex ?? nextSeedIndex()
    const packetId = params.packetId ?? nextPacketId()
    const smKind = params.smKind ?? 'generic'
    const theta = params.theta ?? wrapAngle(TAU * ((seedIndex * 0.38196601125) % 1))
    const sigma = params.sigma ?? wrapAngle(TAU * ((seedIndex * 0.61803398875) % 1))
    const gauge = smGaugeState(smKind, seedIndex, theta, sigma)
    const electricCharge = params.electricCharge ?? gauge.electricCharge
    const fallbackLens = electricCharge < -0.001 ? -1 : electricCharge > 0.001 ? 1 : 0
    const lens = params.lens ?? (smKind === 'generic' ? fallbackLens : lensForSmKind(smKind, fallbackLens))
    const stableCharge = lens === -1 || lens === 1
    const nil = params.nil ?? (stableCharge || isQuarkKind(smKind) ? smNilForKind(smKind, theta, sigma) : -1)
    const mode = params.mode ?? (isQuarkKind(smKind) ? 3 : stableCharge ? 1 : 0)
    const hypercharge = params.hypercharge ?? (smKind === 'generic' ? electricCharge * 2 : gauge.hypercharge)
    const weakIso = params.weakIso ?? gauge.weakIso
    const chirality = params.chirality ?? gauge.chirality
    const spin = params.spin ?? gauge.spin
    const color = params.color ?? gauge.color

    particles.push({
        seedIndex,
        packetId,
        x: params.x,
        y: params.y,
        z: params.z ?? 0,
        vx: params.vx ?? (Math.random() - 0.5) * 0.18,
        vy: params.vy ?? (Math.random() - 0.5) * 0.18,
        vz: params.vz ?? (Math.random() - 0.5) * 0.004,
        theta,
        phaseTotal: theta,
        theta0: theta,
        sigma,
        sigmaTotal: sigma,
        sigma0: sigma,
        lens,
        nil,
        J: params.J ?? (mode === 1 || mode === 3 ? 0.28 : 0.7),
        coherence: params.coherence ?? (mode === 1 || mode === 3 ? 0.78 : 0.42),
        recurrence: params.recurrence ?? (mode === 1 || mode === 3 ? 0.22 : 0.02),
        neutrality: 0,
        pressure: 0,
        massLoad: params.massLoad ?? (mode === 1 || mode === 3 ? 0.36 : 0.16),
        properTime: 0,
        timeRate: 1,
        entanglementId: params.entanglementId ?? -1,
        entanglementPhase: params.entanglementPhase ?? 0,
        branchWeights: branchWeightsFromCarrier(theta, sigma, nil),
        measurement: params.measurement ?? (mode === 1 || mode === 3 ? 'anchored' : 'unresolved'),
        lastMeasuredFrame: params.lastMeasuredFrame ?? -999,
        smKind,
        electricCharge,
        hypercharge,
        weakIso,
        color,
        chirality,
        spin,
        gamma: 1,
        mode,
        age: 0,
        lastTurn: Math.floor(theta / TAU),
        lastSigmaTurn: Math.floor(sigma / TAU),
        radius: params.radius ?? 2.8,
    })

    const index = particles.length - 1
    wrapParticlePosition(particles[index])
    return index
}

function isChargedLeptonKind(kind: SmKind) {
    return kind === 'electron' || kind === 'positron' || kind === 'muon' || kind === 'antimuon'
}

function leptonMassLoad(kind: SmKind) {
    if (kind === 'muon' || kind === 'antimuon') return 0.62
    if (kind === 'neutrino' || kind === 'antineutrino') return 0.18
    if (kind === 'photon' || kind === 'gluon') return 0.08
    return 0.34
}

function antiparticleKind(kind: SmKind): SmKind {
    if (kind === 'electron') return 'positron'
    if (kind === 'positron') return 'electron'
    if (kind === 'muon') return 'antimuon'
    if (kind === 'antimuon') return 'muon'
    if (kind === 'neutrino') return 'antineutrino'
    if (kind === 'antineutrino') return 'neutrino'
    return kind
}

function spawnSingleSmParticle(kind: SmKind, site: { x: number, y: number, z: number }, options: { recoil?: boolean, phase?: number } = {}) {
    const seedIndex = nextSeedIndex()
    const theta = wrapAngle(options.phase ?? TAU * ((seedIndex * 0.38196601125) % 1))
    const sigma = wrapAngle(TAU * ((seedIndex * 0.61803398875) % 1) + (options.recoil ? Math.PI * 0.21 : 0))
    const gauge = smGaugeState(kind, seedIndex, theta, sigma)
    const mode: Mode = isQuarkKind(kind)
        ? 3
        : isChargedLeptonKind(kind) || kind === 'neutrino' || kind === 'antineutrino'
            ? 1
            : 0
    return pushManualParticle({
        seedIndex,
        smKind: kind,
        x: site.x,
        y: site.y,
        z: site.z + (options.recoil ? 0.16 : -0.08),
        theta,
        sigma,
        nil: smNilForKind(kind, theta, sigma),
        mode,
        coherence: kind === 'photon' || kind === 'gluon' ? 0.72 : 0.84,
        recurrence: kind === 'photon' ? 0.24 : mode === 1 || mode === 3 ? 0.3 : 0.12,
        J: kind === 'photon' ? 0.36 : mode === 1 || mode === 3 ? 0.22 : 0.44,
        massLoad: leptonMassLoad(kind),
        vx: options.recoil ? -Math.cos(theta) * 0.055 : Math.cos(theta) * 0.012,
        vy: options.recoil ? -Math.sin(theta) * 0.055 : Math.sin(theta) * 0.012,
        vz: 0,
        electricCharge: gauge.electricCharge,
        hypercharge: gauge.hypercharge,
        weakIso: gauge.weakIso,
        chirality: gauge.chirality,
        spin: gauge.spin,
        radius: kind === 'muon' || kind === 'antimuon' ? 3.4 : kind === 'photon' ? 3.1 : 2.8,
        measurement: isChargedLeptonKind(kind) ? 'unresolved' : undefined,
    })
}

function liveCapturePhotonCount() {
    let count = 0
    for (const particle of particles) {
        if (particle.smKind === 'photon' && particle.entanglementId === CAPTURE_PHOTON_ENTANGLEMENT_ID) count += 1
    }
    return count
}

function capturePhotonEmissionDirection(electron: ProtoParticle, center: { x: number, y: number, z: number }, nucleusVelocity: { vx: number, vy: number, vz: number }) {
    const relativeVx = electron.vx - nucleusVelocity.vx
    const relativeVy = electron.vy - nucleusVelocity.vy
    if (Math.hypot(relativeVx, relativeVy) > 0.035) return wrapAngle(Math.atan2(relativeVy, relativeVx))

    const radialX = wrappedOffset(electron.x - center.x, width)
    const radialY = wrappedOffset(electron.y - center.y, height)
    const spinTurn = Math.sin(signedAngle(electron.theta - electron.sigma)) >= 0 ? 1 : -1
    return wrapAngle(Math.atan2(radialY, radialX) + spinTurn * Math.PI * 0.5)
}

function emitCapturePhoton(origin: { x: number, y: number, z: number }, direction: number, energy: number, recoilGroup: number[], sourcePacketId: number) {
    if (energy <= 0.006 || liveCapturePhotonCount() >= MAX_CAPTURE_PHOTONS) return false

    const lastFrame = capturePhotonLastByPacket.get(sourcePacketId) ?? -999
    const cooldown = Math.max(120, Math.round(220 - settings.upperWorldCoupling * 42))
    if (frame - lastFrame < cooldown) return false
    capturePhotonLastByPacket.set(sourcePacketId, frame)

    const intensity = clamp01(energy * 1.35)
    const theta = wrapAngle(direction)
    const sigma = wrapAngle(direction * 0.61803398875 + Math.PI * 0.23)
    const speed = Math.min(5.15, 2.35 + Math.sqrt(Math.max(0, energy)) * 2.65)
    const photonIndex = pushManualParticle({
        smKind: 'photon',
        x: origin.x + Math.cos(direction) * 9,
        y: origin.y + Math.sin(direction) * 9,
        z: origin.z + Math.sin(sigma) * 0.08,
        theta,
        sigma,
        nil: -1,
        mode: 0,
        coherence: clamp01(0.6 + intensity * 0.34),
        recurrence: clamp01(0.2 + intensity * 0.32),
        J: clamp01(0.38 - intensity * 0.12),
        massLoad: 0.04 + intensity * 0.08,
        vx: Math.cos(direction) * speed,
        vy: Math.sin(direction) * speed,
        vz: Math.sin(sigma) * 0.08,
        radius: 2.5 + intensity * 2.2,
        measurement: 'unresolved',
        entanglementId: CAPTURE_PHOTON_ENTANGLEMENT_ID,
    })

    const recoil = Math.min(0.045, Math.sqrt(Math.max(0, energy)) * 0.012)
    const groupSize = Math.max(1, recoilGroup.length)
    for (const index of recoilGroup) {
        if (index === photonIndex) continue
        const particle = particles[index]
        if (!particle) continue
        const mass = Math.max(0.28, inertialMass(particle))
        particle.vx -= Math.cos(direction) * recoil / groupSize / mass
        particle.vy -= Math.sin(direction) * recoil / groupSize / mass
        particle.vz -= Math.sin(sigma) * recoil * 0.12 / groupSize / mass
    }

    emitProjectionEvent(particles[photonIndex], 48, 0.48 + intensity * 0.32)
    return true
}

function spawnConservedSmPair(kind: SmKind, site: { x: number, y: number, z: number }) {
    const partnerKind = antiparticleKind(kind)
    const angle = TAU * ((nextSeedIndex() * 0.754877666) % 1)
    spawnSingleSmParticle(kind, offsetPoint(site, 12, angle, -0.06), { phase: angle })
    if (partnerKind !== kind) {
        spawnSingleSmParticle(partnerKind, offsetPoint(site, 12, angle + Math.PI, 0.06), { recoil: true, phase: angle + Math.PI })
    }
}

function quarkFlavorSlot(flavor: QuarkFlavor, colorSlot: number) {
    return (flavor === 'up' ? 0 : 3) + colorSlot
}

function spawnChargeRecoil(site: { x: number, y: number, z: number }, charge: number, angle: number) {
    if (Math.abs(charge) < 0.001) return -1

    const theta = wrapAngle(angle + (charge > 0 ? 0.18 : Math.PI + 0.18))
    const sigma = wrapAngle(angle * 0.61803398875 + Math.PI * 0.37)
    return pushManualParticle({
        smKind: 'generic',
        x: site.x,
        y: site.y,
        z: site.z,
        electricCharge: charge,
        hypercharge: charge * 2,
        weakIso: 0,
        lens: charge > 0 ? 1 : -1,
        nil: basinFromCarrier(theta, sigma),
        mode: 1,
        theta,
        sigma,
        coherence: 0.74,
        recurrence: 0.18,
        J: 0.31,
        massLoad: 0.25 + Math.abs(charge) * 0.1,
        vx: -Math.cos(angle) * 0.07,
        vy: -Math.sin(angle) * 0.07,
        vz: 0,
        radius: 2.5,
    })
}

function spawnQuarkCarrier(site: { x: number, y: number, z: number }, flavor: QuarkFlavor, colorSlot = Math.max(0, nextSeedIndex()) % 3) {
    const seedBase = nextPacketSeedBase()
    const packetId = nextPacketId()
    const slot = quarkFlavorSlot(flavor, colorSlot)
    const seedIndex = seedBase + slot
    const smKind = smKindForSeed(seedIndex)
    const carrierAngle = TAU * colorSlot / 3 + (flavor === 'up' ? 0.14 : 0.47)
    const theta = wrapAngle(TAU * (slot / 24) + carrierAngle * 0.13)
    const sigma = wrapAngle(TAU * ((slot * 0.38196601125) % 1) + carrierAngle * 0.17)

    return pushManualParticle({
        seedIndex,
        packetId,
        smKind,
        x: site.x,
        y: site.y,
        z: site.z,
        theta,
        sigma,
        nil: smNilForKind(smKind, theta, sigma),
        mode: 3,
        coherence: 0.86,
        recurrence: 0.3,
        J: 0.24,
        massLoad: flavor === 'up' ? 0.4 : 0.42,
        entanglementId: packetId * 100 + 7,
        entanglementPhase: colorSlot * TAU / 3,
        vx: Math.cos(carrierAngle) * 0.05,
        vy: Math.sin(carrierAngle) * 0.05,
        vz: 0,
        radius: 2.7,
    })
}

function spawnConservedQuark(flavor: QuarkFlavor, site: { x: number, y: number, z: number }) {
    const colorSlot = Math.max(0, nextSeedIndex()) % 3
    const angle = TAU * colorSlot / 3 + (flavor === 'up' ? 0 : Math.PI / 3)
    const quarkIndex = spawnQuarkCarrier(offsetPoint(site, 10, angle, -0.05), flavor, colorSlot)
    const quark = particles[quarkIndex]
    spawnChargeRecoil(offsetPoint(site, 10, angle + Math.PI, 0.05), -quark.electricCharge, angle + Math.PI)
}

function spawnSmPacket(site: { x: number, y: number, z: number }, packetRadius = 0) {
    const packetId = nextPacketId()
    const seedBase = nextPacketSeedBase()
    const packetAngle = TAU * ((packetId * 0.38196601125) % 1)
    const packetSite = packetRadius > 0
        ? offsetPoint(site, packetRadius, packetAngle, Math.sin(packetAngle) * 0.08)
        : site
    const compact = 0.58

    for (let slot = 0; slot < 24; slot++) {
        const seedIndex = seedBase + slot
        const smKind = smKindForSeed(seedIndex)
        const theta = wrapAngle(TAU * (slot / 24) + packetAngle * 0.13)
        const sigma = wrapAngle(TAU * ((slot * 0.38196601125) % 1) + packetAngle * 0.17)
        let x = packetSite.x
        let y = packetSite.y
        let z = packetSite.z

        if (isQuarkKind(smKind)) {
            const colorAngle = TAU * (slot % 3) / 3 + packetAngle * 0.12
            x += Math.cos(colorAngle) * (12 + Math.floor(slot / 3) * 1.2) * compact + (Math.random() - 0.5) * 3
            y += Math.sin(colorAngle) * (12 + Math.floor(slot / 3) * 1.2) * compact + (Math.random() - 0.5) * 3
            z += (slot % 3 - 1) * 0.12 * compact
        } else if (smKind === 'electron' || smKind === 'positron') {
            const leptonAngle = packetAngle + (smKind === 'electron' ? -0.42 : 0.42) + (slot % 3) * 0.16
            x += Math.cos(leptonAngle) * 34 * compact + (Math.random() - 0.5) * 4
            y += Math.sin(leptonAngle) * 34 * compact + (Math.random() - 0.5) * 4
            z += (smKind === 'electron' ? -0.22 : 0.22) * compact
        } else if (smKind === 'neutrino') {
            x += (Math.random() - 0.5) * 36 * compact
            y += (Math.random() - 0.5) * 36 * compact
            z += Math.sin(packetAngle + slot) * 0.22 * compact
        } else {
            const waveAngle = TAU * ((slot * 0.754877666) % 1) + packetAngle
            const waveRadius = 44 + slot * 0.42
            x += Math.cos(waveAngle) * waveRadius * compact + (Math.random() - 0.5) * 8
            y += Math.sin(waveAngle) * waveRadius * compact + (Math.random() - 0.5) * 8
            z += Math.sin(waveAngle * 2) * 0.24 * compact
        }

        const nil = smNilForKind(smKind, theta, sigma)
        const mode: Mode = smKind === 'electron' || smKind === 'positron'
            ? 1
            : isQuarkKind(smKind)
                ? 3
                : smKind === 'neutrino'
                    ? 1
                    : 0
        const entanglementId = isQuarkKind(smKind)
            ? packetId * 100 + Math.floor(slot / 3)
            : smKind === 'electron' || smKind === 'positron'
                ? -1
                : packetId * 100 + 20 + Math.floor(slot / 6)

        pushManualParticle({
            seedIndex,
            packetId,
            smKind,
            x,
            y,
            z,
            theta,
            sigma,
            nil,
            mode,
            coherence: smKind === 'photon' || smKind === 'gluon' ? 0.68 : 0.86,
            recurrence: nil >= 0 ? 0.34 : 0.14,
            J: smKind === 'photon' || smKind === 'gluon' ? 0.4 : 0.24,
            entanglementId,
            entanglementPhase: entanglementId >= 0 ? wrapAngle((slot % 4) * Math.PI * 0.5) : 0,
            radius: 2.4 + Math.random() * 0.7,
            measurement: isChargedLeptonKind(smKind) ? 'unresolved' : undefined,
        })
    }
}

function isAtomicSpawnKind(kind: SpawnKind): kind is AtomicSpawnKind {
    return kind === 'hydrogen' || kind === 'deuterium' || kind === 'tritium' || kind === 'helium4'
}

function atomicSpawnSpec(kind: AtomicElementKind) {
    if (kind === 'deuterium') return { label: 'D', protons: 1, neutrons: 1, electrons: 1, shellRadius: 45 }
    if (kind === 'tritium') return { label: 'T', protons: 1, neutrons: 2, electrons: 1, shellRadius: 48 }
    if (kind === 'helium4') return { label: 'He', protons: 2, neutrons: 2, electrons: 2, shellRadius: 52 }
    if (kind === 'oxygen16') return { label: 'O', protons: 8, neutrons: 8, electrons: 8, shellRadius: 64 }
    return { label: 'H', protons: 1, neutrons: 0, electrons: 1, shellRadius: 42 }
}

function spawnBaryonCarrier(site: { x: number, y: number, z: number }, kind: NucleonKind, ordinal: number) {
    const seedBase = nextPacketSeedBase()
    const packetId = nextPacketId()
    const slots = kind === 'proton' ? [0, 1, 5] : [2, 3, 4]
    const entanglementId = packetId * 100 + ordinal
    const ids: number[] = []

    for (let i = 0; i < slots.length; i++) {
        const slot = slots[i]
        const seedIndex = seedBase + slot
        const smKind = smKindForSeed(seedIndex)
        const quarkAngle = TAU * i / 3 + ordinal * 0.47
        const theta = wrapAngle(TAU * (slot / 24) + ordinal * 0.31)
        const sigma = wrapAngle(TAU * ((slot * 0.38196601125) % 1) + ordinal * 0.19)
        const id = pushManualParticle({
            seedIndex,
            packetId,
            smKind,
            x: site.x + Math.cos(quarkAngle) * 4.6,
            y: site.y + Math.sin(quarkAngle) * 4.6,
            z: site.z + (i - 1) * 0.08,
            theta,
            sigma,
            nil: smNilForKind(smKind, theta, sigma),
            mode: 3,
            coherence: 0.9,
            recurrence: 0.38,
            J: 0.18,
            massLoad: kind === 'proton' ? 0.44 : 0.48,
            entanglementId,
            entanglementPhase: i * TAU / 3,
            vx: (Math.random() - 0.5) * 0.05,
            vy: (Math.random() - 0.5) * 0.05,
            vz: (Math.random() - 0.5) * 0.002,
            radius: 2.7,
        })
        ids.push(id)
    }

    return ids
}

function spawnFreeNucleon(kind: NucleonKind, site: { x: number, y: number, z: number }) {
    const ordinal = Math.max(1, nextSeedIndex())
    spawnBaryonCarrier(site, kind, ordinal)
}

function spawnBoundElectron(site: { x: number, y: number, z: number }, atomId: number, shellRadius: number, ordinal: number, moleculeId: number) {
    const angle = TAU * ((ordinal + 0.17) / Math.max(1, ordinal + 2)) + atomId * 0.013
    const theta = wrapAngle(angle + Math.PI * 0.35)
    const sigma = wrapAngle(angle * 0.61803398875 + Math.PI * 0.2)
    return pushManualParticle({
        packetId: atomId,
        smKind: 'electron',
        x: site.x + Math.cos(angle) * shellRadius,
        y: site.y + Math.sin(angle) * shellRadius * 0.72,
        z: site.z - 0.16 + (ordinal % 2) * 0.28,
        theta,
        sigma,
        nil: basinFromCarrier(theta, sigma),
        mode: 1,
        coherence: 0.88,
        recurrence: 0.32,
        J: 0.2,
        massLoad: 0.34,
        entanglementId: moleculeId + atomId + ordinal,
        entanglementPhase: ordinal * Math.PI,
        vx: -Math.sin(angle) * 0.08,
        vy: Math.cos(angle) * 0.08,
        vz: 0,
        radius: 2.8,
    })
}

function spawnStructuredAtom(kind: AtomicElementKind, site: { x: number, y: number, z: number }, moleculeId = -1) {
    const spec = atomicSpawnSpec(kind)
    const atomId = nextDeclaredAtomId++
    const nucleusIds: number[] = []
    const electronIds: number[] = []
    const nucleonCount = spec.protons + spec.neutrons
    const nucleusRadius = nucleonCount <= 1 ? 0 : 5.8 + nucleonCount * 1.15
    const declaredMoleculeId = moleculeId >= 0 ? moleculeId : atomId

    for (let i = 0; i < nucleonCount; i++) {
        const nucleonKind: NucleonKind = i < spec.protons ? 'proton' : 'neutron'
        const angle = nucleonCount <= 1 ? 0 : TAU * i / nucleonCount + atomId * 0.0017
        const nucleonSite = offsetPoint(site, nucleusRadius, angle, Math.sin(angle) * 0.05)
        nucleusIds.push(...spawnBaryonCarrier(nucleonSite, nucleonKind, atomId + i))
    }

    for (let i = 0; i < spec.electrons; i++) {
        electronIds.push(spawnBoundElectron(site, atomId, spec.shellRadius, i, declaredMoleculeId))
    }

    const atom: DeclaredAtom = {
        id: atomId,
        label: spec.label,
        protons: spec.protons,
        neutrons: spec.neutrons,
        nucleusIds,
        electronIds,
        bondIds: [],
        x: site.x,
        y: site.y,
        z: site.z,
        shellRadius: spec.shellRadius,
        moleculeId: declaredMoleculeId,
    }
    declaredAtoms.push(atom)
    return atom
}

function spawnHydrogenMolecule(site: { x: number, y: number, z: number }) {
    const moleculeId = nextDeclaredMoleculeId++
    const halfBond = 42
    const left = spawnStructuredAtom('hydrogen', offsetPoint(site, halfBond, Math.PI, -0.03), moleculeId)
    const right = spawnStructuredAtom('hydrogen', offsetPoint(site, halfBond, 0, 0.03), moleculeId)
    const bondId = nextDeclaredBondId++
    const bond: DeclaredBond = {
        id: bondId,
        label: 'H2',
        atomIds: [left.id, right.id],
        electronIds: [...left.electronIds, ...right.electronIds],
        restLength: halfBond * 2,
        order: 1,
        stability: 0.74,
        freeEnergy: 0,
        boundEnergy: 0,
        binding: 0,
        moleculeId,
    }
    declaredBonds.push(bond)
    left.bondIds.push(bondId)
    right.bondIds.push(bondId)
}

function createDeclaredBond(label: string, left: DeclaredAtom, right: DeclaredAtom, electronIds: number[], restLength: number, order: number, moleculeId: number) {
    const bondId = nextDeclaredBondId++
    const bond: DeclaredBond = {
        id: bondId,
        label,
        atomIds: [left.id, right.id],
        electronIds,
        restLength,
        order,
        stability: 0.62,
        freeEnergy: 0,
        boundEnergy: 0,
        binding: 0,
        moleculeId,
    }
    declaredBonds.push(bond)
    left.bondIds.push(bondId)
    right.bondIds.push(bondId)
    return bond
}

function spawnWaterMolecule(site: { x: number, y: number, z: number }, orientation = TAU * ((nextDeclaredMoleculeId * 0.38196601125) % 1)) {
    const moleculeId = nextDeclaredMoleculeId++
    const bondLength = 62
    const halfAngle = 104.5 * Math.PI / 360
    const oxygen = spawnStructuredAtom('oxygen16', site, moleculeId)
    const leftAngle = orientation + Math.PI + halfAngle
    const rightAngle = orientation + Math.PI - halfAngle
    const leftHydrogen = spawnStructuredAtom('hydrogen', offsetPoint(site, bondLength, leftAngle, -0.06), moleculeId)
    const rightHydrogen = spawnStructuredAtom('hydrogen', offsetPoint(site, bondLength, rightAngle, 0.06), moleculeId)

    createDeclaredBond('O-H', oxygen, leftHydrogen, [
        oxygen.electronIds[0],
        oxygen.electronIds[2],
        ...leftHydrogen.electronIds,
    ].filter(index => particles[index]), bondLength, 1, moleculeId)
    createDeclaredBond('O-H', oxygen, rightHydrogen, [
        oxygen.electronIds[1],
        oxygen.electronIds[3],
        ...rightHydrogen.electronIds,
    ].filter(index => particles[index]), bondLength, 1, moleculeId)

    return { moleculeId, oxygen, leftHydrogen, rightHydrogen }
}

function spawnWaterCluster(site: { x: number, y: number, z: number }) {
    const count = 6
    const spacing = 150
    const waters: WaterMolecule[] = []
    const clusterId = nextDeclaredMoleculeId++
    for (let i = 0; i < count; i++) {
        const angle = TAU * i / count
        const ring = offsetPoint(site, spacing, angle, Math.sin(angle * 2) * 0.08)
        waters.push(spawnWaterMolecule(ring, angle + Math.PI * 0.5))
    }

    for (let i = 0; i < waters.length; i++) {
        const donor = waters[i]
        const acceptor = waters[(i + 1) % waters.length]
        createDeclaredBond('H...O', donor.rightHydrogen, acceptor.oxygen, [
            donor.rightHydrogen.electronIds[0],
            acceptor.oxygen.electronIds[4 + (i % 4)],
        ].filter(index => particles[index]), spacing * 0.72, 0.35, clusterId)
    }
}

function refreshManualWorld() {
    manualEmptyWorld = false
    orbitalSamples = []
    physicsEnergyBaseline = null
    physicsEnergyBaselineWarmupUntil = frame + 72
    metrics.netCharge = totalElectricCharge()
    buildAtomComposites()
    applyMttClosureGradient()
    collectOrbitalSamples()
    captureInvariantBaseline()
}

function addEntity(kind: SpawnKind) {
    const site = spawnSite()

    if (kind !== 'primitive') activePreset.value = 'sm'

    if (kind === 'primitive') {
        pushManualParticle({
            x: site.x,
            y: site.y,
            z: site.z,
            lens: 0,
            nil: -1,
            mode: 0,
            coherence: 0.38,
            recurrence: 0.02,
            J: 0.72,
        })
    } else if (kind === 'positive' || kind === 'negative') {
        const charge = kind === 'positive' ? 1 : -1
        const theta = wrapAngle(TAU * Math.random())
        const sigma = wrapAngle(TAU * Math.random())
        const partnerTheta = wrapAngle(theta + Math.PI)
        const partnerSigma = wrapAngle(sigma + Math.PI * 0.5)
        pushManualParticle({
            x: site.x - 11,
            y: site.y,
            z: site.z,
            electricCharge: charge,
            hypercharge: charge * 2,
            weakIso: 0,
            lens: charge > 0 ? 1 : -1,
            nil: basinFromCarrier(theta, sigma),
            mode: 1,
            theta,
            sigma,
            coherence: 0.8,
            recurrence: 0.24,
            J: 0.26,
            massLoad: 0.34,
        })
        pushManualParticle({
            x: site.x + 11,
            y: site.y,
            z: site.z + 0.06,
            electricCharge: -charge,
            hypercharge: -charge * 2,
            weakIso: 0,
            lens: charge > 0 ? -1 : 1,
            nil: basinFromCarrier(partnerTheta, partnerSigma),
            mode: 1,
            theta: partnerTheta,
            sigma: partnerSigma,
            coherence: 0.8,
            recurrence: 0.24,
            J: 0.26,
            massLoad: 0.34,
            vx: charge > 0 ? -0.05 : 0.05,
            vy: 0.02,
        })
    } else if (kind === 'electron') {
        spawnSingleSmParticle('electron', site)
    } else if (kind === 'electronPair') {
        spawnConservedSmPair('electron', site)
    } else if (kind === 'positron') {
        spawnConservedSmPair('positron', site)
    } else if (kind === 'muon') {
        spawnConservedSmPair('muon', site)
    } else if (kind === 'antimuon') {
        spawnConservedSmPair('antimuon', site)
    } else if (kind === 'neutrino') {
        spawnConservedSmPair('neutrino', site)
    } else if (kind === 'antineutrino') {
        spawnConservedSmPair('antineutrino', site)
    } else if (kind === 'photon') {
        spawnSingleSmParticle('photon', site)
    } else if (kind === 'upQuark') {
        spawnConservedQuark('up', site)
    } else if (kind === 'downQuark') {
        spawnConservedQuark('down', site)
    } else if (kind === 'proton') {
        spawnFreeNucleon('proton', site)
    } else if (kind === 'neutron') {
        spawnFreeNucleon('neutron', site)
    } else if (kind === 'atom') {
        spawnSmPacket(site)
    } else if (kind === 'bigAtom') {
        const clusterCount = 4
        for (let i = 0; i < clusterCount; i++) {
            const angle = TAU * i / clusterCount
            spawnSmPacket(offsetPoint(site, 26, angle, Math.sin(angle) * 0.06))
        }
    } else if (isAtomicSpawnKind(kind)) {
        layerView.value = 'atom'
        spawnStructuredAtom(kind, site)
    } else if (kind === 'h2') {
        layerView.value = 'atom'
        spawnHydrogenMolecule(site)
    } else if (kind === 'water') {
        layerView.value = 'atom'
        spawnWaterMolecule(site)
    } else {
        layerView.value = 'atom'
        spawnWaterCluster(site)
    }

    refreshManualWorld()
}

function energyPulseCenter() {
    if (lookingGlass.x !== 0 || lookingGlass.y !== 0) {
        return { x: lookingGlass.x, y: lookingGlass.y, z: 0 }
    }
    const center = screenToWorld(viewportWidth * 0.5, viewportHeight * 0.5)
    return { x: center.x, y: center.y, z: 0 }
}

function addEnergyPulse() {
    if (particles.length === 0) return
    if (!isSmPreset()) activePreset.value = 'sm'

    const center = energyPulseCenter()
    const pulseRadius = Math.max(160, Math.min(width, height) * 0.2)
    const touched: Array<{ index: number, mass: number }> = []
    let totalMass = 0
    let totalPx = 0
    let totalPy = 0
    let totalPz = 0
    let deposited = 0
    const candidates: Array<{ index: number, distance: number }> = []

    for (let i = 0; i < particles.length; i++) {
        const p = particles[i]
        const dx = wrappedOffset(p.x - center.x, width)
        const dy = wrappedOffset(p.y - center.y, height)
        const dz = p.z - center.z
        const distance = Math.hypot(dx, dy, dz * projectionDepthScale())
        candidates.push({ index: i, distance })
    }

    candidates.sort((a, b) => a.distance - b.distance)
    const fallbackLimit = Math.min(96, Math.max(12, Math.ceil(particles.length * 0.18)))

    for (const candidate of candidates) {
        const i = candidate.index
        const p = particles[i]
        const distance = candidate.distance
        const dx = wrappedOffset(p.x - center.x, width)
        const dy = wrappedOffset(p.y - center.y, height)
        const inRadius = distance <= pulseRadius
        if (!inRadius && touched.length >= fallbackLimit) continue

        const mass = inertialMass(p)
        const falloff = inRadius ? 1 - distance / pulseRadius : 0.18 * (1 - touched.length / Math.max(1, fallbackLimit))
        const strength = falloff * falloff * (0.9 + settings.sourceCoupling * 0.22 + settings.upperWorldCoupling * 0.12)
        const radial = Math.atan2(dy, dx)
        const twist = Math.sin(p.theta + p.sigma + frame * 0.013) >= 0 ? 1 : -1
        const kickAngle = radial + twist * Math.PI * 0.42
        const kick = strength / Math.sqrt(mass)
        const dvx = Math.cos(kickAngle) * kick
        const dvy = Math.sin(kickAngle) * kick
        const dvz = Math.sin(p.sigma + frame * 0.017) * kick * 0.12

        p.vx += dvx
        p.vy += dvy
        p.vz += dvz
        p.pressure = clamp01(p.pressure + strength * 0.16)
        p.J = clamp01(p.J + strength * 0.055)
        p.coherence = clamp01(p.coherence - strength * 0.018)
        p.phaseTotal += strength * 0.035 * twist
        p.sigmaTotal += strength * 0.024 * -twist
        p.theta = wrapAngle(p.phaseTotal)
        p.sigma = wrapAngle(p.sigmaTotal)

        totalMass += mass
        totalPx += mass * dvx
        totalPy += mass * dvy
        totalPz += mass * dvz
        deposited += 0.5 * mass * (dvx * dvx + dvy * dvy + dvz * dvz)
        touched.push({ index: i, mass })
        if (touched.length < 32) emitProjectionEvent(p, 34, 0.5 + strength * 0.3)
    }

    if (touched.length > 1 && totalMass > 0) {
        const correctionX = totalPx / totalMass
        const correctionY = totalPy / totalMass
        const correctionZ = totalPz / totalMass
        for (const item of touched) {
            const p = particles[item.index]
            p.vx -= correctionX
            p.vy -= correctionY
            p.vz -= correctionZ
        }
    }

    energyPulseResidue += deposited
    metrics.energyInput = energyPulseResidue
}

function isSmPreset() {
    return activePreset.value === 'sm' || activePreset.value === 'oneAtom'
}

function presetIsSmSeed(preset: PresetId) {
    return preset === 'sm' || preset === 'oneAtom'
}

function smKindForSeed(index: number): SmKind {
    const slot = index % 24
    if (slot < 9) {
        const color = slot % 3
        if (color === 0) return 'quarkR'
        if (color === 1) return 'quarkG'
        return 'quarkB'
    }
    if (slot < 12) return 'electron'
    if (slot < 15) return 'positron'
    if (slot < 18) return 'neutrino'
    if (slot < 22) return 'photon'
    return 'gluon'
}

function lensForSmKind(kind: SmKind, fallback: -1 | 0 | 1): -1 | 0 | 1 {
    if (kind === 'electron' || kind === 'muon') return -1
    if (kind === 'positron' || kind === 'antimuon') return 1
    if (kind === 'neutrino' || kind === 'antineutrino' || kind === 'photon' || kind === 'gluon') return 0
    if (kind === 'quarkR' || kind === 'quarkG' || kind === 'quarkB') return fallback === 0 ? 1 : fallback
    return fallback
}

function smNilForKind(kind: SmKind, theta: number, sigma: number): -1 | 0 | 1 | 2 {
    if (kind === 'quarkR') return 0
    if (kind === 'quarkG') return 1
    if (kind === 'quarkB') return 2
    if (kind === 'electron' || kind === 'positron' || kind === 'muon' || kind === 'antimuon') return basinFromCarrier(theta, sigma)
    if (kind === 'neutrino') return basinFromCarrier(theta + Math.PI / 3, sigma)
    if (kind === 'antineutrino') return basinFromCarrier(theta - Math.PI / 3, sigma)
    return -1
}

function smColor(kind: SmKind, alpha = 1) {
    if (kind === 'electron') return `rgba(103, 232, 249, ${alpha})`
    if (kind === 'positron') return `rgba(251, 113, 133, ${alpha})`
    if (kind === 'muon') return `rgba(34, 211, 238, ${alpha})`
    if (kind === 'antimuon') return `rgba(244, 114, 182, ${alpha})`
    if (kind === 'neutrino') return `rgba(165, 180, 252, ${alpha})`
    if (kind === 'antineutrino') return `rgba(196, 181, 253, ${alpha})`
    if (kind === 'quarkR') return `rgba(239, 68, 68, ${alpha})`
    if (kind === 'quarkG') return `rgba(34, 197, 94, ${alpha})`
    if (kind === 'quarkB') return `rgba(59, 130, 246, ${alpha})`
    if (kind === 'photon') return `rgba(253, 230, 138, ${alpha})`
    if (kind === 'gluon') return `rgba(192, 132, 252, ${alpha})`
    return `rgba(150, 177, 205, ${alpha})`
}

function smHue(kind: SmKind) {
    if (kind === 'electron') return 186
    if (kind === 'positron') return 350
    if (kind === 'muon') return 190
    if (kind === 'antimuon') return 328
    if (kind === 'neutrino') return 235
    if (kind === 'antineutrino') return 260
    if (kind === 'quarkR') return 0
    if (kind === 'quarkG') return 142
    if (kind === 'quarkB') return 217
    if (kind === 'photon') return 48
    if (kind === 'gluon') return 270
    return 205
}

function isQuarkKind(kind: SmKind) {
    return kind === 'quarkR' || kind === 'quarkG' || kind === 'quarkB'
}

function isQuarkBindingPair(a: ProtoParticle, b: ProtoParticle) {
    return isQuarkKind(a.smKind) && isQuarkKind(b.smKind) && a.entanglementId >= 0 && a.entanglementId === b.entanglementId
}

function isFermionKind(kind: SmKind) {
    return isQuarkKind(kind) || kind === 'electron' || kind === 'positron' || kind === 'muon' || kind === 'antimuon' || kind === 'neutrino' || kind === 'antineutrino'
}

function isRecentlyMeasuredChargedLepton(p: ProtoParticle) {
    return isChargedLeptonKind(p.smKind) && p.measurement !== 'unresolved' && frame - p.lastMeasuredFrame < 96
}

function isUnmeasuredChargedCloud(p: ProtoParticle) {
    return isSmPreset() && isChargedLeptonKind(p.smKind) && !isRecentlyMeasuredChargedLepton(p)
}

function colorForSmKind(kind: SmKind): GaugeColor {
    if (kind === 'quarkR') return 'red'
    if (kind === 'quarkG') return 'green'
    if (kind === 'quarkB') return 'blue'
    return 'none'
}

function smQuarkFlavorSlot(index: number) {
    return Math.floor((index % 24) / 3)
}

function smElectricCharge(kind: SmKind, index: number) {
    if (kind === 'electron') return -1
    if (kind === 'positron') return 1
    if (kind === 'muon') return -1
    if (kind === 'antimuon') return 1
    if (kind === 'neutrino' || kind === 'antineutrino' || kind === 'photon' || kind === 'gluon') return 0
    if (isQuarkKind(kind)) return smQuarkFlavorSlot(index) === 0 ? 2 / 3 : -1 / 3
    return 0
}

function smChirality(kind: SmKind, theta: number, sigma: number): Chirality {
    if (!isFermionKind(kind)) return 'R'
    if (kind === 'neutrino') return 'L'
    if (kind === 'antineutrino') return 'R'
    return Math.cos(theta + sigma * 0.5) >= -0.18 ? 'L' : 'R'
}

function smWeakIso(kind: SmKind, index: number, chirality: Chirality) {
    if (chirality === 'R') return 0
    if (kind === 'neutrino') return 0.5
    if (kind === 'electron' || kind === 'muon') return -0.5
    if (kind === 'positron' || kind === 'antimuon') return 0.5
    if (isQuarkKind(kind)) return smQuarkFlavorSlot(index) === 0 ? 0.5 : -0.5
    return 0
}

function smGaugeState(kind: SmKind, index: number, theta: number, sigma: number) {
    const electricCharge = smElectricCharge(kind, index)
    const chirality = smChirality(kind, theta, sigma)
    const weakIso = smWeakIso(kind, index, chirality)
    const hypercharge = chirality === 'L' ? 2 * (electricCharge - weakIso) : 2 * electricCharge
    const spin = kind === 'photon' || kind === 'gluon'
        ? 1
        : isFermionKind(kind)
            ? (Math.sin(theta + sigma) >= 0 ? 0.5 : -0.5)
            : 0

    return {
        electricCharge,
        hypercharge,
        weakIso,
        color: colorForSmKind(kind),
        chirality,
        spin,
    }
}

function colorIndex(color: GaugeColor) {
    if (color === 'red') return 0
    if (color === 'green') return 1
    if (color === 'blue') return 2
    return -1
}

function mttGaugeBranch(p: ProtoParticle) {
    return p.nil >= 0 ? p.nil : basinFromCarrier(p.theta, p.sigma)
}

function mttChiralOrientation(p: ProtoParticle) {
    return Math.cos(p.theta + p.sigma * 0.5) >= -0.18 ? 1 : -1
}

function mttGaugeConstraintForce(a: ProtoParticle, b: ProtoParticle, phaseDelta: number, sigmaDelta: number, closeness: number) {
    if (!isSmPreset()) return 0

    let force = 0
    const locality = closeness * closeness
    const phaseTransport = clamp01((1 + Math.cos(phaseDelta)) * 0.5)
    const sigmaTransport = clamp01((1 + Math.cos(sigmaDelta)) * 0.5)
    const transportQuality = phaseTransport * 0.64 + sigmaTransport * 0.36
    const aLens = a.lens
    const bLens = b.lens

    if (aLens !== 0 && bLens !== 0) {
        force += -0.24 * aLens * bLens * transportQuality * locality
    }

    const aBranch = mttGaugeBranch(a)
    const bBranch = mttGaugeBranch(b)
    const sameSource = a.entanglementId >= 0 && a.entanglementId === b.entanglementId
    const tripletEligible = a.mode === 3 && b.mode === 3
    if (tripletEligible) {
        const branchComplement = aBranch !== bBranch ? 1 : -1
        const sourceGain = sameSource ? 1 : 0.16
        force += branchComplement * sourceGain * (0.46 + transportQuality * 0.18) * locality
    }

    const chiralA = mttChiralOrientation(a)
    const chiralB = mttChiralOrientation(b)
    const neutralTransport = aLens === 0 && bLens === 0 && chiralA === chiralB
    if (neutralTransport) {
        force += 0.08 * transportQuality * locality
    }

    return force * settings.sourceCoupling
}

function mttGaugeConstraintTorque(a: ProtoParticle, b: ProtoParticle, phaseDelta: number, sigmaDelta: number, closeness: number) {
    if (!isSmPreset()) return { phase: 0, sigma: 0 }

    const locality = closeness * closeness
    const branchTwist = Math.sin((mttGaugeBranch(a) - mttGaugeBranch(b)) * TAU / 3)
    const lensTwist = (a.lens - b.lens) * Math.PI / 3
    const chiralTwist = (mttChiralOrientation(a) - mttChiralOrientation(b)) * Math.PI / 4

    return {
        phase: Math.sin(phaseDelta + chiralTwist + branchTwist * 0.28) * locality * settings.sourceCoupling * 0.08,
        sigma: Math.sin(sigmaDelta + lensTwist + branchTwist * 0.42) * locality * settings.sourceCoupling * 0.012,
    }
}

function mttOccupancyCellSize(p: ProtoParticle) {
    return Math.max(12, mttClosureCellRadius(p) * 1.18)
}

function mttOccupancyCellKey(p: ProtoParticle) {
    const cellSize = mttOccupancyCellSize(p)
    const branch = p.nil >= 0 ? p.nil : basinFromCarrier(p.theta, p.sigma)
    const chargeSlot = Math.round(p.electricCharge * 3)
    const xCell = Math.floor(p.x / cellSize)
    const yCell = Math.floor(p.y / cellSize)
    const zStep = Math.max(0.24, 0.64 / Math.max(0.6, settings.upperWorldCoupling))
    const zCell = Math.floor((p.z + 1.5) / zStep)
    return `${p.smKind}:${chargeSlot}:${p.lens}:${branch}:${xCell}:${yCell}:${zCell}`
}

function mttSpinorStateOverlap(a: ProtoParticle, b: ProtoParticle, phaseDelta = signedAngle(b.theta - a.theta), sigmaDelta = signedAngle(b.sigma - a.sigma)) {
    if (!isFermionKind(a.smKind) || a.smKind !== b.smKind) return 0

    const sameCharge = Math.abs(a.electricCharge - b.electricCharge) < 0.001
    if (!sameCharge) return 0

    const spinOverlap = Math.sign(a.spin) === Math.sign(b.spin) ? 1 : 0.08
    const chiralityOverlap = a.chirality === b.chirality ? 1 : 0.38
    const nilOverlap = a.nil >= 0 && b.nil >= 0 && a.nil === b.nil ? 1 : 0.48
    const phaseOverlap = (1 + Math.cos(phaseDelta)) * 0.5
    const sigmaOverlap = (1 + Math.cos(sigmaDelta)) * 0.5

    return clamp01((phaseOverlap * 0.58 + sigmaOverlap * 0.42) * spinOverlap * chiralityOverlap * nilOverlap)
}

function buildMttOccupancyState(n: number): MttOccupancyState {
    const costs = new Float32Array(n)
    const cellKeys = Array.from({ length: n }, () => '')
    const cells = new Map<string, MttOccupancyCell>()

    for (let i = 0; i < n; i++) {
        const p = particles[i]
        if (!isFermionKind(p.smKind)) continue

        const key = mttOccupancyCellKey(p)
        cellKeys[i] = key
        let cell = cells.get(key)
        if (!cell) {
            cell = { key, indices: [], x: 0, y: 0, z: 0 }
            cells.set(key, cell)
        }
        cell.indices.push(i)
        cell.x += p.x
        cell.y += p.y
        cell.z += p.z
    }

    let activeCells = 0
    let totalCost = 0
    let costCount = 0

    for (const cell of cells.values()) {
        const count = cell.indices.length
        if (count === 0) continue
        cell.x /= count
        cell.y /= count
        cell.z /= count
        if (count < 2) continue

        let cellConflict = 0
        for (let aSlot = 0; aSlot < count; aSlot++) {
            const aIndex = cell.indices[aSlot]
            const a = particles[aIndex]
            for (let bSlot = aSlot + 1; bSlot < count; bSlot++) {
                const bIndex = cell.indices[bSlot]
                const b = particles[bIndex]
                const overlap = mttSpinorStateOverlap(a, b)
                if (overlap <= 0.08) continue
                const conflict = clamp01((overlap - 0.08) / 0.92)
                costs[aIndex] += conflict
                costs[bIndex] += conflict
                cellConflict += conflict
            }
        }

        if (cellConflict > 0) activeCells += 1
    }

    for (let i = 0; i < n; i++) {
        const cost = clamp01(costs[i] * 0.42)
        costs[i] = cost
        if (cost > 0) {
            totalCost += cost
            costCount += 1
        }
    }

    return {
        costs,
        cellKeys,
        cells,
        activeCells,
        meanCost: costCount > 0 ? totalCost / costCount : 0,
    }
}

function mttOccupancyPairForce(state: MttOccupancyState, i: number, j: number, a: ProtoParticle, b: ProtoParticle, phaseDelta: number, sigmaDelta: number, closeness: number) {
    if (!state.cellKeys[i] || state.cellKeys[i] !== state.cellKeys[j]) return 0

    const overlap = mttSpinorStateOverlap(a, b, phaseDelta, sigmaDelta)
    if (overlap <= 0.08) return 0

    const cellCost = Math.max(state.costs[i], state.costs[j])
    return -0.2 * settings.capacity * settings.sourceCoupling * closeness * closeness * clamp01(overlap * 0.65 + cellCost * 0.35)
}

function applyMttOccupancyClosureForces(state: MttOccupancyState, fx: Float32Array, fy: Float32Array, fz: Float32Array, depthScale: number) {
    if (state.activeCells === 0) return

    for (const cell of state.cells.values()) {
        if (cell.indices.length < 2) continue
        for (const index of cell.indices) {
            const cost = state.costs[index]
            if (cost <= 0.001) continue
            const p = particles[index]
            let dx = wrappedOffset(p.x - cell.x, width)
            let dy = wrappedOffset(p.y - cell.y, height)
            let dz = p.z - cell.z
            let distance = Math.hypot(dx, dy, dz * depthScale)
            if (distance < 0.5) {
                dx = Math.cos(p.theta)
                dy = Math.sin(p.theta)
                dz = Math.sin(p.sigma) / depthScale
                distance = Math.max(0.5, Math.hypot(dx, dy, dz * depthScale))
            }
            const force = cost * (0.09 + settings.capacity * 0.035) * settings.sourceCoupling
            fx[index] += dx / distance * force
            fy[index] += dy / distance * force
            fz[index] += dz / distance * force
        }
    }
}

function smClosureSupport(p: ProtoParticle, group?: EntanglementSummary) {
    if (!isSmPreset()) return 0
    let support = 0
    if (isQuarkKind(p.smKind) && group && group.count >= 3) support += 0.08 * group.coherence
    if (p.smKind === 'photon' && Math.abs(p.electricCharge) < 0.001) support += 0.04
    if (p.smKind === 'neutrino' && p.chirality === 'L') support += 0.05
    if (p.smKind === 'antineutrino' && p.chirality === 'R') support += 0.05
    if (isFermionKind(p.smKind) && Math.abs(p.electricCharge - (p.weakIso + p.hypercharge / 2)) < 0.001) support += 0.05
    return support
}

function computeColorClosureStats(): ColorClosureStats {
    if (!isSmPreset()) return { groups: 0, closed: 0, closure: 0 }

    const groups = new Map<number, [number, number, number]>()
    let quarkGroups = 0
    let closed = 0

    for (const p of particles) {
        if (!isQuarkKind(p.smKind) || p.entanglementId < 0) continue
        const counts = groups.get(p.entanglementId) ?? [0, 0, 0]
        if (p.color === 'red') counts[0] += 1
        else if (p.color === 'green') counts[1] += 1
        else if (p.color === 'blue') counts[2] += 1
        groups.set(p.entanglementId, counts)
    }

    for (const counts of groups.values()) {
        const total = counts[0] + counts[1] + counts[2]
        if (total < 3) continue
        quarkGroups += 1
        const balanced = Math.min(counts[0], counts[1], counts[2]) / Math.max(1, Math.max(counts[0], counts[1], counts[2]))
        if (balanced > 0.66) closed += 1
    }

    return {
        groups: quarkGroups,
        closed,
        closure: quarkGroups > 0 ? closed / quarkGroups : 0,
    }
}

function computeColorClosure() {
    return computeColorClosureStats().closure
}

function smProjectorTarget(p: ProtoParticle): -1 | 0 | 1 | 2 {
    if (p.smKind === 'quarkR') return 0
    if (p.smKind === 'quarkG') return 1
    if (p.smKind === 'quarkB') return 2
    return -1
}

function enforceSmProjector(p: ProtoParticle) {
    if (!isSmPreset()) return

    const target = smProjectorTarget(p)
    if (target >= 0) p.nil = target
}

function totalElectricCharge() {
    return particles.reduce((sum, p) => sum + p.electricCharge, 0)
}

function captureInvariantBaseline() {
    invariantState.baselineCharge = isSmPreset() ? totalElectricCharge() : 0
    computeSmInvariants()
}

function computeSmInvariants() {
    if (!isSmPreset() || particles.length === 0) {
        invariantState.chargeDrift = 0
        invariantState.qIdentity = 1
        invariantState.colorClosure = 0
        invariantState.colorGroups = 0
        invariantState.chiralityRule = 1
        invariantState.mediatorRule = 1
        invariantState.projectorRule = 1
        invariantState.mttClosureSamples = 0
        invariantState.mttClosureCost = 0
        invariantState.mttPhaseReturn = 1
        invariantState.mttNilBudget = 1
        invariantState.mttLensBalance = 1
        invariantState.mttWindingReturn = 1
        return
    }

    const colorStats = computeColorClosureStats()
    let qIdentityPass = 0
    let chiralityPass = 0
    let mediatorPass = 0
    let mediatorCount = 0
    let projectorPass = 0
    let phaseReturnSum = 0
    let nilBudgetSum = 0
    let lensBalanceSum = 0
    let windingReturnSum = 0

    for (const p of particles) {
        const expectedQ = p.weakIso + p.hypercharge / 2
        if (Math.abs(p.electricCharge - expectedQ) < 0.001) qIdentityPass += 1

        const chiralityOk = !isFermionKind(p.smKind)
            || (p.smKind === 'neutrino' && p.chirality === 'L')
            || (p.smKind === 'antineutrino' && p.chirality === 'R')
            || (p.chirality === 'R' && Math.abs(p.weakIso) < 0.001)
            || (p.chirality === 'L' && Math.abs(p.weakIso) > 0.001)
        if (chiralityOk) chiralityPass += 1

        if (p.smKind === 'photon' || p.smKind === 'gluon') {
            mediatorCount += 1
            const mediatorOk = p.mode === 0
                && p.spin === 1
                && Math.abs(p.electricCharge) < 0.001
                && Math.abs(p.weakIso) < 0.001
                && Math.abs(p.hypercharge) < 0.001
                && p.color === 'none'
            if (mediatorOk) mediatorPass += 1
        }

        const projectorTarget = smProjectorTarget(p)
        const projectorOk = projectorTarget >= 0
            ? p.nil === projectorTarget && p.mode === 3 && colorIndex(p.color) === projectorTarget
            : p.smKind === 'electron' || p.smKind === 'muon'
                ? p.lens === -1 && p.mode === 1
                : p.smKind === 'positron' || p.smKind === 'antimuon'
                    ? p.lens === 1 && p.mode === 1
                    : p.smKind === 'neutrino'
                        ? p.electricCharge === 0 && p.chirality === 'L'
                        : p.smKind === 'antineutrino'
                            ? p.electricCharge === 0 && p.chirality === 'R'
                            : p.smKind === 'photon' || p.smKind === 'gluon'
                                ? p.mode === 0
                                : true
        if (projectorOk) projectorPass += 1

        const thetaTurnError = Math.abs(p.phaseTotal / TAU - Math.round(p.phaseTotal / TAU))
        const sigmaTurnError = Math.abs(p.sigmaTotal / TAU - Math.round(p.sigmaTotal / TAU))
        const returnWindow = 1 - clamp01(thetaTurnError + sigmaTurnError)
        phaseReturnSum += clamp01(p.recurrence * 0.58 + (1 - p.J) * 0.32 + returnWindow * 0.1)

        const carrierBranch = basinFromCarrier(p.theta, p.sigma)
        const nilScore = p.nil === -1
            ? 0.55
            : p.nil === carrierBranch
                ? 1
                : 0.25
        nilBudgetSum += nilScore

        const lensScore = p.smKind === 'electron'
            ? (p.lens === -1 ? 1 : 0.1)
            : p.smKind === 'positron'
                ? (p.lens === 1 ? 1 : 0.1)
                : p.smKind === 'muon'
                    ? (p.lens === -1 ? 1 : 0.1)
                    : p.smKind === 'antimuon'
                        ? (p.lens === 1 ? 1 : 0.1)
                        : p.smKind === 'neutrino' || p.smKind === 'antineutrino' || p.smKind === 'photon' || p.smKind === 'gluon'
                    ? (p.lens === 0 ? 1 : 0.45)
                    : isQuarkKind(p.smKind)
                        ? (p.lens !== 0 ? 1 : 0.55)
                        : 1
        lensBalanceSum += lensScore

        let dx = wrappedOffset(p.x - geometry.x, width)
        let dy = wrappedOffset(p.y - geometry.y, height)
        const planarDistance = Math.max(1, Math.hypot(dx, dy))
        const radialFlow = Math.abs((dx * p.vx + dy * p.vy) / planarDistance)
        const tangentialFlow = Math.abs((dx * p.vy - dy * p.vx) / planarDistance)
        windingReturnSum += clamp01(tangentialFlow / (tangentialFlow + radialFlow + 0.18) * 0.64 + p.recurrence * 0.36)
    }

    invariantState.chargeDrift = totalElectricCharge() - invariantState.baselineCharge
    invariantState.qIdentity = qIdentityPass / Math.max(1, particles.length)
    invariantState.colorClosure = colorStats.closure
    invariantState.colorGroups = colorStats.groups
    invariantState.chiralityRule = chiralityPass / Math.max(1, particles.length)
    invariantState.mediatorRule = mediatorCount > 0 ? mediatorPass / mediatorCount : 1
    invariantState.projectorRule = projectorPass / Math.max(1, particles.length)
    invariantState.mttPhaseReturn = phaseReturnSum / Math.max(1, particles.length)
    invariantState.mttNilBudget = nilBudgetSum / Math.max(1, particles.length)
    invariantState.mttLensBalance = lensBalanceSum / Math.max(1, particles.length)
    invariantState.mttWindingReturn = windingReturnSum / Math.max(1, particles.length)
}

function particleSlot(p: ProtoParticle) {
    return p.seedIndex % 24
}

function packetMemberBySlot(packet: number[], slot: number) {
    return packet.find(index => particleSlot(particles[index]) === slot) ?? -1
}

function wrappedDistance2(a: ProtoParticle, b: ProtoParticle) {
    let dx = b.x - a.x
    let dy = b.y - a.y
    if (dx > width * 0.5) dx -= width
    else if (dx < -width * 0.5) dx += width
    if (dy > height * 0.5) dy -= height
    else if (dy < -height * 0.5) dy += height
    const dz = (b.z - a.z) * projectionDepthScale()
    return dx * dx + dy * dy + dz * dz
}

function mttVacuumExpectation(p: ProtoParticle) {
    const nilLock = p.nil >= 0 ? 0.14 : 0
    const lensLock = Math.abs(p.lens) * 0.08
    const depthLock = clamp01(1 - Math.abs(p.z) / 1.4) * 0.08
    return clamp01(0.16
        + (1 - p.J) * 0.28
        + p.coherence * 0.2
        + p.recurrence * 0.16
        + nilLock
        + lensLock
        + depthLock)
}

function inertialMass(p: ProtoParticle) {
    const vev = mttVacuumExpectation(p)
    const excitationLoad = p.massLoad * (0.74 + vev * 0.86)
    const stressLoad = p.pressure * 0.22 + p.J * 0.08
    return Math.max(0.16, 0.22 + vev * (0.56 + settings.sourceCoupling * 0.12) + excitationLoad + stressLoad)
}

function particleKineticEnergy(p: ProtoParticle, depthScale = projectionDepthScale(), mass = inertialMass(p)) {
    return 0.5 * mass * (p.vx * p.vx + p.vy * p.vy + (p.vz * depthScale) * (p.vz * depthScale))
}

function groupThermalEnergy(indices: number[], depthScale = projectionDepthScale()) {
    const live = indices.filter(index => particles[index])
    if (live.length === 0) return 0

    let massSum = 0
    let meanVx = 0
    let meanVy = 0
    let meanVz = 0
    for (const index of live) {
        const p = particles[index]
        const mass = inertialMass(p)
        massSum += mass
        meanVx += p.vx * mass
        meanVy += p.vy * mass
        meanVz += p.vz * mass
    }

    meanVx /= Math.max(0.001, massSum)
    meanVy /= Math.max(0.001, massSum)
    meanVz /= Math.max(0.001, massSum)

    let thermal = 0
    for (const index of live) {
        const p = particles[index]
        const mass = inertialMass(p)
        const dvx = p.vx - meanVx
        const dvy = p.vy - meanVy
        const dvz = (p.vz - meanVz) * depthScale
        thermal += 0.5 * mass * (dvx * dvx + dvy * dvy + dvz * dvz)
    }

    return thermal / live.length
}

function groupRelativeKineticEnergy(indices: number[], depthScale = projectionDepthScale()) {
    const live = indices.filter(index => particles[index])
    if (live.length === 0) return 0

    let massSum = 0
    let meanVx = 0
    let meanVy = 0
    let meanVz = 0
    for (const index of live) {
        const p = particles[index]
        const mass = inertialMass(p)
        massSum += mass
        meanVx += p.vx * mass
        meanVy += p.vy * mass
        meanVz += p.vz * mass
    }

    meanVx /= Math.max(0.001, massSum)
    meanVy /= Math.max(0.001, massSum)
    meanVz /= Math.max(0.001, massSum)

    let relative = 0
    for (const index of live) {
        const p = particles[index]
        const mass = inertialMass(p)
        const dvx = p.vx - meanVx
        const dvy = p.vy - meanVy
        const dvz = (p.vz - meanVz) * depthScale
        relative += 0.5 * mass * (dvx * dvx + dvy * dvy + dvz * dvz)
    }

    return relative
}

function convertRelativeKineticToBoundEnergy(indices: number[], bindingPotential: number, captureScore: number, depthScale = projectionDepthScale()) {
    const live = indices.filter(index => particles[index])
    if (live.length < 2 || bindingPotential <= 0 || captureScore <= 0) return { bound: 0, radiated: 0, removedKinetic: 0 }

    let massSum = 0
    let meanVx = 0
    let meanVy = 0
    let meanVz = 0
    for (const index of live) {
        const p = particles[index]
        const mass = inertialMass(p)
        massSum += mass
        meanVx += p.vx * mass
        meanVy += p.vy * mass
        meanVz += p.vz * mass
    }

    if (massSum <= 0) return { bound: 0, radiated: 0, removedKinetic: 0 }

    meanVx /= massSum
    meanVy /= massSum
    meanVz /= massSum

    const before = groupRelativeKineticEnergy(live, depthScale)
    const targetLoss = Math.min(before * 0.72, bindingPotential * captureScore * (0.34 + settings.upperWorldCoupling * 0.08))
    const velocityScale = before > 0.000001
        ? Math.sqrt(Math.max(0, (before - targetLoss) / before))
        : 1

    for (const index of live) {
        const p = particles[index]
        p.vx = meanVx + (p.vx - meanVx) * velocityScale
        p.vy = meanVy + (p.vy - meanVy) * velocityScale
        p.vz = meanVz + (p.vz - meanVz) * velocityScale
        p.recurrence = clamp01(p.recurrence + captureScore * 0.0028)
        p.coherence = clamp01(p.coherence + captureScore * 0.0018)
        p.J = clamp01(p.J - captureScore * 0.0024)
    }

    const after = groupRelativeKineticEnergy(live, depthScale)
    const removedKinetic = Math.max(0, before - after)
    const bound = bindingPotential * captureScore
    const radiated = removedKinetic + bound
    captureBoundResidue += bound
    captureRadiatedResidue += radiated

    return { bound, radiated, removedKinetic }
}

function distanceToPoint2(p: ProtoParticle, point: { x: number, y: number, z: number }) {
    let dx = p.x - point.x
    let dy = p.y - point.y
    if (dx > width * 0.5) dx -= width
    else if (dx < -width * 0.5) dx += width
    if (dy > height * 0.5) dy -= height
    else if (dy < -height * 0.5) dy += height
    const dz = (p.z - point.z) * projectionDepthScale()
    return dx * dx + dy * dy + dz * dz
}

function atomDistance2(a: AtomComposite, b: AtomComposite) {
    let dx = b.x - a.x
    let dy = b.y - a.y
    if (dx > width * 0.5) dx -= width
    else if (dx < -width * 0.5) dx += width
    if (dy > height * 0.5) dy -= height
    else if (dy < -height * 0.5) dy += height
    const dz = (b.z - a.z) * projectionDepthScale()
    return dx * dx + dy * dy + dz * dz
}

function tripletHasRgb(indices: number[]) {
    const colors = new Set(indices.map(index => particles[index].color))
    return colors.has('red') && colors.has('green') && colors.has('blue')
}

function averageParticleValue(indices: number[], getter: (p: ProtoParticle) => number) {
    if (indices.length === 0) return 0
    return indices.reduce((sum, index) => sum + getter(particles[index]), 0) / indices.length
}

function compositePosition(indices: number[]) {
    const count = Math.max(1, indices.length)
    let x = 0
    let y = 0
    let z = 0

    for (const index of indices) {
        const p = particles[index]
        x += p.x
        y += p.y
        z += p.z
    }

    return { x: x / count, y: y / count, z: z / count }
}

function compositeSpread(indices: number[]) {
    let spread2 = 0
    for (let i = 0; i < indices.length; i++) {
        for (let j = i + 1; j < indices.length; j++) {
            spread2 = Math.max(spread2, wrappedDistance2(particles[indices[i]], particles[indices[j]]))
        }
    }
    return Math.sqrt(spread2)
}

function baryonSpreadLimit() {
    return 15
        + settings.circleStrength * 5.2
        + settings.lensStrength * 7.4
        + settings.compositeBias * 5.8
        + settings.entanglementStrength * 3.8
        - settings.timeCurvature * 4.2
}

function baryonFormationThreshold() {
    return clamp01(0.69
        + settings.nilThreshold * 0.16
        + settings.timeCurvature * 0.12
        + settings.gravityStrength * 0.04
        - settings.lensStrength * 0.08
        - settings.compositeBias * 0.08
        - settings.entanglementStrength * 0.06)
}

function baryonStability(indices: number[]) {
    const coherence = averageParticleValue(indices, p => p.coherence)
    const recurrence = averageParticleValue(indices, p => p.recurrence)
    const lowCost = 1 - averageParticleValue(indices, p => p.J)
    const anchored = indices.every(index => particles[index].mode === 3) ? 1 : 0.58
    const spread = compositeSpread(indices)
    const compactness = clamp01(1 - spread / Math.max(4, baryonSpreadLimit() * 1.35))
    return clamp01(coherence * 0.32 + recurrence * 0.12 + lowCost * 0.22 + anchored * 0.14 + compactness * 0.2)
}

function quarkFreeEnergy(index: number) {
    const p = particles[index]
    if (!p || !isQuarkKind(p.smKind)) return 0
    const projectorSlack = p.nil === smProjectorTarget(p) ? 0.04 : 0.22
    const confinementCost = 0.48 + settings.sourceCoupling * 0.08 + settings.lensStrength * 0.035
    return p.J * 0.34
        + (1 - p.coherence) * 0.2
        + (1 - p.recurrence) * 0.08
        + projectorSlack
        + confinementCost
}

function pairPhaseCost(indices: number[]) {
    if (indices.length < 2) return 0
    let cost = 0
    let pairs = 0
    for (let i = 0; i < indices.length; i++) {
        for (let j = i + 1; j < indices.length; j++) {
            const a = particles[indices[i]]
            const b = particles[indices[j]]
            if (!a || !b) continue
            cost += (1 - Math.cos(signedAngle(a.theta - b.theta))) * 0.34
                + (1 - Math.cos(signedAngle(a.sigma - b.sigma))) * 0.16
            pairs += 1
        }
    }
    return pairs > 0 ? clamp01(cost / pairs) : 0
}

function baryonBindingEnergy(indices: number[], expectedCharge: number): BindingEnergy {
    const live = indices.filter(index => particles[index] && isQuarkKind(particles[index].smKind))
    if (live.length !== 3) return { free: 0, bound: 1, binding: -1, stability: 0 }

    const charge = live.reduce((sum, index) => sum + particles[index].electricCharge, 0)
    const spread = compositeSpread(live)
    const spreadCost = clamp01(spread / Math.max(4, baryonSpreadLimit()))
    const colorCost = tripletHasRgb(live) ? 0.02 : 0.82
    const chargeCost = Math.min(1, Math.abs(charge - expectedCharge))
    const projectorCost = averageParticleValue(live, p => p.nil === smProjectorTarget(p) ? 0.04 : 0.72)
    const phaseCost = pairPhaseCost(live)
    const recurrenceSupport = averageParticleValue(live, p => p.recurrence)
    const coherenceSupport = averageParticleValue(live, p => p.coherence)
    const lowCostSupport = 1 - averageParticleValue(live, p => p.J)
    const free = live.reduce((sum, index) => sum + quarkFreeEnergy(index), 0) / live.length + spreadCost * 0.12
    const bound = Math.max(0,
        colorCost * 0.24
        + chargeCost * 0.22
        + projectorCost * 0.14
        + phaseCost * 0.2
        + spreadCost * 0.24
        + (1 - recurrenceSupport) * 0.06
        - coherenceSupport * 0.1
        - lowCostSupport * 0.1,
    )
    const binding = free - bound
    return {
        free,
        bound,
        binding,
        stability: clamp01((binding - 0.05) / 0.72),
    }
}

function buildBaryon(packet: number[], slots: number[], expectedCharge: number) {
    const indices = slots.map(slot => packetMemberBySlot(packet, slot))
    if (indices.some(index => index < 0)) return null
    if (!indices.every(index => isQuarkKind(particles[index].smKind))) return null
    if (!tripletHasRgb(indices)) return null

    const charge = indices.reduce((sum, index) => sum + particles[index].electricCharge, 0)
    if (Math.abs(charge - expectedCharge) > 0.001) return null

    const spread = compositeSpread(indices)
    const energy = baryonBindingEnergy(indices, expectedCharge)
    const stability = clamp01(baryonStability(indices) * 0.32 + energy.stability * 0.68)
    if (spread > baryonSpreadLimit() * 1.2 || energy.binding <= 0.04 || stability < baryonFormationThreshold() * 0.68) return null

    return {
        indices,
        charge,
        stability,
        spread,
        freeEnergy: energy.free,
        boundEnergy: energy.bound,
        binding: energy.binding,
    }
}

function pointDistance2(a: { x: number, y: number, z: number }, b: { x: number, y: number, z: number }) {
    const dx = wrappedOffset(b.x - a.x, width)
    const dy = wrappedOffset(b.y - a.y, height)
    const dz = (b.z - a.z) * projectionDepthScale()
    return dx * dx + dy * dy + dz * dz
}

function nucleonCaptureRadius() {
    return Math.max(30, baryonSpreadLimit() * (1.45 + settings.compositeBias * 0.18))
}

function buildBaryonCandidate(indices: number[], id: number): BaryonCandidate | null {
    const live = indices.filter(index => particles[index] && isQuarkKind(particles[index].smKind))
    if (live.length !== 3 || !tripletHasRgb(live)) return null

    const charge = live.reduce((sum, index) => sum + particles[index].electricCharge, 0)
    const expectedCharge = Math.abs(charge - 1) < 0.001 ? 1 : Math.abs(charge) < 0.001 ? 0 : Number.NaN
    if (!Number.isFinite(expectedCharge)) return null

    const energy = baryonBindingEnergy(live, expectedCharge)
    const stability = clamp01(baryonStability(live) * 0.32 + energy.stability * 0.68)
    if (compositeSpread(live) > baryonSpreadLimit() * 1.3 || energy.binding <= 0.04 || stability < baryonFormationThreshold() * 0.62) return null

    return {
        id,
        kind: expectedCharge === 1 ? 'proton' : 'neutron',
        indices: live,
        charge,
        stability,
        center: compositePosition(live),
        free: energy.free,
        bound: energy.bound,
        binding: energy.binding,
    }
}

function collectFreeBaryonCandidates(usedQuarks: Set<number>) {
    const groups = new Map<number, number[]>()
    for (let i = 0; i < particles.length; i++) {
        const p = particles[i]
        if (!isQuarkKind(p.smKind) || p.entanglementId < 0 || usedQuarks.has(i)) continue
        const members = groups.get(p.entanglementId) ?? []
        members.push(i)
        groups.set(p.entanglementId, members)
    }

    const candidates: BaryonCandidate[] = []
    for (const [id, indices] of groups) {
        const candidate = buildBaryonCandidate(indices, id)
        if (candidate) candidates.push(candidate)
    }
    return candidates.sort((a, b) => b.stability - a.stability)
}

function residualNuclearRange() {
    return Math.max(28, baryonSpreadLimit() * (1.35 + settings.compositeBias * 0.08))
}

function applyResidualNuclearForces(fx: Float32Array, fy: Float32Array, fz: Float32Array, depthScale: number) {
    if (!isSmPreset() || declaredAtoms.length > 0) return

    const baryons = collectFreeBaryonCandidates(new Set())
    if (baryons.length < 2) return

    const range = residualNuclearRange()
    const core = range * 0.36
    const maxDistance = range * 2.15

    for (let i = 0; i < baryons.length; i++) {
        const a = baryons[i]
        for (let j = i + 1; j < baryons.length; j++) {
            const b = baryons[j]
            let dx = wrappedOffset(b.center.x - a.center.x, width)
            let dy = wrappedOffset(b.center.y - a.center.y, height)
            const dzRaw = b.center.z - a.center.z
            const dz = dzRaw * depthScale
            const distance = Math.max(1, Math.hypot(dx, dy, dz))
            if (distance > maxDistance) continue

            const ux = dx / distance
            const uy = dy / distance
            const uz = dz / distance
            const stability = Math.sqrt(a.stability * b.stability)
            const strongAttraction = Math.exp(-distance / range)
                * (1 - Math.exp(-Math.max(0, distance - core) / Math.max(1, range * 0.18)))
                * (0.34 + settings.lensStrength * 0.05 + settings.compositeBias * 0.08)
                * stability
            const hardCore = distance < core
                ? (1 - distance / core) * (0.62 + settings.capacity * 0.18)
                : 0
            const coulombRepulsion = a.charge * b.charge > 0
                ? a.charge * b.charge * 0.12 / (1 + distance / Math.max(1, range * 0.45)) ** 2
                : 0
            const force = strongAttraction - hardCore - coulombRepulsion

            if (Math.abs(force) < 0.001) continue
            addGroupForce(a.indices, fx, fy, fz, ux, uy, uz / depthScale, force)
            addGroupForce(b.indices, fx, fy, fz, -ux, -uy, -uz / depthScale, force)

            if (force > 0.02) {
                const damping = Math.min(0.012, force * 0.02)
                for (const index of [...a.indices, ...b.indices]) {
                    const p = particles[index]
                    p.vx *= 1 - damping
                    p.vy *= 1 - damping
                    p.vz *= 1 - damping * 0.7
                    p.recurrence = clamp01(p.recurrence + damping * 0.5)
                }
            }
        }
    }
}

function meanVelocity(indices: number[]) {
    let vx = 0
    let vy = 0
    let vz = 0
    let count = 0
    for (const index of indices) {
        const p = particles[index]
        if (!p) continue
        vx += p.vx
        vy += p.vy
        vz += p.vz
        count += 1
    }
    return {
        vx: vx / Math.max(1, count),
        vy: vy / Math.max(1, count),
        vz: vz / Math.max(1, count),
    }
}

function electronCapturePairKey(nucleusId: number, electronIndex: number) {
    return nucleusId * 100000 + electronIndex
}

function inferredCaptureStrength(electronIndex: number, nucleusId: number) {
    const electron = particles[electronIndex]
    const capture = inferredElectronCaptures.get(electronIndex)
    if (!electron || electron.smKind !== 'electron' || !capture || capture.nucleusId !== nucleusId) return 0

    const age = frame - capture.lastFrame
    if (age > 720) return 0
    return clamp01(capture.strength * (1 - age / 720))
}

function rememberInferredElectronCapture(electronIndex: number, nucleusId: number, strength: number, lastPhotonFrame?: number) {
    const previous = inferredElectronCaptures.get(electronIndex)
    inferredElectronCaptures.set(electronIndex, {
        nucleusId,
        strength: clamp01(Math.max(previous?.nucleusId === nucleusId ? previous.strength * 0.96 : 0, strength)),
        lastFrame: frame,
        lastPhotonFrame: lastPhotonFrame ?? previous?.lastPhotonFrame ?? -999,
    })
}

function pruneInferredElectronCaptures() {
    for (const [index, capture] of inferredElectronCaptures) {
        const electron = particles[index]
        if (!electron || electron.smKind !== 'electron' || frame - capture.lastFrame > 900) {
            inferredElectronCaptures.delete(index)
        }
    }
}

function applyMttRadiativeCaptureForces(fx: Float32Array, fy: Float32Array, fz: Float32Array, depthScale: number) {
    if (!isSmPreset() || declaredAtoms.length > 0) return

    const baryons = collectFreeBaryonCandidates(new Set())
    const protons = baryons.filter(candidate => candidate.kind === 'proton')
    const neutrons = baryons.filter(candidate => candidate.kind === 'neutron')
    if (protons.length === 0) return

    const usedElectrons = new Set<number>()
    const captureReach = electronCaptureRadius() * (2.05 + settings.carrierSpread * 0.18)
    const threshold = electronCaptureThreshold() - 0.18
    const nucleonReach2 = nucleonCaptureRadius() ** 2

    for (const proton of protons) {
        let best: { index: number, score: number, distance: number } | null = null
        let neutron: BaryonCandidate | null = null
        let neutronScore = Number.POSITIVE_INFINITY

        for (const candidate of neutrons) {
            const d2 = pointDistance2(proton.center, candidate.center)
            if (d2 > nucleonReach2 || d2 >= neutronScore) continue
            neutron = candidate
            neutronScore = d2
        }

        const nucleusIds = [...proton.indices, ...(neutron ? neutron.indices : [])]
        const nucleusCenter = compositePosition(nucleusIds)

        for (let index = 0; index < particles.length; index++) {
            if (usedElectrons.has(index)) continue
            const electron = particles[index]
            if (!electron || electron.smKind !== 'electron') continue
            const previousCapture = inferredElectronCaptures.get(index)
            if (previousCapture && previousCapture.nucleusId !== proton.id && frame - previousCapture.lastFrame < 480) continue

            const distance = Math.sqrt(distanceToPoint2(electron, nucleusCenter))
            if (distance > captureReach) continue

            const nucleusVelocity = meanVelocity(nucleusIds)
            const relativeSpeed = Math.hypot(
                electron.vx - nucleusVelocity.vx,
                electron.vy - nucleusVelocity.vy,
                (electron.vz - nucleusVelocity.vz) * depthScale,
            )
            const cloudSupport = electron.measurement === 'unresolved' ? 0.08 : 0
            const captureMemory = inferredCaptureStrength(index, proton.id)
            const score = electronShellScore(index, nucleusCenter)
                + proton.stability * 0.08
                + cloudSupport
                + captureMemory * 0.24
                - clamp01(relativeSpeed / 3.2) * (captureMemory > 0.1 ? 0.08 : 0.2)

            if (score < threshold) continue
            if (!best || score > best.score) best = { index, score, distance }
        }

        if (!best) continue

        const electron = particles[best.index]
        const dx = wrappedOffset(nucleusCenter.x - electron.x, width)
        const dy = wrappedOffset(nucleusCenter.y - electron.y, height)
        const dzRaw = nucleusCenter.z - electron.z
        const distance = Math.max(1, Math.hypot(dx, dy, dzRaw * depthScale))
        const shellRadius = Math.max(28, electronCaptureRadius() * 0.68)
        const outwardAngle = distance > 3
            ? Math.atan2(-dy, -dx)
            : electron.theta + electron.sigma * 0.22
        const target = {
            x: nucleusCenter.x + Math.cos(outwardAngle) * shellRadius,
            y: nucleusCenter.y + Math.sin(outwardAngle) * shellRadius * 0.72,
            z: nucleusCenter.z - 0.12 + Math.sin(outwardAngle + electron.sigma) * 0.12,
        }
        const shellStrength = best.score * proton.stability * (0.01 + settings.lensStrength * 0.003 + settings.sourceCoupling * 0.002) * (physicsLedgerEnabled.value ? 0.54 : 1)
        addStructureForce(best.index, fx, fy, fz, target, shellStrength)

        const nucleusPull = best.score * proton.stability * (0.004 + settings.compositeBias * 0.002)
        addGroupForce(nucleusIds, fx, fy, fz, -dx / distance, -dy / distance, -dzRaw / distance, nucleusPull)

        const captureMemory = inferredCaptureStrength(best.index, proton.id)
        if ((best.score > electronCaptureThreshold() - 0.08 || captureMemory > 0.12) && best.distance < captureReach * 0.82) {
            const group = [...nucleusIds, best.index]
            const v = meanVelocity(group)
            const nucleusVelocity = meanVelocity(nucleusIds)
            const photonDirection = capturePhotonEmissionDirection(electron, nucleusCenter, nucleusVelocity)
            const bindingPotential = Math.max(0.02,
                proton.binding * 0.18
                + (neutron?.binding ?? 0) * 0.14
                + proton.stability * 0.08
                + (neutron?.stability ?? 0) * 0.04
                + best.score * 0.1)
            const capturePairKey = electronCapturePairKey(proton.id, best.index)
            const previousCapture = inferredElectronCaptures.get(best.index)
            const canRadiate = !previousCapture
                || previousCapture.nucleusId !== proton.id
                || frame - previousCapture.lastPhotonFrame > Math.max(150, Math.round(240 - settings.upperWorldCoupling * 36))
            const conversion = canRadiate
                ? convertRelativeKineticToBoundEnergy(group, bindingPotential, best.score * proton.stability, depthScale)
                : { bound: 0, radiated: 0, removedKinetic: 0 }
            const emitted = canRadiate
                ? emitCapturePhoton(nucleusCenter, photonDirection, conversion.radiated, group, capturePairKey)
                : false
            const captureStrength = clamp01(captureMemory * 0.94 + best.score * proton.stability * 0.18 + (emitted ? 0.12 : 0.035))
            rememberInferredElectronCapture(best.index, proton.id, captureStrength, emitted ? frame : previousCapture?.lastPhotonFrame)
            electron.recurrence = clamp01(electron.recurrence + captureStrength * 0.018)
            electron.coherence = clamp01(electron.coherence + captureStrength * 0.012)
            electron.J = clamp01(electron.J - captureStrength * 0.018)

            const damping = best.score * best.score * (0.012 + settings.upperWorldCoupling * 0.004 + captureStrength * 0.018)
            for (const index of group) {
                const p = particles[index]
                if (!p) continue
                p.vx += (v.vx - p.vx) * damping
                p.vy += (v.vy - p.vy) * damping
                p.vz += (v.vz - p.vz) * damping
                p.recurrence = clamp01(p.recurrence + best.score * 0.0025)
                p.coherence = clamp01(p.coherence + best.score * 0.0016)
                p.J = clamp01(p.J - best.score * 0.0022)
            }
            energyPulseResidue = Math.max(0, energyPulseResidue - conversion.radiated * 0.22)
        }

        usedElectrons.add(best.index)
    }
}

function electronCaptureRadius() {
    return (18
        + settings.capacity * 12
        + settings.lensStrength * 8
        + settings.compositeBias * 6
        + settings.measurementStrength * 4
        - settings.gravityStrength * 2)
        * settings.carrierSpread
}

function electronCaptureThreshold() {
    return clamp01(0.62
        + settings.nilThreshold * 0.14
        + settings.timeCurvature * 0.12
        - settings.capacity * 0.08
        - settings.lensStrength * 0.05
        - settings.entanglementStrength * 0.04)
}

function electronShellScore(index: number, center: { x: number, y: number, z: number }) {
    const electron = particles[index]
    const distance = Math.sqrt(distanceToPoint2(electron, center))
    const captureRadius = Math.max(8, electronCaptureRadius())
    const captureSupport = clamp01(1 - Math.max(0, distance - captureRadius) / captureRadius)
    const compressionPenalty = clamp01(1 - distance / mttClosureCellRadius(electron))
    const lowCost = 1 - electron.J
    return clamp01(electron.coherence * 0.38 + lowCost * 0.22 + electron.recurrence * 0.12 + captureSupport * 0.28 - compressionPenalty * 0.08)
}

function mttClosureCellRadius(p: ProtoParticle) {
    return Math.max(5, (p.radius * (2.2 + settings.capacity * 1.8 + settings.lensStrength * 0.55) + settings.projectionDepth * 1.4 + (1 - p.J) * 2.4) * settings.carrierSpread)
}

function wrapParticlePosition(p: ProtoParticle) {
    if (p.x < 0) p.x += width
    else if (p.x >= width) p.x -= width
    if (p.y < 0) p.y += height
    else if (p.y >= height) p.y -= height
}

function atomCarrierMean(atom: AtomComposite) {
    let thetaX = 0
    let thetaY = 0
    let sigmaX = 0
    let sigmaY = 0
    let weightSum = 0

    for (const index of atom.nucleusIds) {
        const p = particles[index]
        if (!p) continue
        const weight = 0.35 + p.coherence + (1 - p.J) * 0.4
        thetaX += Math.cos(p.theta) * weight
        thetaY += Math.sin(p.theta) * weight
        sigmaX += Math.cos(p.sigma) * weight
        sigmaY += Math.sin(p.sigma) * weight
        weightSum += weight
    }

    if (weightSum <= 0) return { theta: atom.id * 0.37, sigma: atom.id * 0.19 }
    return {
        theta: wrapAngle(Math.atan2(thetaY, thetaX)),
        sigma: wrapAngle(Math.atan2(sigmaY, sigmaX)),
    }
}

function mttClosureFunctional(electron: ProtoParticle, atom: AtomComposite, atomCarrier: { theta: number, sigma: number }, offsetX = 0, offsetY = 0, offsetZ = 0): MttClosureCost {
    const depthScale = Math.max(1, projectionDepthScale())
    const dx = wrappedOffset(electron.x + offsetX - atom.x, width)
    const dy = wrappedOffset(electron.y + offsetY - atom.y, height)
    const dz = electron.z + offsetZ - atom.z
    const weightedDz = dz * depthScale
    const distance = Math.max(0.5, Math.hypot(dx, dy, weightedDz))
    const compression = clamp01(1 - distance / mttClosureCellRadius(electron))

    const phaseThetaCost = (1 - Math.cos(signedAngle(electron.theta - atomCarrier.theta))) * 0.5
    const phaseSigmaCost = (1 - Math.cos(signedAngle(electron.sigma - atomCarrier.sigma))) * 0.5
    const phase = clamp01(phaseThetaCost * 0.62 + phaseSigmaCost * 0.38)

    const carrierBranch = basinFromCarrier(electron.theta, electron.sigma)
    const nil = electron.nil === -1
        ? 0.28
        : electron.nil === carrierBranch
            ? 0.04
            : 0.86

    const lens = electron.lens === -1 && electron.electricCharge < 0
        ? 0.04
        : clamp01(Math.abs(electron.lens + 1) * 0.45 + Math.max(0, electron.electricCharge + 1) * 0.2)

    const radialFlow = Math.abs((dx * electron.vx + dy * electron.vy + weightedDz * electron.vz * depthScale) / distance)
    const planarDistance = Math.max(1, Math.hypot(dx, dy))
    const tangentialFlow = Math.abs((dx * electron.vy - dy * electron.vx) / planarDistance)
    const returnSupport = clamp01(tangentialFlow / (tangentialFlow + radialFlow + 0.12) * 0.46 + electron.recurrence * 0.54)
    const winding = 1 - returnSupport

    const capacity = clamp01(compression * compression / Math.max(0.34, settings.capacity * (0.62 + electron.coherence * 0.38)))
    const selection = phase * 0.32 + nil * 0.18 + lens * 0.12 + winding * 0.22 + (1 - electron.coherence) * 0.16
    const total = clamp01(compression * compression * (0.34 + capacity * 0.52 + selection * 0.74) + compression * selection * 0.18)

    return {
        total,
        phase,
        nil,
        lens,
        capacity,
        winding,
        compression,
    }
}

function applyMttClosureGradient() {
    if (!isSmPreset() || atomComposites.length === 0) {
        invariantState.mttClosureSamples = 0
        invariantState.mttClosureCost = 0
        return
    }

    let samples = 0
    let totalCost = 0
    let phaseCost = 0
    let nilCost = 0
    let lensCost = 0
    let windingCost = 0

    for (const atom of atomComposites) {
        if (atom.stability < 0.18 || atom.electronIds.length === 0) continue
        const atomCarrier = atomCarrierMean(atom)

        for (const electronId of atom.electronIds) {
            const electron = particles[electronId]
            if (!electron || electron.smKind !== 'electron') continue

            const base = mttClosureFunctional(electron, atom, atomCarrier)
            samples += 1
            totalCost += base.total
            phaseCost += base.phase
            nilCost += base.nil
            lensCost += base.lens
            windingCost += base.winding

            if (base.compression <= 0.001) continue

            const epsilon = Math.max(1.2, mttClosureCellRadius(electron) * 0.24)
            const gradX = (mttClosureFunctional(electron, atom, atomCarrier, epsilon, 0, 0).total - mttClosureFunctional(electron, atom, atomCarrier, -epsilon, 0, 0).total) / (2 * epsilon)
            const gradY = (mttClosureFunctional(electron, atom, atomCarrier, 0, epsilon, 0).total - mttClosureFunctional(electron, atom, atomCarrier, 0, -epsilon, 0).total) / (2 * epsilon)
            const gradZ = (mttClosureFunctional(electron, atom, atomCarrier, 0, 0, epsilon / Math.max(1, projectionDepthScale())).total - mttClosureFunctional(electron, atom, atomCarrier, 0, 0, -epsilon / Math.max(1, projectionDepthScale())).total) / (2 * epsilon)
            const response = atom.stability * (2.2 + settings.capacity * 0.5 + (1 - electron.J) * 0.38) * settings.sourceCoupling
            let kickX = -gradX * response
            let kickY = -gradY * response
            let kickZ = -gradZ * response

            if (Math.hypot(kickX, kickY) < 0.0001 && base.compression > 0.82) {
                const phaseDirection = electron.theta + electron.sigma * 0.5
                const phaseKick = base.total * response / Math.max(1, mttClosureCellRadius(electron))
                kickX += Math.cos(phaseDirection) * phaseKick
                kickY += Math.sin(phaseDirection) * phaseKick
            }

            electron.vx += kickX
            electron.vy += kickY
            electron.vz += kickZ

            const dx = wrappedOffset(electron.x - atom.x, width)
            const dy = wrappedOffset(electron.y - atom.y, height)
            const planarDistance = Math.max(1, Math.hypot(dx, dy))
            const tangentX = -dy / planarDistance
            const tangentY = dx / planarDistance
            const phaseSlip = Math.sin(signedAngle(electron.theta - atomCarrier.theta) - signedAngle(electron.sigma - atomCarrier.sigma) * 0.5)
            const returnFlow = phaseSlip * base.compression * atom.stability * (settings.circleStrength * 0.022 + electron.recurrence * 0.014) * settings.upperWorldCoupling
            electron.vx += tangentX * returnFlow
            electron.vy += tangentY * returnFlow

            electron.J = clamp01(electron.J + base.total * 0.005 + base.compression * base.capacity * 0.004 - (1 - base.total) * 0.002)
            electron.coherence = clamp01(electron.coherence + (1 - base.total) * atom.stability * 0.004 - base.compression * base.capacity * 0.002)
            electron.pressure = clamp01(electron.pressure + base.compression * (base.capacity + base.winding) * 0.003 - (1 - base.compression) * 0.001)
            wrapParticlePosition(electron)
        }
    }

    invariantState.mttClosureSamples = samples
    if (samples > 0) {
        invariantState.mttClosureCost = totalCost / samples
        invariantState.mttPhaseReturn = clamp01(1 - phaseCost / samples)
        invariantState.mttNilBudget = clamp01(1 - nilCost / samples)
        invariantState.mttLensBalance = clamp01(1 - lensCost / samples)
        invariantState.mttWindingReturn = clamp01(1 - windingCost / samples)
    } else {
        invariantState.mttClosureCost = 0
    }
}

function atomClusterRadius() {
    return 28 + settings.gravityStrength * 180 + settings.capacity * 12 + settings.timeCurvature * 8
}

function assignAtomClusters() {
    const visited = new Set<number>()
    let clusterId = 0
    const radius2 = atomClusterRadius() ** 2
    const gravityPull = clamp01(settings.gravityStrength * 0.16)

    for (let i = 0; i < atomComposites.length; i++) {
        if (visited.has(i)) continue

        const queue = [i]
        const cluster: number[] = []
        visited.add(i)

        while (queue.length > 0) {
            const current = queue.pop()
            if (current === undefined) continue
            cluster.push(current)

            for (let j = 0; j < atomComposites.length; j++) {
                if (visited.has(j)) continue
                if (atomComposites[current].charge !== 0 || atomComposites[j].charge !== 0) continue
                if (atomDistance2(atomComposites[current], atomComposites[j]) > radius2) continue
                visited.add(j)
                queue.push(j)
            }
        }

        let cx = 0
        let cy = 0
        let cz = 0
        for (const index of cluster) {
            const atom = atomComposites[index]
            cx += atom.x
            cy += atom.y
            cz += atom.z
        }
        cx /= Math.max(1, cluster.length)
        cy /= Math.max(1, cluster.length)
        cz /= Math.max(1, cluster.length)

        for (const index of cluster) {
            const atom = atomComposites[index]
            atom.clusterId = clusterId
            if (cluster.length > 1 && gravityPull > 0) {
                atom.x = atom.x * (1 - gravityPull) + cx * gravityPull
                atom.y = atom.y * (1 - gravityPull) + cy * gravityPull
                atom.z = atom.z * (1 - gravityPull * 0.35) + cz * gravityPull * 0.35
            }
        }

        clusterId += 1
    }
}

function declaredAtomById(id: number) {
    return declaredAtoms.find(atom => atom.id === id)
}

function declaredAtomCenter(atom: DeclaredAtom) {
    const ids = atom.nucleusIds.filter(index => particles[index])
    if (ids.length === 0) return { x: atom.x, y: atom.y, z: atom.z }
    return compositePosition(ids)
}

function declaredAtomStability(atom: DeclaredAtom, charge: number) {
    const nucleusIds = atom.nucleusIds.filter(index => particles[index])
    const electronIds = atom.electronIds.filter(index => particles[index])
    const nuclearSupport = nucleusIds.length > 0
        ? averageParticleValue(nucleusIds, p => p.coherence * 0.45 + (1 - p.J) * 0.35 + p.recurrence * 0.2)
        : 0
    const shellSupport = electronIds.length > 0
        ? averageParticleValue(electronIds, p => p.coherence * 0.44 + (1 - p.J) * 0.34 + p.recurrence * 0.22)
        : 0
    const expectedElectrons = Math.max(1, atom.protons)
    const shellFill = clamp01(electronIds.length / expectedElectrons)
    const neutrality = 1 - Math.min(1, Math.abs(charge))
    const liveBonds = atom.bondIds
        .map(id => declaredBonds.find(bond => bond.id === id))
        .filter((bond): bond is DeclaredBond => Boolean(bond))
    const bondSupport = liveBonds.length > 0
        ? liveBonds.reduce((sum, bond) => sum + bond.stability, 0) / liveBonds.length * 0.1
        : 0
    return clamp01(nuclearSupport * 0.42 + shellSupport * 0.26 + shellFill * 0.12 + neutrality * 0.12 + bondSupport)
}

function declaredAtomVector(left: DeclaredAtom, right: DeclaredAtom, depthScale = projectionDepthScale()) {
    const dx = wrappedOffset(right.x - left.x, width)
    const dy = wrappedOffset(right.y - left.y, height)
    const dzRaw = right.z - left.z
    const dz = dzRaw * depthScale
    const distance = Math.max(1, Math.hypot(dx, dy, dz))
    return { dx, dy, dzRaw, dz, distance }
}

function declaredAtomCoreRadius(atom: DeclaredAtom) {
    return 8 + Math.sqrt(Math.max(1, atom.protons + atom.neutrons)) * 2.4
}

function declaredBondIdealLength(bond: DeclaredBond) {
    return Math.max(24, bond.restLength * (bond.label === 'H...O' ? 1.08 : 1))
}

function declaredAtomUnitDirection(left: DeclaredAtom, right: DeclaredAtom, vector: ReturnType<typeof declaredAtomVector>) {
    let ux = vector.dx / vector.distance
    let uy = vector.dy / vector.distance
    let uz = vector.dzRaw / vector.distance
    if (Math.abs(ux) + Math.abs(uy) + Math.abs(uz) < 0.001) {
        const angle = wrapAngle(left.id * 0.113 + right.id * 0.173)
        ux = Math.cos(angle)
        uy = Math.sin(angle)
        uz = 0
    }
    return { ux, uy, uz }
}

function distanceFromPointToAtom(point: { x: number, y: number, z: number }, atom: DeclaredAtom, depthScale = projectionDepthScale()) {
    const dx = wrappedOffset(point.x - atom.x, width)
    const dy = wrappedOffset(point.y - atom.y, height)
    const dz = (point.z - atom.z) * depthScale
    return Math.max(1, Math.hypot(dx, dy, dz))
}

function declaredBondClosureEnergy(bond: DeclaredBond): BondClosureEnergy {
    const left = declaredAtomById(bond.atomIds[0])
    const right = declaredAtomById(bond.atomIds[1])
    if (!left || !right) return { free: 0, bound: 1, binding: -1, stability: 0, distance: 0, bridge: 0, repulsion: 1, pressure: 1 }

    const depthScale = projectionDepthScale()
    const vector = declaredAtomVector(left, right, depthScale)
    const idealLength = declaredBondIdealLength(bond)
    const bondScale = Math.max(24, (left.shellRadius + right.shellRadius) * 0.9 * settings.carrierSpread)
    const liveElectrons = bond.electronIds.filter(index => particles[index])
    let bridge = 0
    let phaseCost = 0

    for (const index of liveElectrons) {
        const electron = particles[index]
        const point = { x: electron.x, y: electron.y, z: electron.z }
        const dl = distanceFromPointToAtom(point, left, depthScale)
        const dr = distanceFromPointToAtom(point, right, depthScale)
        const shared = clamp01((left.protons / (1 + dl / bondScale) + right.protons / (1 + dr / bondScale)) / Math.max(1, left.protons + right.protons))
        const balance = clamp01(1 - Math.abs(dl - dr) / Math.max(1, dl + dr))
        const recurrence = electron.recurrence * 0.38 + electron.coherence * 0.34 + (1 - electron.J) * 0.28
        bridge += clamp01(shared * 0.4 + balance * 0.28 + recurrence * 0.32)
        phaseCost += (1 - recurrence) * 0.48 + (electron.lens === -1 ? 0.04 : 0.34)
    }

    const bridgeSupport = liveElectrons.length > 0 ? bridge / liveElectrons.length : 0
    const meanPhaseCost = liveElectrons.length > 0 ? phaseCost / liveElectrons.length : 0.65
    let electronPressure = 0
    for (let i = 0; i < liveElectrons.length; i++) {
        for (let j = i + 1; j < liveElectrons.length; j++) {
            const a = particles[liveElectrons[i]]
            const b = particles[liveElectrons[j]]
            if (!a || !b) continue
            const distance = Math.sqrt(wrappedDistance2(a, b))
            electronPressure += clamp01(1 - distance / Math.max(8, bondScale * 0.32)) * 0.24
        }
    }

    const electronScreening = clamp01(bridgeSupport * 0.38 + Math.min(liveElectrons.length, 4) * 0.045 + bond.order * 0.04)
    const nuclearRepulsion = (left.protons * right.protons) / (1 + vector.distance / Math.max(12, bondScale)) * 0.18 * (1 - electronScreening)
    const compressionLeak = vector.distance < idealLength
        ? clamp01((idealLength - vector.distance) / idealLength) * 0.42
        : 0
    const separationLeak = clamp01(Math.abs(vector.distance - idealLength) / Math.max(1, idealLength * 1.4)) * 0.2 + compressionLeak
    const free = 0.34
        + liveElectrons.reduce((sum, index) => {
            const p = particles[index]
            return sum + (p ? p.J * 0.26 + (1 - p.coherence) * 0.18 + (1 - p.recurrence) * 0.16 : 0.6)
        }, 0) / Math.max(1, liveElectrons.length)
        + (left.protons + right.protons) * 0.08
    const bound = Math.max(0, nuclearRepulsion + electronPressure + meanPhaseCost * 0.2 + separationLeak - bridgeSupport * 0.62 - bond.order * 0.04)
    const binding = free - bound

    return {
        free,
        bound,
        binding,
        stability: clamp01((binding - 0.04) / 0.58),
        distance: vector.distance,
        bridge: bridgeSupport,
        repulsion: nuclearRepulsion,
        pressure: electronPressure,
    }
}

function updateDeclaredBondStability(bond: DeclaredBond) {
    const energy = declaredBondClosureEnergy(bond)
    bond.freeEnergy = energy.free
    bond.boundEnergy = energy.bound
    bond.binding = energy.binding
    bond.stability = energy.stability
}

function buildDeclaredAtomComposites() {
    atomComposites = []

    for (const atom of declaredAtoms) {
        const center = declaredAtomCenter(atom)
        atom.x = center.x
        atom.y = center.y
        atom.z = center.z
    }

    for (const bond of declaredBonds) updateDeclaredBondStability(bond)

    for (const atom of declaredAtoms) {
        const electronIds = atom.electronIds.filter(index => particles[index])
        const nucleusIds = atom.nucleusIds.filter(index => particles[index])
        const charge = atom.protons - electronIds.length
        const stability = declaredAtomStability(atom, charge)
        const radius = atom.shellRadius + atom.neutrons * 2.4 + atom.protons * 1.8 + stability * 8
        atomComposites.push({
            id: atom.id,
            x: atom.x,
            y: atom.y,
            z: atom.z,
            protons: atom.protons,
            neutrons: atom.neutrons,
            electrons: electronIds.length,
            charge,
            stability,
            radius,
            nucleusIds,
            electronIds,
            clusterId: atom.bondIds.length > 0 ? atom.moleculeId : atom.id,
        })
    }

    updateAtomMetrics()
}

function buildFreeAtomComposites(usedQuarks: Set<number>, usedElectrons: Set<number>) {
    const baryons = collectFreeBaryonCandidates(usedQuarks)
    const protons = baryons.filter(candidate => candidate.kind === 'proton')
    const neutrons = baryons.filter(candidate => candidate.kind === 'neutron')
    const usedBaryons = new Set<number>()
    const captureRadius2 = nucleonCaptureRadius() ** 2

    for (const proton of protons) {
        if (usedBaryons.has(proton.id)) continue

        let neutron: BaryonCandidate | null = null
        let neutronScore = Number.POSITIVE_INFINITY
        for (const candidate of neutrons) {
            if (usedBaryons.has(candidate.id)) continue
            const d2 = pointDistance2(proton.center, candidate.center)
            if (d2 > captureRadius2 || d2 >= neutronScore) continue
            neutron = candidate
            neutronScore = d2
        }

        const nucleusIds = [...proton.indices, ...(neutron ? neutron.indices : [])]
        const center = compositePosition(nucleusIds)
        const electronPool = particles
            .map((particle, index) => ({ particle, index }))
            .filter(({ particle, index }) => particle.smKind === 'electron' && particle.mode === 1 && !usedElectrons.has(index))
            .map(({ index }) => ({
                index,
                score: electronShellScore(index, center) + inferredCaptureStrength(index, proton.id) * 0.38,
            }))
            .filter(item => item.score >= electronCaptureThreshold() - 0.24)
            .sort((a, b) => b.score - a.score)
        const electronIds = electronPool.slice(0, 1).map(item => item.index)
        const electrons = electronIds.length
        const neutronsCount = neutron ? 1 : 0
        const charge = 1 - electrons
        const captureMemory = electronIds.length > 0 ? inferredCaptureStrength(electronIds[0], proton.id) : 0
        const shellSupport = electrons > 0 ? averageParticleValue(electronIds, p => p.coherence) : 0
        const nuclearSupport = proton.stability * 0.62 + (neutron ? neutron.stability * 0.38 : 0)
        const neutrality = 1 - Math.min(1, Math.abs(charge))
        const lowCost = 1 - averageParticleValue([...nucleusIds, ...electronIds], p => p.J)
        const captureSupport = electronPool.length > 0 ? electronPool[0].score : 0
        const thermalEnergy = groupThermalEnergy([...nucleusIds, ...electronIds])
        const relativeEnergy = groupRelativeKineticEnergy([...nucleusIds, ...electronIds])
        const carrierDissipation = averageParticleValue([...nucleusIds, ...electronIds], p => p.recurrence * 0.46 + p.coherence * 0.32 + (1 - p.J) * 0.22)
        const releaseSupport = clamp01((proton.binding + (neutron?.binding ?? 0)) * 0.32 + captureSupport * 0.24 + carrierDissipation * 0.28 + captureMemory * 0.18)
        const conversionSupport = clamp01(captureBoundResidue * 0.12 + captureRadiatedResidue * 0.06)
        const energyPenalty = clamp01((thermalEnergy - releaseSupport * 0.82 - conversionSupport * 0.28 - captureMemory * 1.6) / Math.max(0.42, 1.2 + releaseSupport + captureMemory * 2.6)) * 0.2 * (1 - captureMemory * 0.55)
        const driftPenalty = clamp01(relativeEnergy / Math.max(0.2, 4.6 + releaseSupport * 2.4 + captureMemory * 7.5)) * 0.1 * (1 - captureMemory * 0.65)
        const pressurePenalty = metrics.meanPressure * 0.1 + geometry.pressure * 0.08
        const stability = clamp01(nuclearSupport * 0.34 + shellSupport * 0.22 + neutrality * 0.16 + lowCost * 0.12 + releaseSupport * 0.14 + captureSupport * 0.08 + captureMemory * 0.18 + settings.capacity * 0.04 - pressurePenalty - energyPenalty - driftPenalty)

        if (stability < (electrons > 0 ? 0.2 : electronCaptureThreshold() - 0.11) && captureMemory < 0.16) continue
        if (thermalEnergy > 1.24 + releaseSupport * 1.95 + conversionSupport + captureMemory * 9.5 && captureMemory < 0.24) continue

        atomComposites.push({
            id: proton.id,
            x: center.x,
            y: center.y,
            z: center.z,
            protons: 1,
            neutrons: neutronsCount,
            electrons,
            charge,
            stability,
            radius: 42 + neutronsCount * 8 + shellSupport * 18,
            nucleusIds,
            electronIds,
            clusterId: -1,
        })

        usedBaryons.add(proton.id)
        proton.indices.forEach(index => usedQuarks.add(index))
        if (neutron) {
            usedBaryons.add(neutron.id)
            neutron.indices.forEach(index => usedQuarks.add(index))
        }
        electronIds.forEach(index => usedElectrons.add(index))
    }
}

function buildAtomComposites() {
    atomComposites = []

    if (!isSmPreset()) {
        updateAtomMetrics()
        return
    }

    if (declaredAtoms.length > 0) {
        buildDeclaredAtomComposites()
        return
    }

    const packets = new Map<number, number[]>()
    for (let i = 0; i < particles.length; i++) {
        const p = particles[i]
        if (p.smKind === 'generic') continue
        const members = packets.get(p.packetId) ?? []
        members.push(i)
        packets.set(p.packetId, members)
    }

    const usedQuarks = new Set<number>()
    const usedElectrons = new Set<number>()

    for (const [packetId, packet] of packets) {
        const proton = buildBaryon(packet, [0, 1, 5], 1)
        const neutron = buildBaryon(packet, [2, 3, 4], 0)
        if (!proton) continue

        const nucleusIds = [...proton.indices, ...(neutron ? neutron.indices : [])]
        const center = compositePosition(nucleusIds)
        const electronPool = packet
            .filter(index => particles[index].smKind === 'electron' && particles[index].mode === 1)
            .map(index => ({ index, score: electronShellScore(index, center) }))
            .filter(item => item.score >= electronCaptureThreshold())
            .sort((a, b) => b.score - a.score)
            .map(item => item.index)
        const electronIds = electronPool.slice(0, 1)
        const electrons = electronIds.length
        const neutrons = neutron ? 1 : 0
        const charge = 1 - electrons
        if (electrons === 0) continue

        const shellSupport = electrons > 0 ? averageParticleValue(electronIds, p => p.coherence) : 0
        const nuclearSupport = proton.stability * 0.64 + (neutron ? neutron.stability * 0.36 : 0)
        const neutrality = 1 - Math.min(1, Math.abs(charge))
        const lowCost = 1 - averageParticleValue([...nucleusIds, ...electronIds], p => p.J)
        const pressurePenalty = metrics.meanPressure * 0.12 + geometry.pressure * 0.08
        const stability = clamp01(nuclearSupport * 0.4 + shellSupport * 0.22 + neutrality * 0.18 + lowCost * 0.12 + settings.capacity * 0.06 - pressurePenalty)

        if (stability < electronCaptureThreshold() - 0.08) continue

        atomComposites.push({
            id: packetId,
            x: center.x,
            y: center.y,
            z: center.z,
            protons: 1,
            neutrons,
            electrons,
            charge,
            stability,
            radius: 42 + neutrons * 8 + shellSupport * 18,
            nucleusIds,
            electronIds,
            clusterId: -1,
        })

        nucleusIds.forEach(index => usedQuarks.add(index))
        electronIds.forEach(index => usedElectrons.add(index))
    }

    buildFreeAtomComposites(usedQuarks, usedElectrons)
    assignAtomClusters()
    updateAtomMetrics()
}

function isDeclaredCovalentScaffold(bond: DeclaredBond) {
    return bond.label === 'O-H' || bond.label === 'H2'
}

function declaredBondHasLiveEnds(bond: DeclaredBond) {
    const left = declaredAtomById(bond.atomIds[0])
    const right = declaredAtomById(bond.atomIds[1])
    return Boolean(left && right && left.nucleusIds.some(index => particles[index]) && right.nucleusIds.some(index => particles[index]))
}

function isDeclaredBondActive(bond: DeclaredBond) {
    if (isDeclaredCovalentScaffold(bond) && declaredBondHasLiveEnds(bond)) return true
    return bond.stability > 0.08 || bond.binding > 0.03
}

function declaredMoleculeBendError() {
    const moleculeIds = [...new Set(declaredBonds.map(bond => bond.moleculeId))]
    let total = 0
    let samples = 0

    for (const moleculeId of moleculeIds) {
        const oxygen = declaredAtoms.find(atom => atom.moleculeId === moleculeId && atom.label === 'O')
        if (!oxygen) continue
        const hydrogens = declaredAtoms.filter(atom => atom.moleculeId === moleculeId && atom.label === 'H')
        if (hydrogens.length < 2) continue

        const first = hydrogens[0]
        const second = hydrogens[1]
        const a = declaredAtomVector(oxygen, first)
        const b = declaredAtomVector(oxygen, second)
        const dot = (a.dx * b.dx + a.dy * b.dy + a.dz * b.dz) / Math.max(1, a.distance * b.distance)
        const angle = Math.acos(Math.max(-1, Math.min(1, dot))) * 180 / Math.PI
        total += Math.abs(angle - 104.5)
        samples += 1
    }

    return samples > 0 ? total / samples : -1
}

function declaredAtomParticleIds(atom: DeclaredAtom) {
    return [...atom.nucleusIds, ...atom.electronIds].filter(index => particles[index])
}

function declaredOhRestLength(oxygen: DeclaredAtom, hydrogen: DeclaredAtom) {
    const bond = declaredBonds.find(item =>
        item.label === 'O-H'
        && item.atomIds.includes(oxygen.id)
        && item.atomIds.includes(hydrogen.id),
    )
    return bond ? declaredBondIdealLength(bond) : 62
}

function addDeclaredAtomCenterForce(atom: DeclaredAtom, target: { x: number, y: number, z: number }, fx: Float32Array, fy: Float32Array, fz: Float32Array, strength: number, depthScale: number) {
    const dx = wrappedOffset(target.x - atom.x, width)
    const dy = wrappedOffset(target.y - atom.y, height)
    const dz = target.z - atom.z
    const distance = Math.max(1, Math.hypot(dx, dy, dz * depthScale))
    const stiffness = Math.min(0.022, (0.004 + strength * 0.16) * clamp01(distance / Math.max(1, atom.shellRadius * 0.36)))
    for (const index of declaredAtomParticleIds(atom)) {
        fx[index] += dx * stiffness
        fy[index] += dy * stiffness
        fz[index] += dz * stiffness
    }
}

function relaxDeclaredAtomCenter(atom: DeclaredAtom, target: { x: number, y: number, z: number }, amount: number) {
    const dx = wrappedOffset(target.x - atom.x, width)
    const dy = wrappedOffset(target.y - atom.y, height)
    const dz = target.z - atom.z
    const correction = clamp01(amount)
    for (const index of declaredAtomParticleIds(atom)) {
        const p = particles[index]
        if (!p) continue
        p.x += dx * correction
        p.y += dy * correction
        p.z += dz * correction
        p.vx = (p.vx + dx * correction * 0.014) * 0.986
        p.vy = (p.vy + dy * correction * 0.014) * 0.986
        p.vz = (p.vz + dz * correction * 0.014) * 0.986
        wrapParticlePosition(p)
    }
    atom.x += dx * correction
    atom.y += dy * correction
    atom.z += dz * correction
}

function applyDeclaredWaterBendForces(fx: Float32Array, fy: Float32Array, fz: Float32Array, depthScale: number) {
    const targetAngle = 104.5 * Math.PI / 180
    const moleculeIds = [...new Set(declaredBonds.map(bond => bond.moleculeId))]

    for (const moleculeId of moleculeIds) {
        const oxygen = declaredAtoms.find(atom => atom.moleculeId === moleculeId && atom.label === 'O')
        if (!oxygen) continue
        const hydrogens = declaredAtoms.filter(atom => atom.moleculeId === moleculeId && atom.label === 'H')
        if (hydrogens.length < 2) continue

        const left = hydrogens[0]
        const right = hydrogens[1]
        const leftVector = declaredAtomVector(oxygen, left, depthScale)
        const rightVector = declaredAtomVector(oxygen, right, depthScale)
        const leftAngle = Math.atan2(leftVector.dy, leftVector.dx)
        const rightAngle = Math.atan2(rightVector.dy, rightVector.dx)
        const separation = signedAngle(rightAngle - leftAngle)
        if (Math.abs(separation) < 0.001) continue

        const orientation = leftAngle + separation * 0.5
        const handedness = separation >= 0 ? 1 : -1
        const halfAngle = targetAngle * 0.5
        const restLength = (declaredOhRestLength(oxygen, left) + declaredOhRestLength(oxygen, right)) * 0.5
        const error = Math.abs(Math.abs(separation) - targetAngle)
        const strength = Math.min(0.14, 0.018 + error / targetAngle * 0.08) * Math.max(0.45, settings.physicsLedgerStrength)
        const leftTargetAngle = orientation - handedness * halfAngle
        const rightTargetAngle = orientation + handedness * halfAngle
        const leftTarget = {
            x: oxygen.x + Math.cos(leftTargetAngle) * restLength,
            y: oxygen.y + Math.sin(leftTargetAngle) * restLength,
            z: oxygen.z - 0.06,
        }
        const rightTarget = {
            x: oxygen.x + Math.cos(rightTargetAngle) * restLength,
            y: oxygen.y + Math.sin(rightTargetAngle) * restLength,
            z: oxygen.z + 0.06,
        }

        addDeclaredAtomCenterForce(left, leftTarget, fx, fy, fz, strength, depthScale)
        addDeclaredAtomCenterForce(right, rightTarget, fx, fy, fz, strength, depthScale)
        relaxDeclaredAtomCenter(left, leftTarget, Math.min(0.18, 0.035 + error / targetAngle * 0.08))
        relaxDeclaredAtomCenter(right, rightTarget, Math.min(0.18, 0.035 + error / targetAngle * 0.08))
    }
}

function updateAtomMetrics() {
    const activeBonds = declaredBonds.filter(isDeclaredBondActive)
    metrics.atomProtons = atomComposites.reduce((sum, atom) => sum + atom.protons, 0)
    metrics.atomNeutrons = atomComposites.reduce((sum, atom) => sum + atom.neutrons, 0)
    metrics.atomElectrons = atomComposites.reduce((sum, atom) => sum + atom.electrons, 0)
    metrics.atomCandidates = atomComposites.length
    metrics.neutralAtoms = atomComposites.filter(atom => Math.abs(atom.charge) < 0.001).length
    metrics.atomClusters = new Set(atomComposites.map(atom => atom.clusterId).filter(id => id >= 0)).size
    metrics.atomBonds = activeBonds.length
    metrics.molecules = new Set(activeBonds.map(bond => bond.moleculeId)).size
    metrics.moleculeBendError = declaredMoleculeBendError()
    updateBindingMetrics()
}

function updateBindingMetrics() {
    const groups = new Map<number, number[]>()
    for (let i = 0; i < particles.length; i++) {
        const p = particles[i]
        if (!isQuarkKind(p.smKind)) continue
        const groupId = p.entanglementId >= 0 ? p.entanglementId : p.packetId * 100 + Math.floor(particleSlot(p) / 3)
        const group = groups.get(groupId) ?? []
        group.push(i)
        groups.set(groupId, group)
    }

    let baryonSamples = 0
    let boundBaryons = 0
    let bindingSum = 0
    let activationSum = 0
    let releaseSum = 0
    for (const group of groups.values()) {
        if (group.length < 3) continue
        const triplet = group.slice(0, 3)
        const charge = triplet.reduce((sum, index) => sum + particles[index].electricCharge, 0)
        const expectedCharge = charge > 0.5 ? 1 : 0
        const energy = baryonBindingEnergy(triplet, expectedCharge)
        baryonSamples += 1
        bindingSum += energy.binding
        activationSum += Math.max(0.08, energy.bound + 0.1 * (1 - energy.stability))
        releaseSum += Math.max(0, energy.binding)
        if (tripletHasRgb(triplet) && energy.binding > 0.04) boundBaryons += 1
    }

    const liveBonds = declaredBonds.filter(bond => bond.stability > 0.001)
    for (const bond of liveBonds) {
        activationSum += Math.max(0.08, bond.boundEnergy + bond.order * 0.1 + Math.max(0, 0.12 - bond.stability * 0.04))
        releaseSum += Math.max(0, bond.binding)
    }
    releaseSum += captureRadiatedResidue
    activationSum += captureBoundResidue * 0.28
    metrics.baryonSamples = baryonSamples
    metrics.boundBaryons = boundBaryons
    metrics.baryonBinding = baryonSamples > 0 ? bindingSum / baryonSamples : 0
    metrics.bondBinding = liveBonds.length > 0 ? liveBonds.reduce((sum, bond) => sum + bond.binding, 0) / liveBonds.length : 0
    metrics.bondEnergy = liveBonds.length > 0 ? liveBonds.reduce((sum, bond) => sum + bond.boundEnergy, 0) / liveBonds.length : 0
    metrics.activationEnergy = activationSum
    metrics.releasedEnergy = releaseSum
}

function wrappedOffset(value: number, span: number) {
    if (value > span * 0.5) return value - span
    if (value < -span * 0.5) return value + span
    return value
}

function orbitalKindLabel(kind: OrbitalKind) {
    if (kind === '1s') return showOrbitalReference.value ? '1s' : 'core'
    if (kind === '2s') return showOrbitalReference.value ? '2s' : 'shell'
    if (kind === '2p') return showOrbitalReference.value ? '2p' : 'split'
    return 'n/a'
}

function orbitalKindForAtom(atom: AtomComposite): OrbitalKind {
    if (atom.electrons < 1 || atom.electronIds.length === 0) return 'none'
    const electron = particles[atom.electronIds[0]]
    if (!electron) return 'none'

    const branch = dominantBranch(electron.branchWeights)
    if (branch === 1 && electron.coherence > 0.56) return '2p'
    if (branch === 2 || electron.recurrence < 0.18) return '2s'
    return '1s'
}

function orbitalReferenceMeanRadius(atom: AtomComposite, kind: OrbitalKind) {
    if (kind === '1s') return atom.radius * 0.58
    if (kind === '2s') return atom.radius * 0.9
    if (kind === '2p') return atom.radius * 0.78
    return 0
}

function orbitalReferenceAxis(atom: AtomComposite) {
    const electron = particles[atom.electronIds[0]]
    return electron ? electron.theta + electron.sigma * 0.5 : atom.id * 0.43
}

function computeOrbitalMomentComparison() {
    if (!showOrbitalReference.value) {
        return {
            radialError: -1,
            lobeBalance: -1,
        }
    }

    let radialWeight = 0
    let radialError = 0
    let lobeWeight = 0
    let lobeBalance = 0
    const depthScale = projectionDepthScale()
    const currentMode = orbitalSampleMode.value

    for (const atom of atomComposites) {
        const kind = orbitalKindForAtom(atom)
        const referenceRadius = orbitalReferenceMeanRadius(atom, kind)
        if (kind === 'none' || referenceRadius <= 0) continue

        let sampleWeight = 0
        let sampleRadius = 0
        let positiveLobe = 0
        let negativeLobe = 0
        const axis = orbitalReferenceAxis(atom)
        const axisX = Math.cos(axis)
        const axisY = Math.sin(axis)

        for (const sample of orbitalSamples) {
            if (sample.atomId !== atom.id || sample.mode !== currentMode) continue
            const sampleLife = sample.mode === 'raw' ? RAW_ORBITAL_SAMPLE_LIFE : ORBITAL_SAMPLE_LIFE
            const weight = sample.weight * Math.max(0, 1 - sample.age / sampleLife)
            if (weight <= 0.002) continue
            const radius = Math.hypot(sample.dx, sample.dy, sample.dz * depthScale)
            sampleWeight += weight
            sampleRadius += radius * weight

            if (kind === '2p') {
                const signedLobe = sample.dx * axisX + sample.dy * axisY
                if (signedLobe >= 0) positiveLobe += weight
                else negativeLobe += weight
            }
        }

        if (sampleWeight <= 0) continue
        const meanRadius = sampleRadius / sampleWeight
        radialError += Math.abs(meanRadius - referenceRadius) / referenceRadius * sampleWeight
        radialWeight += sampleWeight

        if (kind === '2p' && positiveLobe + negativeLobe > 0) {
            lobeBalance += Math.min(positiveLobe, negativeLobe) / Math.max(positiveLobe, negativeLobe) * sampleWeight
            lobeWeight += sampleWeight
        }
    }

    return {
        radialError: radialWeight > 0 ? radialError / radialWeight : -1,
        lobeBalance: lobeWeight > 0 ? lobeBalance / lobeWeight : -1,
    }
}

function updateOrbitalMetrics() {
    metrics.orbitalSamples = orbitalSamples.filter(sample => sample.mode === orbitalSampleMode.value).length
    const counts: Record<OrbitalKind, number> = { none: 0, '1s': 0, '2s': 0, '2p': 0 }

    for (const atom of atomComposites) {
        const kind = orbitalKindForAtom(atom)
        counts[kind] += atom.electrons
    }

    let dominant: OrbitalKind = 'none'
    let dominantCount = 0
    for (const kind of ['1s', '2s', '2p'] as OrbitalKind[]) {
        if (counts[kind] > dominantCount) {
            dominant = kind
            dominantCount = counts[kind]
        }
    }
    metrics.orbitalState = dominantCount > 0 ? orbitalKindLabel(dominant) : 'n/a'
    const moments = computeOrbitalMomentComparison()
    metrics.orbitalRadialError = moments.radialError
    metrics.orbitalLobeBalance = moments.lobeBalance
}

function collectOrbitalSamples() {
    if (orbitalSamples.length > 0) {
        for (const sample of orbitalSamples) {
            sample.age += 1
            sample.weight *= 0.996
        }
        orbitalSamples = orbitalSamples.filter(sample => {
            const sampleLife = sample.mode === 'raw' ? RAW_ORBITAL_SAMPLE_LIFE : ORBITAL_SAMPLE_LIFE
            return sample.mode === orbitalSampleMode.value && sample.age < sampleLife && sample.weight > 0.016
        })
    }

    if (!isSmPreset() || atomComposites.length === 0) {
        if (!isSmPreset()) orbitalSamples = []
        updateOrbitalMetrics()
        return
    }

    const sampleMode = orbitalSampleMode.value
    for (const atom of atomComposites) {
        if (atom.stability < 0.18 || atom.electrons < 1) continue
        const kind = orbitalKindForAtom(atom)
        if (kind === 'none') continue

        for (const electronId of atom.electronIds) {
            const electron = particles[electronId]
            if (!electron || electron.smKind !== 'electron') continue

            const branch = electron.nil >= 0 ? (electron.nil as 0 | 1 | 2) : dominantBranch(electron.branchWeights)
            let dx = wrappedOffset(electron.x - atom.x, width)
            let dy = wrappedOffset(electron.y - atom.y, height)
            let dz = electron.z - atom.z

            if (sampleMode === 'guided') {
                const phase = electron.theta + electron.sigma * 0.5 + frame * 0.019
                const spinorMix = 0.12 + electron.coherence * 0.22 + (1 - electron.J) * 0.08
                const spread = atom.radius * (0.42 + branch * 0.16 + electron.coherence * 0.18) * settings.carrierSpread

                if (kind === '2p') {
                    const orientation = electron.theta + electron.entanglementPhase
                    const side = Math.cos(electron.sigma + frame * 0.011) >= 0 ? 1 : -1
                    dx += Math.cos(orientation) * spread * spinorMix * side
                    dy += Math.sin(orientation) * spread * spinorMix * side
                    dz += Math.sin(orientation + electron.sigma) * 0.12 * spinorMix
                } else if (kind === '2s') {
                    dx += Math.cos(phase) * spread * spinorMix * 0.64
                    dy += Math.sin(phase) * spread * spinorMix * 0.64
                    dz += Math.sin(phase * 2) * 0.1 * spinorMix
                } else {
                    dx += Math.cos(phase) * spread * spinorMix * 0.34
                    dy += Math.sin(phase) * spread * spinorMix * 0.34
                    dz += Math.sin(phase + electron.sigma) * 0.07 * spinorMix
                }
            }

            orbitalSamples.push({
                atomId: atom.id,
                dx,
                dy,
                dz,
                weight: clamp01(atom.stability * (0.34 + electron.coherence * 0.42 + (1 - electron.J) * 0.24)),
                age: 0,
                branch,
                theta: electron.theta,
                kind,
                mode: sampleMode,
            })
        }
    }

    if (orbitalSamples.length > MAX_ORBITAL_SAMPLES) {
        orbitalSamples.splice(0, orbitalSamples.length - MAX_ORBITAL_SAMPLES)
    }
    updateOrbitalMetrics()
}

function seedParticles() {
    const n = Math.max(20, Math.floor(settings.particleCount))
    const centerX = width * 0.5
    const centerY = height * 0.5
    const radius = Math.min(viewportWidth, viewportHeight) * 0.34
    const preset = activePreset.value

    for (let i = 0; i < n; i++) {
        const t = i / n
        const theta = TAU * t
        const sigma = wrapAngle(TAU * ((i * 0.38196601125) % 1) + Math.sin(i * 0.17) * 0.28)
        const arm = i % 3
        const smKind = presetIsSmSeed(preset) ? smKindForSeed(i) : 'generic'
        let lens = (arm === 0 ? -1 : arm === 1 ? 0 : 1) as -1 | 0 | 1
        lens = lensForSmKind(smKind, lens)
        const spatialAngle = TAU * ((i * 0.61803398875) % 1) + (Math.random() - 0.5) * 0.34
        const spatialRadius = radius * (0.12 + Math.sqrt(Math.random()) * 0.78)
        let z = Math.sin(theta * 2 + Math.random() * 0.5) * 0.36 + (Math.random() - 0.5) * 0.2
        let x = centerX + Math.cos(spatialAngle) * spatialRadius
        let y = centerY + Math.sin(spatialAngle) * spatialRadius

        if (preset === 'basins') {
            const basin = i % 3
            const a = TAU * basin / 3 + (Math.random() - 0.5) * 0.55
            const r = radius * (0.12 + Math.sqrt(Math.random()) * 0.4)
            x = centerX + Math.cos(a) * r + (Math.random() - 0.5) * radius * 0.42
            y = centerY + Math.sin(a) * r + (Math.random() - 0.5) * radius * 0.42
            z = (basin - 1) * 0.38 + (Math.random() - 0.5) * 0.28
        } else if (preset === 'composites') {
            const cluster = Math.floor(i / 3)
            const a = TAU * ((cluster * 0.38196601125) % 1)
            const r = radius * (0.1 + Math.sqrt((cluster % 31) / 31) * 0.72)
            x = centerX + Math.cos(a) * r + (arm - 1) * 10 + (Math.random() - 0.5) * 7
            y = centerY + Math.sin(a) * r + Math.sin(arm * TAU / 3) * 10 + (Math.random() - 0.5) * 7
            z = (arm - 1) * 0.22 + (Math.random() - 0.5) * 0.2
        } else if (preset === 'partition') {
            const side = i % 2 === 0 ? -1 : 1
            x = centerX + side * radius * 0.42 + (Math.random() - 0.5) * radius * 0.55
            y = centerY + Math.sin(theta * 2) * radius * 0.32 + (Math.random() - 0.5) * radius * 0.22
            z = side * 0.26 + (Math.random() - 0.5) * 0.34
        } else if (presetIsSmSeed(preset)) {
            const packet = Math.floor(i / 24)
            const slot = i % 24
            const packetAngle = TAU * ((packet * 0.38196601125) % 1)
            const packetRadius = preset === 'oneAtom' ? 0 : radius * (0.2 + ((packet % 11) / 11) * 0.58)
            const packetX = centerX + Math.cos(packetAngle) * packetRadius
            const packetY = centerY + Math.sin(packetAngle) * packetRadius
            const compact = preset === 'oneAtom' ? 0.58 : 1

            if (smKind === 'quarkR' || smKind === 'quarkG' || smKind === 'quarkB') {
                const colorAngle = TAU * (slot % 3) / 3 + packetAngle * 0.12
                x = packetX + Math.cos(colorAngle) * (12 + (packet % 3) * 2) * compact + (Math.random() - 0.5) * 5 * compact
                y = packetY + Math.sin(colorAngle) * (12 + (packet % 3) * 2) * compact + (Math.random() - 0.5) * 5 * compact
                z = (slot % 3 - 1) * 0.2 * compact + (Math.random() - 0.5) * 0.14 * compact
            } else if (smKind === 'electron' || smKind === 'positron') {
                const leptonAngle = packetAngle + (smKind === 'electron' ? -0.42 : 0.42)
                x = packetX + Math.cos(leptonAngle) * 34 * compact + (Math.random() - 0.5) * 10 * compact
                y = packetY + Math.sin(leptonAngle) * 34 * compact + (Math.random() - 0.5) * 10 * compact
                z = (smKind === 'electron' ? -0.28 : 0.28) * compact + (Math.random() - 0.5) * 0.16 * compact
            } else if (smKind === 'neutrino') {
                x = packetX + (Math.random() - 0.5) * 56 * compact
                y = packetY + (Math.random() - 0.5) * 56 * compact
                z = Math.sin(packetAngle + slot) * 0.34 * compact + (Math.random() - 0.5) * 0.12 * compact
            } else {
                const waveAngle = TAU * ((i * 0.754877666) % 1)
                const waveRadius = preset === 'oneAtom' ? 46 + slot * 0.8 : radius * (0.16 + Math.sqrt((slot + 1) / 24) * 0.72)
                x = centerX + Math.cos(waveAngle) * waveRadius + (Math.random() - 0.5) * 20 * compact
                y = centerY + Math.sin(waveAngle) * waveRadius + (Math.random() - 0.5) * 20 * compact
                z = Math.sin(waveAngle * 2) * 0.44 * compact + (Math.random() - 0.5) * 0.18 * compact
            }
        }

        const seedNilChance = preset === 'basins' ? 0.62 : preset === 'composites' ? 0.34 : presetIsSmSeed(preset) ? 0.82 : 0.2
        const smNil = smNilForKind(smKind, theta, sigma)
        const seededNil = smNil >= 0 ? smNil : Math.random() < seedNilChance ? basinFromCarrier(theta, sigma) : -1
        const seededCoherence = preset === 'oneAtom'
            ? smKind === 'photon' || smKind === 'gluon' ? 0.62 + Math.random() * 0.12 : 0.74 + Math.random() * 0.16
            : presetIsSmSeed(preset)
            ? smKind === 'photon' ? 0.58 + Math.random() * 0.18
                : smKind === 'gluon' ? 0.52 + Math.random() * 0.2
                    : seededNil >= 0 ? 0.58 + Math.random() * 0.18 : 0.36 + Math.random() * 0.18
            : seededNil >= 0 ? 0.42 + Math.random() * 0.22 : 0.25 + Math.random() * 0.2
        const seededRecurrence = seededNil >= 0 ? (preset === 'oneAtom' ? 0.28 + Math.random() * 0.22 : presetIsSmSeed(preset) ? 0.12 + Math.random() * 0.24 : Math.random() * 0.18) : 0
        const entangled = presetIsSmSeed(preset) ? smKind !== 'electron' && smKind !== 'positron' : i % 7 !== 0
        const entanglementId = entangled
            ? presetIsSmSeed(preset)
                ? Math.floor(i / (smKind === 'quarkR' || smKind === 'quarkG' || smKind === 'quarkB' ? 3 : 6))
                : Math.floor(i / 4)
            : -1
        const entanglementPhase = entangled ? wrapAngle((i % 4) * Math.PI * 0.5 + (Math.floor(i / 4) % 3) * 0.17) : 0
        let mode: Mode = Math.random() < 0.06 ? 2 : 0
        if (seededNil >= 0 && lens !== 0 && seededCoherence > 0.55 && seededRecurrence > 0.1) {
            mode = 1
        }
        if (presetIsSmSeed(preset)) {
            if (smKind === 'electron' || smKind === 'positron') mode = 1
            else if (smKind === 'quarkR' || smKind === 'quarkG' || smKind === 'quarkB') mode = 3
            else if (smKind === 'neutrino') mode = Math.random() < 0.35 ? 1 : 0
            else mode = 0
        }
        const gauge = smGaugeState(smKind, i, theta, sigma)

        particles.push({
            seedIndex: i,
            packetId: Math.floor(i / 24),
            x,
            y,
            z,
            vx: (Math.random() - 0.5) * (preset === 'oneAtom' ? 0.22 : 0.7),
            vy: (Math.random() - 0.5) * (preset === 'oneAtom' ? 0.22 : 0.7),
            vz: (Math.random() - 0.5) * (preset === 'oneAtom' ? 0.004 : 0.012),
            theta,
            phaseTotal: theta,
            theta0: theta,
            sigma,
            sigmaTotal: sigma,
            sigma0: sigma,
            lens,
            nil: seededNil,
            J: preset === 'oneAtom' ? 0.42 : 0.75,
            coherence: seededCoherence,
            recurrence: seededRecurrence,
            neutrality: 0,
            pressure: 0,
            massLoad: seededNil >= 0 ? 0.28 : 0.16,
            properTime: 0,
            timeRate: 1,
            entanglementId,
            entanglementPhase,
            branchWeights: branchWeightsFromCarrier(theta, sigma, seededNil),
            measurement: presetIsSmSeed(preset) && isChargedLeptonKind(smKind) ? 'unresolved' : mode === 1 ? 'anchored' : 'unresolved',
            lastMeasuredFrame: -999,
            smKind,
            electricCharge: gauge.electricCharge,
            hypercharge: gauge.hypercharge,
            weakIso: gauge.weakIso,
            color: gauge.color,
            chirality: gauge.chirality,
            spin: gauge.spin,
            gamma: 1,
            mode,
            age: 0,
            lastTurn: Math.floor(theta / TAU),
            lastSigmaTurn: Math.floor(sigma / TAU),
            radius: 2.1 + Math.random() * 1.4,
        })
    }

    captureInvariantBaseline()
    buildAtomComposites()
    applyMttClosureGradient()
    collectOrbitalSamples()
}

function resizeCanvas() {
    const canvas = canvasRef.value
    const shell = shellRef.value
    if (!canvas || !shell) return

    dpr = Math.min(window.devicePixelRatio || 1, 1.25)
    viewportWidth = Math.max(1, shell.clientWidth)
    viewportHeight = Math.max(1, shell.clientHeight)
    width = viewportWidth * ARENA_SCALE
    height = viewportHeight * ARENA_SCALE
    canvas.width = Math.floor(viewportWidth * dpr)
    canvas.height = Math.floor(viewportHeight * dpr)
    canvas.style.width = `${viewportWidth}px`
    canvas.style.height = `${viewportHeight}px`
    ctx = canvas.getContext('2d')
    if (ctx) ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
    if (lookingGlass.x === 0 && lookingGlass.y === 0) {
        lookingGlass.x = width * 0.5
        lookingGlass.y = height * 0.5
    }
    if (particles.length === 0 && !manualEmptyWorld) seedParticles()
}

function clampZoom(value: number) {
    return Math.max(0.35, Math.min(3, value))
}

function canvasPointFromEvent(event: PointerEvent | WheelEvent) {
    const canvas = canvasRef.value
    const rect = canvas?.getBoundingClientRect()
    return {
        x: event.clientX - (rect?.left ?? 0),
        y: event.clientY - (rect?.top ?? 0),
    }
}

function screenToWorld(x: number, y: number) {
    return {
        x: (x - viewportWidth * 0.5 - camera.x) / camera.zoom + width * 0.5,
        y: (y - viewportHeight * 0.5 - camera.y) / camera.zoom + height * 0.5,
    }
}

function setCameraZoom(nextZoom: number, focusX = viewportWidth * 0.5, focusY = viewportHeight * 0.5) {
    const before = screenToWorld(focusX, focusY)
    camera.zoom = clampZoom(nextZoom)
    camera.x = focusX - viewportWidth * 0.5 - (before.x - width * 0.5) * camera.zoom
    camera.y = focusY - viewportHeight * 0.5 - (before.y - height * 0.5) * camera.zoom
}

function zoomBy(factor: number) {
    setCameraZoom(camera.zoom * factor)
}

function resetCamera() {
    camera.zoom = 1
    camera.x = 0
    camera.y = 0
}

function applyCameraTransform() {
    if (!ctx) return
    ctx.translate(viewportWidth * 0.5 + camera.x, viewportHeight * 0.5 + camera.y)
    ctx.scale(camera.zoom, camera.zoom)
    ctx.translate(-width * 0.5, -height * 0.5)
}

function wrapAngle(value: number) {
    let v = value % TAU
    if (v < 0) v += TAU
    return v
}

function signedAngle(value: number) {
    let v = (value + Math.PI) % TAU
    if (v < 0) v += TAU
    return v - Math.PI
}

function clamp01(value: number) {
    return Math.max(0, Math.min(1, value))
}

function scoreStatus(score: number, passAt: number, warnAt: number): LedgerStatus {
    if (score >= passAt) return 'pass'
    if (score >= warnAt) return 'warn'
    return 'fail'
}

function costStatus(cost: number, passBelow: number, warnBelow: number): LedgerStatus {
    if (cost <= passBelow) return 'pass'
    if (cost <= warnBelow) return 'warn'
    return 'fail'
}

function formatSignedCharge(value: number) {
    if (Math.abs(value) < 0.001) return '0.000'
    return `${value > 0 ? '+' : ''}${value.toFixed(3)}`
}

function basinFromTheta(theta: number): 0 | 1 | 2 {
    return Math.floor(wrapAngle(theta) / (TAU / 3)) as 0 | 1 | 2
}

function basinFromCarrier(theta: number, sigma: number): 0 | 1 | 2 {
    return basinFromTheta(theta + sigma * 0.5)
}

function wrapBranch(value: number): 0 | 1 | 2 {
    const branch = ((value % 3) + 3) % 3
    return branch as 0 | 1 | 2
}

function normalizeBranchWeights(weights: BranchWeights): BranchWeights {
    const total = Math.max(0.0001, weights[0] + weights[1] + weights[2])
    return [weights[0] / total, weights[1] / total, weights[2] / total]
}

function branchWeightsFromCarrier(theta: number, sigma: number, nil: -1 | 0 | 1 | 2): BranchWeights {
    const carrierBranch = basinFromCarrier(theta, sigma)
    const weights: BranchWeights = [0.12, 0.12, 0.12]
    weights[carrierBranch] += 0.52
    if (nil >= 0) {
        const nilBranch = nil as 0 | 1 | 2
        weights[nilBranch] += 0.34
    }
    return normalizeBranchWeights(weights)
}

function dominantBranch(weights: BranchWeights): 0 | 1 | 2 {
    if (weights[1] > weights[0] && weights[1] >= weights[2]) return 1
    if (weights[2] > weights[0] && weights[2] > weights[1]) return 2
    return 0
}

function blendBranchWeights(current: BranchWeights, target: BranchWeights, gain: number): BranchWeights {
    const g = clamp01(gain)
    return normalizeBranchWeights([
        current[0] * (1 - g) + target[0] * g,
        current[1] * (1 - g) + target[1] * g,
        current[2] * (1 - g) + target[2] * g,
    ])
}

function pullBranchWeights(current: BranchWeights, branch: 0 | 1 | 2, gain: number): BranchWeights {
    const target: BranchWeights = [0.08, 0.08, 0.08]
    target[branch] = 0.84
    return blendBranchWeights(current, target, gain)
}

function computeBranchWeights(p: ProtoParticle, group?: EntanglementSummary): BranchWeights {
    const carrierBranch = basinFromCarrier(p.theta, p.sigma)
    const temperature = 0.16 + settings.measurementStrength * 0.16
    const raw: BranchWeights = [0, 0, 0]

    for (let i = 0; i < 3; i++) {
        const branch = i as 0 | 1 | 2
        const carrierCost = branch === carrierBranch ? 0.04 : 0.46
        const nilCost = p.nil === -1 ? 0.18 : p.nil === branch ? 0.03 : 0.5
        const entangledCost = group ? (branch === group.selectedNil ? 0.02 : 0.34 * group.coherence * settings.entanglementStrength) : 0
        const chargeCost = p.lens === 0 ? (branch === 1 ? 0.04 : 0.14) : (branch === 1 ? 0.18 : 0.08)
        const stressCost = p.J * 0.2 + p.pressure * 0.14
        raw[branch] = Math.exp(-(carrierCost + nilCost + entangledCost + chargeCost + stressCost) / Math.max(0.06, temperature))
    }

    return normalizeBranchWeights(raw)
}

function buildEntanglementState(): EntanglementState {
    const summaries = new Map<number, EntanglementSummary>()
    const members = new Map<number, number[]>()

    for (let i = 0; i < particles.length; i++) {
        const p = particles[i]
        if (p.entanglementId < 0) continue

        let summary = summaries.get(p.entanglementId)
        if (!summary) {
            summary = {
                id: p.entanglementId,
                count: 0,
                phaseX: 0,
                phaseY: 0,
                sigmaX: 0,
                sigmaY: 0,
                lensSum: 0,
                nilCounts: [0, 0, 0],
                anchorCount: 0,
                coherenceSum: 0,
                meanPhase: 0,
                meanSigma: 0,
                coherence: 0,
                selectedNil: 0,
            }
            summaries.set(p.entanglementId, summary)
            members.set(p.entanglementId, [])
        }

        const carrierPhase = wrapAngle(p.theta - p.entanglementPhase)
        const carrierSigma = wrapAngle(p.sigma + p.entanglementPhase * 0.5)
        const weight = 0.25 + p.coherence
        summary.count += 1
        summary.phaseX += Math.cos(carrierPhase) * weight
        summary.phaseY += Math.sin(carrierPhase) * weight
        summary.sigmaX += Math.cos(carrierSigma) * weight
        summary.sigmaY += Math.sin(carrierSigma) * weight
        summary.lensSum += p.lens
        summary.coherenceSum += p.coherence
        if (p.nil >= 0) {
            const nilBranch = p.nil as 0 | 1 | 2
            summary.nilCounts[nilBranch] += 1
        }
        if (p.mode === 1 || p.mode === 3) summary.anchorCount += 1
        members.get(p.entanglementId)?.push(i)
    }

    for (const summary of summaries.values()) {
        summary.meanPhase = wrapAngle(Math.atan2(summary.phaseY, summary.phaseX))
        summary.meanSigma = wrapAngle(Math.atan2(summary.sigmaY, summary.sigmaX))
        const phaseOrder = Math.min(1, Math.hypot(summary.phaseX, summary.phaseY) / Math.max(1, summary.count))
        const anchorOrder = summary.anchorCount / Math.max(1, summary.count)
        const coherenceOrder = summary.coherenceSum / Math.max(1, summary.count)
        summary.coherence = clamp01(phaseOrder * 0.42 + anchorOrder * 0.24 + coherenceOrder * 0.34)

        let selectedNil = basinFromCarrier(summary.meanPhase, summary.meanSigma)
        let selectedCount = -1
        for (let i = 0; i < 3; i++) {
            if (summary.nilCounts[i] > selectedCount) {
                selectedNil = i as 0 | 1 | 2
                selectedCount = summary.nilCounts[i]
            }
        }
        summary.selectedNil = selectedNil
    }

    return { summaries, members }
}

function lensCompatibility(a: ProtoParticle, b: ProtoParticle) {
    if (a.lens === 0 || b.lens === 0) return 0.18
    if (a.lens + b.lens === 0) return 1
    return -0.75
}

function hasStableCharge(p: ProtoParticle) {
    return p.lens === -1 || p.lens === 1
}

function projectionDepthScale() {
    return Math.min(viewportWidth, viewportHeight) * 0.13 * settings.projectionDepth * (0.7 + settings.upperWorldCoupling * 0.3)
}

function projectPoint(x: number, y: number, z: number) {
    const parallax = z * settings.projectionDepth * (0.82 + settings.upperWorldCoupling * 0.18)
    return {
        x: x + parallax * 42,
        y: y - parallax * 20,
        scale: Math.max(0.68, Math.min(1.34, 1 + parallax * 0.18)),
    }
}

function projectParticle(p: ProtoParticle) {
    return projectPoint(p.x, p.y, p.z)
}

function emptyMeasurementProfile(): MeasurementProfile {
    return { gain: 0, kind: measurementKind.value }
}

function measurementProfileForParticle(p: ProtoParticle): MeasurementProfile {
    if (!lookingGlassEnabled.value || (!lookingGlass.active && frame > lookingGlass.pulseUntil)) return emptyMeasurementProfile()
    const projected = projectParticle(p)
    const radius = Math.max(1, settings.measurementRadius)

    if (measurementKind.value === 'split') {
        const split = radius * 0.48
        const leftDistance = Math.hypot(projected.x - (lookingGlass.x - split), projected.y - lookingGlass.y)
        const rightDistance = Math.hypot(projected.x - (lookingGlass.x + split), projected.y - lookingGlass.y)
        const leftCloseness = leftDistance < radius ? 1 - leftDistance / radius : 0
        const rightCloseness = rightDistance < radius ? 1 - rightDistance / radius : 0
        const closeness = Math.max(leftCloseness, rightCloseness)
        if (closeness <= 0) return emptyMeasurementProfile()
        return {
            gain: closeness * closeness * settings.measurementStrength * 1.08,
            kind: 'split',
            branch: leftCloseness >= rightCloseness ? 0 : 2,
        }
    }

    const dx = projected.x - lookingGlass.x
    const dy = projected.y - lookingGlass.y
    const distance = Math.hypot(dx, dy)
    if (distance >= radius) return emptyMeasurementProfile()

    const closeness = 1 - distance / radius
    const baseGain = closeness * closeness * settings.measurementStrength

    if (measurementKind.value === 'interference') {
        return { gain: baseGain * 0.62, kind: 'interference' }
    }

    if (measurementKind.value === 'whichPath') {
        return {
            gain: baseGain * 1.28,
            kind: 'whichPath',
            branch: projected.x < lookingGlass.x ? 0 : 2,
        }
    }

    return { gain: baseGain, kind: 'projector' }
}

function constrainEntangledPartners(sourceIndex: number, source: ProtoParticle, selectedBranch: 0 | 1 | 2, gain: number, members: Map<number, number[]>) {
    if (source.entanglementId < 0 || settings.entanglementStrength <= 0) return
    const groupMembers = members.get(source.entanglementId)
    if (!groupMembers) return

    let emitted = 0
    for (const index of groupMembers) {
        if (index === sourceIndex) continue
        const partner = particles[index]
        const phaseOffset = Math.round(signedAngle(partner.entanglementPhase - source.entanglementPhase) / (TAU / 3))
        const partnerBranch = wrapBranch(selectedBranch + phaseOffset)
        const pull = clamp01(gain * settings.entanglementStrength * 0.34)

        partner.branchWeights = pullBranchWeights(partner.branchWeights, partnerBranch, pull)
        partner.coherence = clamp01(partner.coherence + gain * 0.035 * settings.entanglementStrength)
        partner.J = clamp01(partner.J - gain * 0.028 * settings.entanglementStrength)
        partner.measurement = partner.mode === 1 || partner.mode === 3 ? 'anchored' : 'focused'
        partner.lastMeasuredFrame = frame

        if (partner.nil === -1 && partner.J < settings.nilThreshold + 0.18) {
            partner.nil = partnerBranch
        } else if (partner.nil >= 0 && partner.nil !== partnerBranch) {
            partner.pressure = clamp01(partner.pressure + gain * 0.07)
        }

        if (emitted < 2 && gain > 0.42) {
            emitProjectionEvent(partner, 282, 0.28 + gain * 0.32)
            emitted += 1
        }
    }
}

function applyLookingGlassMeasurement(p: ProtoParticle, index: number, profile: MeasurementProfile, group: EntanglementSummary | undefined, members: Map<number, number[]>) {
    const gain = profile.gain
    if (gain <= 0) return false

    const targetWeights = computeBranchWeights(p, group)
    const branchGain = profile.kind === 'interference'
        ? Math.min(1, 0.12 + gain * 0.18)
        : Math.min(1, 0.36 + gain * (profile.kind === 'whichPath' || profile.kind === 'split' ? 0.72 : 0.48))
    p.branchWeights = blendBranchWeights(p.branchWeights, targetWeights, branchGain)
    p.measurement = 'focused'
    p.lastMeasuredFrame = frame

    if (profile.branch !== undefined) {
        p.branchWeights = pullBranchWeights(p.branchWeights, profile.branch, Math.min(1, gain * 0.72))
    }

    const selectedBranch = profile.branch ?? dominantBranch(p.branchWeights)
    const entangledSupport = group ? group.coherence * settings.entanglementStrength * 0.12 : 0

    if (isSmPreset() && isChargedLeptonKind(p.smKind) && profile.kind !== 'interference') {
        p.nil = selectedBranch
        p.mode = 1
        p.measurement = 'anchored'
        p.lastMeasuredFrame = frame
        p.coherence = clamp01(p.coherence + gain * 0.24 + entangledSupport * 0.5)
        p.recurrence = clamp01(p.recurrence + gain * 0.2)
        p.J = clamp01(p.J - gain * 0.12)
        p.pressure = clamp01(p.pressure + gain * (profile.kind === 'whichPath' || profile.kind === 'split' ? 0.03 : 0.012))
        p.vx *= 0.82
        p.vy *= 0.82
        p.vz *= 0.9
        emitProjectionEvent(p, p.electricCharge < 0 ? 186 : 350, 0.92 + gain * 0.42)
        constrainEntangledPartners(index, p, selectedBranch, gain, members)
        return true
    }

    const operatorSlack = profile.kind === 'interference' ? -0.08 : profile.kind === 'whichPath' ? 0.08 : profile.kind === 'split' ? 0.12 : 0
    const admissible = p.J < settings.nilThreshold + 0.12 + gain * 0.22 + entangledSupport + operatorSlack
        && p.coherence + gain * 0.32 + entangledSupport > (profile.kind === 'interference' ? 0.22 : 0.34)

    if (profile.kind === 'interference') {
        p.coherence = clamp01(p.coherence + gain * 0.12 + entangledSupport * 0.35)
        p.J = clamp01(p.J - gain * 0.035)
        p.phaseTotal += Math.sin(signedAngle(p.sigma - p.theta)) * gain * 0.008
        if (gain > 0.45) emitProjectionEvent(p, 212, 0.24 + gain * 0.24)
        return false
    }

    if (!admissible) {
        if (profile.kind === 'whichPath' || profile.kind === 'split') {
            p.pressure = clamp01(p.pressure + gain * 0.08)
            p.coherence = clamp01(p.coherence - gain * 0.025)
        }
        return false
    }

    const wasProjected = p.mode === 1 || p.mode === 3
    p.nil = selectedBranch
    const coherenceGain = profile.kind === 'whichPath' || profile.kind === 'split' ? gain * 0.09 : gain * 0.18
    p.coherence = clamp01(p.coherence + coherenceGain + entangledSupport)
    p.recurrence = clamp01(p.recurrence + gain * 0.16)
    p.J = clamp01(p.J - gain * (profile.kind === 'whichPath' || profile.kind === 'split' ? 0.045 : 0.08))

    if (hasStableCharge(p)) {
        p.mode = 1
    } else if (p.neutrality > 0.42 || (group && Math.abs(group.lensSum) <= Math.max(1, group.count * 0.28))) {
        p.mode = 3
    }

    if (p.mode === 1 || p.mode === 3) {
        p.measurement = 'anchored'
        if (!wasProjected) emitProjectionEvent(p, p.mode === 1 ? 176 : 48, 0.86 + gain * 0.3)
    }

    constrainEntangledPartners(index, p, selectedBranch, gain, members)
    return p.mode === 1 || p.mode === 3
}

function addStructureForce(index: number, fx: Float32Array, fy: Float32Array, fz: Float32Array, target: { x: number, y: number, z: number }, strength: number) {
    const p = particles[index]
    if (!p) return
    const dx = wrappedOffset(target.x - p.x, width)
    const dy = wrappedOffset(target.y - p.y, height)
    const dz = target.z - p.z
    fx[index] += dx * strength
    fy[index] += dy * strength
    fz[index] += dz * strength
}

function addGroupForce(indices: number[], fx: Float32Array, fy: Float32Array, fz: Float32Array, dx: number, dy: number, dz: number, strength: number) {
    const live = indices.filter(index => particles[index])
    if (live.length === 0) return
    const scale = strength / live.length
    for (const index of live) {
        fx[index] += dx * scale
        fy[index] += dy * scale
        fz[index] += dz * scale
    }
}

function emptyPhysicsEnergyLedger(): PhysicsEnergyLedger {
    return {
        kinetic: 0,
        coulomb: 0,
        confinement: 0,
        nuclear: 0,
        pauli: 0,
        orbital: 0,
        bond: 0,
        photon: 0,
        total: 0,
    }
}

function addNormalizedPairForce(fx: Float32Array, fy: Float32Array, fz: Float32Array, i: number, j: number, ux: number, uy: number, uz: number, force: number, depthScale: number) {
    fx[i] += ux * force
    fy[i] += uy * force
    fz[i] += uz * force / depthScale
    fx[j] -= ux * force
    fy[j] -= uy * force
    fz[j] -= uz * force / depthScale
}

function photonInternalLedgerEnergy(p: ProtoParticle) {
    if (p.smKind !== 'photon') return 0
    const captureBoost = p.entanglementId === CAPTURE_PHOTON_ENTANGLEMENT_ID ? 0.12 : 0.04
    return captureBoost + p.coherence * 0.16 + p.recurrence * 0.08 + Math.max(0, 1 - p.J) * 0.05
}

function applyPhysicsLedgerPairTerms(ledger: PhysicsEnergyLedger, fx: Float32Array, fy: Float32Array, fz: Float32Array, i: number, j: number, pairStride: number, depthScale: number) {
    if (pairStride > 1 && ((i * 31 + j * 17 + frame) % pairStride !== 0)) return

    const a = particles[i]
    const b = particles[j]
    let dx = b.x - a.x
    let dy = b.y - a.y
    const dzRaw = b.z - a.z

    if (dx > width * 0.5) dx -= width
    else if (dx < -width * 0.5) dx += width
    if (dy > height * 0.5) dy -= height
    else if (dy < -height * 0.5) dy += height

    const dz = dzRaw * depthScale
    const d2 = dx * dx + dy * dy + dz * dz
    if (d2 < 0.0001) return

    const distance = Math.sqrt(d2)
    const ux = dx / distance
    const uy = dy / distance
    const uz = dz / distance
    const forceScale = physicsLedgerEnabled.value ? settings.physicsLedgerStrength : 0
    const energyWeight = Math.max(1, pairStride)

    const chargeProduct = a.electricCharge * b.electricCharge
    if (Math.abs(chargeProduct) > 0.001 && distance < Math.min(width, height) * 0.42) {
        const emRange = Math.max(36, 62 * settings.carrierSpread)
        const atten = 1 / (1 + distance / emRange)
        const coulombUnit = 0.18 * settings.lensStrength * atten
        ledger.coulomb += coulombUnit * chargeProduct * energyWeight
        if (forceScale > 0) {
            const force = -chargeProduct * atten * atten * (0.026 + settings.lensStrength * 0.012) * forceScale
            addNormalizedPairForce(fx, fy, fz, i, j, ux, uy, uz, force, depthScale)
        }
    }

    if (isQuarkKind(a.smKind) && isQuarkKind(b.smKind) && a.entanglementId >= 0 && a.entanglementId === b.entanglementId) {
        const colorComplement = a.color !== b.color ? 1 : 0.42
        const stringRange = Math.max(14, baryonSpreadLimit() * 0.7)
        const stretch = Math.max(0, distance - stringRange * 0.42) / stringRange
        ledger.confinement += colorComplement * (0.08 + stretch * 0.24) * settings.sourceCoupling * energyWeight
        if (forceScale > 0 && stretch > 0) {
            const force = colorComplement * clamp01(stretch) * (0.03 + settings.sourceCoupling * 0.012) * forceScale
            addNormalizedPairForce(fx, fy, fz, i, j, ux, uy, uz, force, depthScale)
        }
    }

    if (isFermionKind(a.smKind) && a.smKind === b.smKind && Math.abs(a.electricCharge - b.electricCharge) < 0.001) {
        const pauliRange = Math.max(10, Math.min(mttOccupancyCellSize(a), mttOccupancyCellSize(b)) * 0.9)
        const closeness = clamp01(1 - distance / pauliRange)
        if (closeness > 0) {
            const overlap = mttSpinorStateOverlap(a, b)
            const pauli = overlap * closeness * closeness * (0.16 + settings.capacity * 0.08)
            ledger.pauli += pauli * energyWeight
            if (forceScale > 0 && overlap > 0.08) {
                const force = -overlap * closeness * (0.026 + settings.capacity * 0.015) * forceScale
                addNormalizedPairForce(fx, fy, fz, i, j, ux, uy, uz, force, depthScale)
            }
        }
    }
}

function applyPhysicsLedgerNuclearTerms(ledger: PhysicsEnergyLedger, fx: Float32Array, fy: Float32Array, fz: Float32Array, depthScale: number) {
    const baryons = collectFreeBaryonCandidates(new Set())
    if (baryons.length < 2) return

    const range = residualNuclearRange()
    const core = range * 0.34
    const forceScale = physicsLedgerEnabled.value ? settings.physicsLedgerStrength : 0

    for (let i = 0; i < baryons.length; i++) {
        const a = baryons[i]
        for (let j = i + 1; j < baryons.length; j++) {
            const b = baryons[j]
            let dx = wrappedOffset(b.center.x - a.center.x, width)
            let dy = wrappedOffset(b.center.y - a.center.y, height)
            const dzRaw = b.center.z - a.center.z
            const dz = dzRaw * depthScale
            const distance = Math.max(1, Math.hypot(dx, dy, dz))
            if (distance > range * 2.4) continue

            const ux = dx / distance
            const uy = dy / distance
            const uz = dzRaw / distance
            const stability = Math.sqrt(a.stability * b.stability)
            const attractiveWell = -stability * Math.exp(-distance / range) * (0.42 + settings.compositeBias * 0.08)
            const hardCore = distance < core ? ((core - distance) / core) ** 2 * (0.52 + settings.capacity * 0.12) : 0
            const protonRepulsion = a.charge * b.charge > 0
                ? a.charge * b.charge * 0.08 / (1 + distance / Math.max(1, range * 0.45))
                : 0
            ledger.nuclear += attractiveWell + hardCore + protonRepulsion

            if (forceScale > 0) {
                const attraction = stability * Math.exp(-distance / range) * (0.018 + settings.compositeBias * 0.006)
                const repulsion = distance < core ? ((core - distance) / core) * (0.05 + settings.capacity * 0.016) : 0
                const coulomb = protonRepulsion * 0.04
                const force = (attraction - repulsion - coulomb) * forceScale
                if (Math.abs(force) > 0.0005) {
                    addGroupForce(a.indices, fx, fy, fz, ux, uy, uz, force)
                    addGroupForce(b.indices, fx, fy, fz, -ux, -uy, -uz, force)
                }
            }
        }
    }
}

function applyPhysicsLedgerOrbitalTerms(ledger: PhysicsEnergyLedger, fx: Float32Array, fy: Float32Array, fz: Float32Array, depthScale: number) {
    const baryons = collectFreeBaryonCandidates(new Set())
    const protons = baryons.filter(candidate => candidate.kind === 'proton')
    if (protons.length === 0) return

    const neutrons = baryons.filter(candidate => candidate.kind === 'neutron')
    const forceScale = physicsLedgerEnabled.value ? settings.physicsLedgerStrength : 0
    const captureRange = electronCaptureRadius() * (2.15 + settings.carrierSpread * 0.12)
    const nucleonRange2 = nucleonCaptureRadius() ** 2

    for (const proton of protons) {
        let nearestNeutron: BaryonCandidate | null = null
        let nearestNeutronDistance = Number.POSITIVE_INFINITY
        for (const neutron of neutrons) {
            const d2 = pointDistance2(proton.center, neutron.center)
            if (d2 > nucleonRange2 || d2 >= nearestNeutronDistance) continue
            nearestNeutron = neutron
            nearestNeutronDistance = d2
        }

        const nucleusIds = [...proton.indices, ...(nearestNeutron ? nearestNeutron.indices : [])]
        const nucleusCenter = compositePosition(nucleusIds)
        const nucleusVelocity = meanVelocity(nucleusIds)
        const chargeZ = Math.max(1, Math.round(proton.charge))

        for (let electronIndex = 0; electronIndex < particles.length; electronIndex++) {
            const electron = particles[electronIndex]
            if (!electron || electron.smKind !== 'electron') continue

            const dx = wrappedOffset(electron.x - nucleusCenter.x, width)
            const dy = wrappedOffset(electron.y - nucleusCenter.y, height)
            const dzRaw = electron.z - nucleusCenter.z
            const dz = dzRaw * depthScale
            const distance = Math.max(1, Math.hypot(dx, dy, dz))
            if (distance > captureRange) continue

            const ux = dx / distance
            const uy = dy / distance
            const uz = dzRaw / distance
            const shellScale = Math.max(24, electronCaptureRadius() * (0.58 + settings.carrierSpread * 0.05))
            const pressureScale = Math.max(7, shellScale * (0.22 + settings.capacity * 0.035))
            const vev = mttVacuumExpectation(electron)
            const closureSupport = clamp01(electron.coherence * 0.42 + (1 - electron.J) * 0.34 + electron.recurrence * 0.24)
            const alpha = chargeZ * proton.stability * (0.24 + settings.lensStrength * 0.07 + settings.sourceCoupling * 0.035)
            const quantumPressure = (0.12 + settings.capacity * 0.045 + vev * 0.07 + (1 - closureSupport) * 0.045)

            const relVx = electron.vx - nucleusVelocity.vx
            const relVy = electron.vy - nucleusVelocity.vy
            const relVz = (electron.vz - nucleusVelocity.vz) * depthScale
            const radialVelocity = relVx * ux + relVy * uy + relVz * (dz / distance)
            const relativeSpeed2 = relVx * relVx + relVy * relVy + relVz * relVz
            const tangentialSpeed = Math.sqrt(Math.max(0, relativeSpeed2 - radialVelocity * radialVelocity))
            const flowSupport = clamp01(tangentialSpeed / Math.max(0.08, 0.34 + alpha * 0.22))

            const attractionEnergy = -alpha / (1 + distance / shellScale)
            const pressureEnergy = quantumPressure / (1 + distance / pressureScale) ** 2
            const flowEnergyCredit = flowSupport * closureSupport * 0.035
            ledger.orbital += attractionEnergy + pressureEnergy - flowEnergyCredit

            if (forceScale <= 0) continue
            const attraction = alpha / shellScale / (1 + distance / shellScale) ** 2
            const pressure = 2 * quantumPressure / pressureScale / (1 + distance / pressureScale) ** 3
            const radialForce = (pressure - attraction) * forceScale * (0.7 + proton.stability * 0.45)

            fx[electronIndex] += ux * radialForce
            fy[electronIndex] += uy * radialForce
            fz[electronIndex] += uz * radialForce
            addGroupForce(nucleusIds, fx, fy, fz, -ux, -uy, -uz, radialForce)

            const radialDamping = clamp01(Math.abs(radialVelocity) / 1.8) * closureSupport * 0.0025 * forceScale
            electron.vx -= ux * radialVelocity * radialDamping
            electron.vy -= uy * radialVelocity * radialDamping
            electron.vz -= (dz / distance) * radialVelocity * radialDamping / depthScale
        }
    }
}

function applyPhysicsLedgerBondTerms(ledger: PhysicsEnergyLedger, fx: Float32Array, fy: Float32Array, fz: Float32Array, depthScale: number) {
    if (declaredBonds.length === 0) return
    const forceScale = physicsLedgerEnabled.value ? settings.physicsLedgerStrength : 0

    for (const bond of declaredBonds) {
        const left = declaredAtomById(bond.atomIds[0])
        const right = declaredAtomById(bond.atomIds[1])
        if (!left || !right) continue

        const energy = declaredBondClosureEnergy(bond)
        ledger.bond += energy.bound - energy.free

        if (forceScale <= 0) continue
        const vector = declaredAtomVector(left, right, depthScale)
        const { ux, uy, uz } = declaredAtomUnitDirection(left, right, vector)
        const idealLength = declaredBondIdealLength(bond)
        const restError = vector.distance - idealLength
        const spring = clamp01(Math.abs(restError) / Math.max(1, idealLength)) * (0.026 + energy.stability * 0.018) * forceScale
        if (restError > 0 && energy.binding > 0.02) {
            addGroupForce(left.nucleusIds, fx, fy, fz, ux, uy, uz, spring)
            addGroupForce(right.nucleusIds, fx, fy, fz, -ux, -uy, -uz, spring)
        } else if (restError < 0) {
            addGroupForce(left.nucleusIds, fx, fy, fz, -ux, -uy, -uz, spring)
            addGroupForce(right.nucleusIds, fx, fy, fz, ux, uy, uz, spring)
        }
    }
}

function applyPhysicsEnergyLedgerForces(fx: Float32Array, fy: Float32Array, fz: Float32Array, depthScale: number, pairStride: number) {
    const ledger = emptyPhysicsEnergyLedger()
    if (!isSmPreset()) return ledger

    const n = particles.length
    for (let i = 0; i < n; i++) {
        const p = particles[i]
        ledger.kinetic += particleKineticEnergy(p, depthScale, inertialMass(p))
        ledger.photon += photonInternalLedgerEnergy(p)
    }

    for (let i = 0; i < n; i++) {
        for (let j = i + 1; j < n; j++) {
            applyPhysicsLedgerPairTerms(ledger, fx, fy, fz, i, j, pairStride, depthScale)
        }
    }

    applyPhysicsLedgerNuclearTerms(ledger, fx, fy, fz, depthScale)
    applyPhysicsLedgerOrbitalTerms(ledger, fx, fy, fz, depthScale)
    applyPhysicsLedgerBondTerms(ledger, fx, fy, fz, depthScale)
    ledger.total = ledger.kinetic + ledger.coulomb + ledger.confinement + ledger.nuclear + ledger.pauli + ledger.orbital + ledger.bond + ledger.photon
    return ledger
}

function updatePhysicsLedgerMetrics(ledger: PhysicsEnergyLedger) {
    if (physicsEnergyBaseline === null || frame <= physicsEnergyBaselineWarmupUntil) physicsEnergyBaseline = ledger.total
    metrics.ledgerTotalEnergy = ledger.total
    metrics.ledgerEnergyDrift = ledger.total - physicsEnergyBaseline
    metrics.ledgerCoulombEnergy = ledger.coulomb
    metrics.ledgerConfinementEnergy = ledger.confinement
    metrics.ledgerNuclearEnergy = ledger.nuclear
    metrics.ledgerPauliEnergy = ledger.pauli
    metrics.ledgerOrbitalEnergy = ledger.orbital
    metrics.ledgerBondEnergy = ledger.bond
    metrics.ledgerPhotonEnergy = ledger.photon
}

function applyBoundAtomReturnFlow(atom: AtomComposite) {
    const live = [...atom.nucleusIds, ...atom.electronIds].filter(index => particles[index])
    if (live.length < 2 || atom.stability < 0.2 || atom.electrons === 0) return

    let massSum = 0
    let vx = 0
    let vy = 0
    let vz = 0
    for (const index of live) {
        const p = particles[index]
        const mass = inertialMass(p)
        massSum += mass
        vx += p.vx * mass
        vy += p.vy * mass
        vz += p.vz * mass
    }

    if (massSum <= 0) return

    vx /= massSum
    vy /= massSum
    vz /= massSum
    const speed = Math.hypot(vx, vy, vz * projectionDepthScale())
    if (speed < 0.004) return

    const isotopeSupport = atom.protons === 1 && atom.electrons === 1 ? 1 : 0.55
    const returnFlow = atom.stability * isotopeSupport * (0.01 + settings.upperWorldCoupling * 0.004 + settings.sourceCoupling * 0.003)
    for (const index of live) {
        const p = particles[index]
        p.vx -= vx * returnFlow
        p.vy -= vy * returnFlow
        p.vz -= vz * returnFlow * 0.65
        p.recurrence = clamp01(p.recurrence + returnFlow * 0.012)
    }
}

function isDeclaredBondElectron(index: number) {
    return declaredBonds.some(bond => bond.electronIds.includes(index))
}

function applyDeclaredStructureForces(fx: Float32Array, fy: Float32Array, fz: Float32Array, depthScale: number) {
    if (declaredAtoms.length === 0) return

    for (const atom of declaredAtoms) {
        const center = declaredAtomCenter(atom)
        atom.x = center.x
        atom.y = center.y
        atom.z = center.z
        const nucleonCount = Math.max(1, atom.protons + atom.neutrons)
        const nucleusTargetRadius = 2.8 + Math.sqrt(nucleonCount) * 2.1

        for (let i = 0; i < atom.nucleusIds.length; i++) {
            const targetAngle = atom.id * 0.001 + i * TAU / Math.max(3, atom.nucleusIds.length)
            addStructureForce(atom.nucleusIds[i], fx, fy, fz, {
                x: center.x + Math.cos(targetAngle) * nucleusTargetRadius,
                y: center.y + Math.sin(targetAngle) * nucleusTargetRadius,
                z: center.z + Math.sin(targetAngle * 2) * 0.04,
            }, 0.024)
        }

        for (let i = 0; i < atom.electronIds.length; i++) {
            const electronIndex = atom.electronIds[i]
            const electron = particles[electronIndex]
            if (!electron) continue
            const shellPhase = electron.theta + electron.sigma * 0.24 + i * TAU / Math.max(1, atom.electronIds.length)
            const shellRadius = atom.shellRadius * (0.84 + 0.06 * atom.protons + 0.025 * atom.neutrons)
            if (!isDeclaredBondElectron(electronIndex)) {
                const target = {
                    x: center.x + Math.cos(shellPhase) * shellRadius,
                    y: center.y + Math.sin(shellPhase) * shellRadius * 0.72,
                    z: center.z - 0.14 + Math.sin(shellPhase + electron.sigma) * 0.14,
                }
                addStructureForce(electronIndex, fx, fy, fz, target, 0.01 + atom.protons * 0.002)
            }

            const dx = wrappedOffset(electron.x - center.x, width)
            const dy = wrappedOffset(electron.y - center.y, height)
            const dz = (electron.z - center.z) * depthScale
            const distance = Math.max(1, Math.hypot(dx, dy, dz))
            const innerLimit = shellRadius * 0.42
            if (distance < innerLimit) {
                const outward = (1 - distance / innerLimit) * (0.08 + settings.capacity * 0.025)
                fx[electronIndex] += dx / distance * outward
                fy[electronIndex] += dy / distance * outward
                fz[electronIndex] += dz / distance * outward / depthScale
                electron.pressure = clamp01(electron.pressure + outward * 0.02)
            }
        }
    }

    for (let i = 0; i < declaredAtoms.length; i++) {
        const left = declaredAtoms[i]
        for (let j = i + 1; j < declaredAtoms.length; j++) {
            const right = declaredAtoms[j]
            const vector = declaredAtomVector(left, right, depthScale)
            const minDistance = declaredAtomCoreRadius(left) + declaredAtomCoreRadius(right)
            if (vector.distance >= minDistance) continue
            const { ux, uy, uz } = declaredAtomUnitDirection(left, right, vector)
            const overlap = clamp01((minDistance - vector.distance) / minDistance)
            const strength = overlap * overlap * (0.42 + settings.capacity * 0.18)
            addGroupForce(left.nucleusIds, fx, fy, fz, -ux, -uy, -uz, strength)
            addGroupForce(right.nucleusIds, fx, fy, fz, ux, uy, uz, strength)
        }
    }

    for (const bond of declaredBonds) {
        const left = declaredAtomById(bond.atomIds[0])
        const right = declaredAtomById(bond.atomIds[1])
        if (!left || !right) continue

        const energy = declaredBondClosureEnergy(bond)
        bond.freeEnergy = energy.free
        bond.boundEnergy = energy.bound
        bond.binding = energy.binding
        bond.stability = energy.stability

        const vector = declaredAtomVector(left, right, depthScale)
        const { ux, uy, uz } = declaredAtomUnitDirection(left, right, vector)
        const idealLength = declaredBondIdealLength(bond)
        const scaffoldPull = isDeclaredCovalentScaffold(bond) ? 0.18 + bond.order * 0.08 : 0
        const liveElectrons = bond.electronIds.filter(index => particles[index])
        const bridgeCenter = liveElectrons.length > 0
            ? compositePosition(liveElectrons)
            : { x: left.x + vector.dx * 0.5, y: left.y + vector.dy * 0.5, z: left.z + vector.dzRaw * 0.5 }
        const repulse = energy.repulsion * (0.16 + settings.capacity * 0.04)
        addGroupForce(left.nucleusIds, fx, fy, fz, -ux, -uy, -uz, repulse)
        addGroupForce(right.nucleusIds, fx, fy, fz, ux, uy, uz, repulse)

        const restError = vector.distance - idealLength
        const restStrength = clamp01(Math.abs(restError) / idealLength) * (0.12 + energy.stability * 0.05 + settings.capacity * 0.03)
        if (restError < 0) {
            addGroupForce(left.nucleusIds, fx, fy, fz, -ux, -uy, -uz, restStrength)
            addGroupForce(right.nucleusIds, fx, fy, fz, ux, uy, uz, restStrength)
        } else if (energy.binding > 0.04 || scaffoldPull > 0) {
            const closurePull = restStrength * clamp01(Math.max(energy.binding, scaffoldPull))
            addGroupForce(left.nucleusIds, fx, fy, fz, ux, uy, uz, closurePull)
            addGroupForce(right.nucleusIds, fx, fy, fz, -ux, -uy, -uz, closurePull)
        }

        const bridgePull = Math.max(0, energy.binding, scaffoldPull * 0.55) * (0.038 + settings.sourceCoupling * 0.012)
        const leftBridgeDx = wrappedOffset(bridgeCenter.x - left.x, width)
        const leftBridgeDy = wrappedOffset(bridgeCenter.y - left.y, height)
        const leftBridgeDz = bridgeCenter.z - left.z
        const rightBridgeDx = wrappedOffset(bridgeCenter.x - right.x, width)
        const rightBridgeDy = wrappedOffset(bridgeCenter.y - right.y, height)
        const rightBridgeDz = bridgeCenter.z - right.z
        addGroupForce(left.nucleusIds, fx, fy, fz, leftBridgeDx, leftBridgeDy, leftBridgeDz, bridgePull / Math.max(18, vector.distance))
        addGroupForce(right.nucleusIds, fx, fy, fz, rightBridgeDx, rightBridgeDy, rightBridgeDz, bridgePull / Math.max(18, vector.distance))

        const bondScale = Math.max(24, (left.shellRadius + right.shellRadius) * 0.9 * settings.carrierSpread)
        for (let i = 0; i < liveElectrons.length; i++) {
            const electronIndex = liveElectrons[i]
            const electron = particles[electronIndex]
            if (!electron) continue

            for (const atom of [left, right]) {
                const dx = wrappedOffset(atom.x - electron.x, width)
                const dy = wrappedOffset(atom.y - electron.y, height)
                const dz = atom.z - electron.z
                const distance = Math.max(1, Math.hypot(dx, dy, dz * depthScale))
                const attraction = atom.protons / (1 + distance / bondScale) ** 2 * (0.018 + energy.stability * 0.018)
                fx[electronIndex] += dx / distance * attraction
                fy[electronIndex] += dy / distance * attraction
                fz[electronIndex] += dz / distance * attraction
            }

            for (let j = 0; j < liveElectrons.length; j++) {
                if (j === i) continue
                const other = particles[liveElectrons[j]]
                if (!other) continue
                const dx = wrappedOffset(electron.x - other.x, width)
                const dy = wrappedOffset(electron.y - other.y, height)
                const dz = electron.z - other.z
                const distance = Math.max(1, Math.hypot(dx, dy, dz * depthScale))
                const pressure = clamp01(1 - distance / Math.max(8, bondScale * 0.34)) * (0.04 + settings.capacity * 0.018)
                fx[electronIndex] += dx / distance * pressure
                fy[electronIndex] += dy / distance * pressure
                fz[electronIndex] += dz / distance * pressure
            }

            const bindingGain = Math.max(0, energy.binding, scaffoldPull * 0.45)
            electron.recurrence = clamp01(electron.recurrence + bindingGain * 0.0024 - Math.max(0, -energy.binding) * 0.0014)
            electron.coherence = clamp01(electron.coherence + bindingGain * 0.0017 - energy.pressure * 0.0012)
            electron.J = clamp01(electron.J - bindingGain * 0.002 + Math.max(0, energy.bound - energy.free) * 0.0016)
        }
    }

    applyDeclaredWaterBendForces(fx, fy, fz, depthScale)
}

function applyInferredAtomClosureForces(fx: Float32Array, fy: Float32Array, fz: Float32Array, depthScale: number) {
    if (declaredAtoms.length > 0 || atomComposites.length === 0) return

    for (const atom of atomComposites) {
        const captureMemory = atom.electronIds.length > 0 ? inferredCaptureStrength(atom.electronIds[0], atom.id) : 0
        if ((atom.stability < 0.18 && captureMemory < 0.12) || atom.nucleusIds.length === 0) continue

        const center = compositePosition(atom.nucleusIds)
        atom.x = center.x
        atom.y = center.y
        atom.z = center.z
        applyBoundAtomReturnFlow(atom)
        const effectiveStability = Math.max(atom.stability, captureMemory * 0.72)
        const nucleusRadius = 3.8 + Math.sqrt(atom.nucleusIds.length) * 1.6
        const nucleusStrength = effectiveStability * (0.012 + settings.compositeBias * 0.006 + settings.sourceCoupling * 0.004)

        for (let i = 0; i < atom.nucleusIds.length; i++) {
            const targetAngle = atom.id * 0.017 + i * TAU / Math.max(3, atom.nucleusIds.length)
            addStructureForce(atom.nucleusIds[i], fx, fy, fz, {
                x: center.x + Math.cos(targetAngle) * nucleusRadius,
                y: center.y + Math.sin(targetAngle) * nucleusRadius,
                z: center.z + Math.sin(targetAngle * 1.7) * 0.035,
            }, nucleusStrength)
        }

        const shellRadius = Math.max(28, atom.radius * (0.72 + settings.carrierSpread * 0.08))
        for (let i = 0; i < atom.electronIds.length; i++) {
            const electronIndex = atom.electronIds[i]
            const electron = particles[electronIndex]
            if (!electron) continue

            const shellPhase = electron.theta + electron.sigma * 0.22 + i * TAU / Math.max(1, atom.electronIds.length)
            const target = {
                x: center.x + Math.cos(shellPhase) * shellRadius,
                y: center.y + Math.sin(shellPhase) * shellRadius * 0.72,
                z: center.z - 0.12 + Math.sin(shellPhase + electron.sigma) * 0.13,
            }
            addStructureForce(electronIndex, fx, fy, fz, target, effectiveStability * (0.012 + settings.lensStrength * 0.003 + captureMemory * 0.01) * (physicsLedgerEnabled.value ? 0.7 : 1))

            const dx = wrappedOffset(electron.x - center.x, width)
            const dy = wrappedOffset(electron.y - center.y, height)
            const dz = (electron.z - center.z) * depthScale
            const distance = Math.max(1, Math.hypot(dx, dy, dz))
            const innerLimit = shellRadius * 0.36
            if (distance < innerLimit) {
                const outward = (1 - distance / innerLimit) * effectiveStability * (0.045 + settings.capacity * 0.018)
                fx[electronIndex] += dx / distance * outward
                fy[electronIndex] += dy / distance * outward
                fz[electronIndex] += dz / distance * outward / depthScale
                electron.pressure = clamp01(electron.pressure + outward * 0.012)
            }
        }
    }
}

function stepSimulation() {
    if (!isRunning.value) return

    const n = particles.length
    pruneInferredElectronCaptures()
    const entanglementState = buildEntanglementState()
    const interactionRadius = Math.max(42, Math.min(viewportWidth, viewportHeight) * 0.085)
    const interactionRadius2 = interactionRadius * interactionRadius
    const shortRadius = 11
    const shortRadius2 = shortRadius * shortRadius
    const depthScale = Math.max(1, projectionDepthScale())
    const dt = 1
    const estimatedPairs = n * Math.max(0, n - 1) / 2
    const pairStride = Math.max(1, Math.ceil(estimatedPairs / MAX_PAIR_INTERACTIONS))
    const occupancyState = buildMttOccupancyState(n)

    const fx = new Float32Array(n)
    const fy = new Float32Array(n)
    const fz = new Float32Array(n)
    const phaseTorque = new Float32Array(n)
    const sigmaTorque = new Float32Array(n)
    const phaseError = new Float32Array(n)
    const localCount = new Uint16Array(n)
    const lensCharge = new Float32Array(n)
    const neutralPairs = new Uint16Array(n)

    let loadSum = 0
    let loadX = 0
    let loadY = 0
    let loadZ = 0
    let pressureSum = 0

    for (let i = 0; i < n; i++) {
        const a = particles[i]
        a.age += 1
        a.neutrality = 0
        const load = Math.max(0.04, a.massLoad)
        loadSum += load
        loadX += a.x * load
        loadY += a.y * load
        loadZ += a.z * load
        pressureSum += a.pressure
    }

    geometry = {
        x: loadSum > 0 ? loadX / loadSum : width * 0.5,
        y: loadSum > 0 ? loadY / loadSum : height * 0.5,
        z: loadSum > 0 ? loadZ / loadSum : 0,
        load: loadSum / Math.max(1, n),
        pressure: pressureSum / Math.max(1, n),
    }

    for (let i = 0; i < n; i++) {
        const a = particles[i]
        for (let j = i + 1; j < n; j++) {
            if (pairStride > 1 && ((i * 31 + j * 17 + frame) % pairStride !== 0)) continue
            const b = particles[j]
            let dx = b.x - a.x
            let dy = b.y - a.y
            const dzRaw = b.z - a.z

            if (dx > width * 0.5) dx -= width
            else if (dx < -width * 0.5) dx += width
            if (dy > height * 0.5) dy -= height
            else if (dy < -height * 0.5) dy += height

            const dz = dzRaw * depthScale
            const d2 = dx * dx + dy * dy + dz * dz
            if (d2 < 0.0001 || d2 > interactionRadius2) continue

            const d = Math.sqrt(d2)
            const inv = 1 / d
            const uX = dx * inv
            const uY = dy * inv
            const uZ = dz * inv
            const closeness = 1 - d / interactionRadius
            const phaseDelta = signedAngle(b.theta - a.theta)
            const sigmaDelta = signedAngle(b.sigma - a.sigma)
            const phaseAlign = Math.cos(phaseDelta) * 0.72 + Math.cos(sigmaDelta) * 0.28
            const lens = lensCompatibility(a, b)
            const nilMatch = a.nil >= 0 && b.nil >= 0 ? (a.nil === b.nil ? 0.28 : -0.38) : 0
            const sameEntangled = a.entanglementId >= 0 && a.entanglementId === b.entanglementId
            const entangledRelation = sameEntangled
                ? Math.cos(signedAngle((b.theta - b.entanglementPhase) - (a.theta - a.entanglementPhase)))
                : 0
            const cancellationBridge = (a.mode === 2 || b.mode === 2) ? 0.26 : 0
            const compositePull = lens > 0 ? settings.compositeBias * 0.28 : 0
            const gaugeConstraintForce = mttGaugeConstraintForce(a, b, phaseDelta, sigmaDelta, closeness)
            const occupancyForce = mttOccupancyPairForce(occupancyState, i, j, a, b, phaseDelta, sigmaDelta, closeness)

            let force = 0
            if (d2 < shortRadius2) {
                force -= 2.2 * (1 - d / shortRadius)
            }
            force += settings.circleStrength * 0.42 * phaseAlign * closeness
            force += settings.lensStrength * 0.34 * lens * closeness
            force += nilMatch * closeness
            force += settings.entanglementStrength * 0.1 * entangledRelation * closeness
            force += gaugeConstraintForce
            force += occupancyForce
            force += cancellationBridge * Math.sin(Math.abs(phaseDelta)) * closeness
            force += compositePull * closeness

            fx[i] += uX * force
            fy[i] += uY * force
            fz[i] += uZ * force / depthScale
            fx[j] -= uX * force
            fy[j] -= uY * force
            fz[j] -= uZ * force / depthScale

            const torque = Math.sin(phaseDelta) * closeness
            const secondaryTorque = Math.sin(sigmaDelta) * closeness
            phaseTorque[i] += torque
            phaseTorque[j] -= torque
            sigmaTorque[i] += secondaryTorque
            sigmaTorque[j] -= secondaryTorque
            if (sameEntangled) {
                const relationTorque = Math.sin(signedAngle((b.theta - b.entanglementPhase) - (a.theta - a.entanglementPhase))) * closeness * settings.entanglementStrength
                phaseTorque[i] += relationTorque * 0.24
                phaseTorque[j] -= relationTorque * 0.24
            }
            const gaugeTorque = mttGaugeConstraintTorque(a, b, phaseDelta, sigmaDelta, closeness)
            phaseTorque[i] += gaugeTorque.phase
            phaseTorque[j] -= gaugeTorque.phase
            sigmaTorque[i] += gaugeTorque.sigma
            sigmaTorque[j] -= gaugeTorque.sigma
            phaseError[i] += (1 - phaseAlign) * closeness
            phaseError[j] += (1 - phaseAlign) * closeness
            localCount[i] += 1
            localCount[j] += 1
            lensCharge[i] += b.lens * closeness
            lensCharge[j] += a.lens * closeness
            if (lens > 0 && d < interactionRadius * 0.42) {
                neutralPairs[i] += 1
                neutralPairs[j] += 1
            }
        }
    }

    if (pointer.active && pointer.dragMode === 'field' && stirField.value) {
        const dragX = pointer.x - pointer.lastX
        const dragY = pointer.y - pointer.lastY
        for (let i = 0; i < n; i++) {
            const p = particles[i]
            const dx = p.x - pointer.x
            const dy = p.y - pointer.y
            const d2 = dx * dx + dy * dy
            const r = 150
            if (d2 < r * r) {
                const k = (1 - Math.sqrt(d2) / r) * 0.24
                fx[i] += dragX * k
                fy[i] += dragY * k
                phaseTorque[i] += signedAngle(Math.atan2(dy, dx) - p.theta) * 0.025
                sigmaTorque[i] += signedAngle(Math.atan2(dy, dx) + Math.PI / 2 - p.sigma) * 0.014
            }
        }
        pointer.lastX = pointer.x
        pointer.lastY = pointer.y
    }

    const physicsLedger = applyPhysicsEnergyLedgerForces(fx, fy, fz, depthScale, pairStride)
    applyDeclaredStructureForces(fx, fy, fz, depthScale)
    applyResidualNuclearForces(fx, fy, fz, depthScale)
    applyMttRadiativeCaptureForces(fx, fy, fz, depthScale)
    applyInferredAtomClosureForces(fx, fy, fz, depthScale)
    applyMttOccupancyClosureForces(occupancyState, fx, fy, fz, depthScale)

    let anchors = 0
    let cancellation = 0
    let nil0 = 0
    let nil1 = 0
    let nil2 = 0
    let meanJ = 0
    let meanCoherence = 0
    let meanPressure = 0
    let meanTimeRate = 0
    let meanDepth = 0
    let composites = 0
    let entangled = 0
    let measured = 0
    let netCharge = 0
    let leftCount = 0
    let fermionCount = 0
    let meanGamma = 0
    let kineticEnergy = 0
    let momentumX = 0
    let momentumY = 0
    let momentumZ = 0
    let capturePhotons = 0

    for (let i = 0; i < n; i++) {
        const p = particles[i]
        const group = p.entanglementId >= 0 ? entanglementState.summaries.get(p.entanglementId) : undefined
        const count = Math.max(1, localCount[i])
        const density = localCount[i] / 16
        const phaseCost = phaseError[i] / count
        const phaseOrder = clamp01(1 - phaseCost)
        const lensCost = Math.min(1, Math.abs(p.lens + lensCharge[i]) / Math.max(1, localCount[i] * 0.42))
        const speed = Math.hypot(p.vx, p.vy)
        let gdx = geometry.x - p.x
        let gdy = geometry.y - p.y
        if (gdx > width * 0.5) gdx -= width
        else if (gdx < -width * 0.5) gdx += width
        if (gdy > height * 0.5) gdy -= height
        else if (gdy < -height * 0.5) gdy += height
        const gdz = (geometry.z - p.z) * depthScale
        const geometryDistance = Math.max(1, Math.hypot(gdx, gdy, gdz))
        const geometryPotential = clamp01(settings.gravityStrength * geometry.load * 1.8 / (1 + geometryDistance / 220))
        const geometryForce = settings.gravityStrength * geometry.load * 0.18 / (1 + geometryDistance / 150)
        fx[i] += gdx / geometryDistance * geometryForce
        fy[i] += gdy / geometryDistance * geometryForce
        fz[i] += gdz / geometryDistance * geometryForce / depthScale

        const depthBurden = Math.abs(p.z) * settings.projectionDepth * settings.upperWorldCoupling
        const capacityPressure = Math.max(0, density - settings.capacity * settings.carrierSpread * (1.18 - Math.min(0.28, depthBurden * 0.12)))
        const occupancyCost = occupancyState.costs[i] ?? 0
        const neutralSupport = Math.min(1, neutralPairs[i] / 3)
        const targetBasin = basinFromCarrier(p.theta, p.sigma)
        const basinCost = p.nil >= 0 ? (p.nil === targetBasin ? 0.05 : 0.42) : 0.24
        const entangledPhaseCost = group
            ? (1 - Math.cos(signedAngle((p.theta - p.entanglementPhase) - group.meanPhase))) * 0.5
            : 0
        const entangledNilSupport = group && p.nil >= 0 && p.nil === group.selectedNil
            ? group.coherence * settings.entanglementStrength
            : 0
        const smSupport = smClosureSupport(p, group)
        const c = isSmPreset() ? 5.2 : 7
        const beta = Math.min(0.96, speed / c)
        p.gamma = 1 / Math.sqrt(1 - beta * beta)

        p.pressure = clamp01(0.46 * capacityPressure + 0.22 * geometryPotential + 0.14 * depthBurden + 0.12 * Math.min(1, speed / 7) + occupancyCost * 0.22)
        p.J = clamp01(0.34 * phaseCost + 0.16 * lensCost + 0.2 * p.pressure + 0.07 * Math.min(1, speed / 9) + basinCost * 0.14 + occupancyCost * 0.18 + entangledPhaseCost * 0.08 * settings.entanglementStrength - neutralSupport * 0.22 - entangledNilSupport * 0.05 - smSupport)
        const closureMargin = clamp01((settings.nilThreshold + 0.18 - p.J) / 0.36)
        p.coherence = clamp01(p.coherence + (phaseOrder - p.coherence) * 0.018 + closureMargin * 0.018 + neutralSupport * 0.012 - capacityPressure * 0.01 - occupancyCost * 0.008)
        p.neutrality = neutralSupport
        if (group) {
            p.branchWeights = blendBranchWeights(p.branchWeights, computeBranchWeights(p, group), 0.018 * settings.entanglementStrength)
        } else {
            p.branchWeights = blendBranchWeights(p.branchWeights, branchWeightsFromCarrier(p.theta, p.sigma, p.nil), 0.012)
        }
        p.massLoad = clamp01(0.1 + p.pressure * 0.42 + Math.min(1, speed / 5) * 0.18 + p.J * 0.16 + (p.mode === 1 ? 0.22 : p.mode === 3 ? 0.16 : 0))
        const baseTimeRate = 1 - settings.timeCurvature * (0.48 * p.pressure + 0.36 * geometryPotential + 0.16 * p.J)
        p.timeRate = Math.max(0.22, baseTimeRate / (isSmPreset() ? Math.sqrt(p.gamma) : 1))
        p.properTime += p.timeRate

        const previousTurn = p.lastTurn
        p.phaseTotal += (settings.phaseDrift * (1 + p.lens * 0.18) + phaseTorque[i] * 0.018) * p.timeRate
        p.sigmaTotal += (settings.phaseDrift * 0.62 * (1 - p.lens * 0.11) + sigmaTorque[i] * 0.013 + p.neutrality * 0.002) * p.timeRate
        p.theta = wrapAngle(p.phaseTotal)
        p.sigma = wrapAngle(p.sigmaTotal)
        const nextTurn = Math.floor(p.phaseTotal / TAU)
        const previousSigmaTurn = p.lastSigmaTurn
        const nextSigmaTurn = Math.floor(p.sigmaTotal / TAU)
        if ((nextTurn !== previousTurn || nextSigmaTurn !== previousSigmaTurn) && p.J < settings.nilThreshold + 0.16) {
            p.recurrence = Math.min(1, p.recurrence + (0.14 + neutralSupport * 0.04) * settings.upperWorldCoupling)
            p.lastTurn = nextTurn
            p.lastSigmaTurn = nextSigmaTurn
        } else {
            p.recurrence = clamp01(p.recurrence + (closureMargin * phaseOrder * 0.002 + neutralSupport * 0.001) * settings.upperWorldCoupling - capacityPressure * 0.0015 - occupancyCost * 0.0012)
        }

        if (p.nil === -1 && p.age > 18 && p.coherence > 0.3 && p.J < settings.nilThreshold + 0.12) {
            p.nil = targetBasin
            emitProjectionEvent(p, 205, 0.52)
        }

        if (p.nil >= 0 && p.coherence > 0.48 && p.J < settings.nilThreshold + 0.04 && p.recurrence > 0.12) {
            if (hasStableCharge(p)) {
                if (p.mode !== 1) emitProjectionEvent(p, 154, 0.9)
                p.mode = 1
            } else if (neutralSupport > 0.68) {
                if (p.mode !== 3) emitProjectionEvent(p, 42, 0.74)
                p.mode = 3
            } else {
                p.mode = 0
            }
        } else if (p.J > settings.nilThreshold + 0.24 || (p.coherence < 0.13 && p.age > 90)) {
            if (p.mode !== 2 && p.nil >= 0) metrics.partitions += 1
            if (p.mode !== 2) emitProjectionEvent(p, 270, 0.68)
            p.mode = 2
            p.nil = -1
            p.coherence = Math.max(p.coherence, 0.2)
        } else if (p.mode === 1 && (!hasStableCharge(p) || p.coherence < 0.54)) {
            p.mode = 0
        }

        const measurementProfile = measurementProfileForParticle(p)
        if (measurementProfile.gain > 0.015) {
            applyLookingGlassMeasurement(p, i, measurementProfile, group, entanglementState.members)
        } else if (p.measurement === 'focused' && frame - p.lastMeasuredFrame > 72) {
            p.measurement = 'unresolved'
        }

        if ((p.mode === 1 || p.mode === 3) && !(isSmPreset() && isChargedLeptonKind(p.smKind))) {
            p.measurement = 'anchored'
        }
        if (isSmPreset()) {
            if (p.smKind === 'photon' || p.smKind === 'gluon') {
                p.mode = 0
                if (p.measurement === 'anchored') p.measurement = 'unresolved'
                p.coherence = Math.max(p.coherence, 0.56)
            } else if (isQuarkKind(p.smKind)) {
                enforceSmProjector(p)
                p.mode = 3
            } else if (isChargedLeptonKind(p.smKind) || p.smKind === 'neutrino' || p.smKind === 'antineutrino') {
                p.mode = 1
                if (isChargedLeptonKind(p.smKind) && p.measurement === 'anchored' && frame - p.lastMeasuredFrame > 96) {
                    p.measurement = 'unresolved'
                }
            }
        }

        const pulsePeriod = Math.max(42, Math.floor(118 - p.coherence * 54))
        if ((p.mode === 1 || p.mode === 3) && p.age % pulsePeriod === 0) {
            emitProjectionEvent(p, p.mode === 1 ? 154 : 42, 0.28 + p.coherence * 0.22)
        }

        const damping = isSmPreset() && (p.smKind === 'photon' || p.smKind === 'gluon')
            ? 0.986
            : p.mode === 1 ? 0.91 : p.mode === 2 ? 0.965 : 0.94
        const inertial = inertialMass(p)
        p.vx = (p.vx + fx[i] * dt / inertial) * damping
        p.vy = (p.vy + fy[i] * dt / inertial) * damping
        p.vz = (p.vz + (fz[i] * dt - p.z * 0.002 * settings.projectionDepth * settings.upperWorldCoupling) / inertial) * (0.96 - p.pressure * 0.04)
        const maxSpeed = isSmPreset()
            ? (p.smKind === 'photon' || p.smKind === 'gluon' ? 5.15 : 4.45)
            : p.mode === 2 ? 5.6 : 4.3
        const newSpeed = Math.hypot(p.vx, p.vy)
        if (newSpeed > maxSpeed) {
            p.vx = p.vx / newSpeed * maxSpeed
            p.vy = p.vy / newSpeed * maxSpeed
        }

        p.x += p.vx
        p.y += p.vy
        p.z += p.vz
        if (p.z > 1.4) {
            p.z = 1.4
            p.vz *= -0.45
        } else if (p.z < -1.4) {
            p.z = -1.4
            p.vz *= -0.45
        }
        if (p.x < 0) p.x += width
        else if (p.x >= width) p.x -= width
        if (p.y < 0) p.y += height
        else if (p.y >= height) p.y -= height

        if (p.mode === 1) anchors += 1
        if (p.mode === 2) cancellation += 1
        if (p.nil === 0) nil0 += 1
        else if (p.nil === 1) nil1 += 1
        else if (p.nil === 2) nil2 += 1
        if (p.mode === 3 || neutralSupport > 0.75) composites += 1
        if (p.entanglementId >= 0) entangled += 1
        if (frame - p.lastMeasuredFrame < 90) measured += 1
        netCharge += p.electricCharge
        if (isFermionKind(p.smKind)) {
            fermionCount += 1
            if (p.chirality === 'L') leftCount += 1
        }
        if (p.smKind === 'photon' && p.entanglementId === CAPTURE_PHOTON_ENTANGLEMENT_ID) capturePhotons += 1
        kineticEnergy += particleKineticEnergy(p, depthScale, inertial)
        momentumX += inertial * p.vx
        momentumY += inertial * p.vy
        momentumZ += inertial * p.vz * depthScale
        meanGamma += p.gamma
        meanJ += p.J
        meanCoherence += p.coherence
        meanPressure += p.pressure
        meanTimeRate += p.timeRate
        meanDepth += Math.abs(p.z)
    }

    metrics.anchors = anchors
    metrics.cancellation = cancellation
    metrics.nil0 = nil0
    metrics.nil1 = nil1
    metrics.nil2 = nil2
    metrics.meanJ = meanJ / Math.max(1, n)
    metrics.meanCoherence = meanCoherence / Math.max(1, n)
    metrics.meanPressure = meanPressure / Math.max(1, n)
    metrics.meanTimeRate = meanTimeRate / Math.max(1, n)
    metrics.meanDepth = meanDepth / Math.max(1, n)
    metrics.composites = composites
    metrics.entangled = entangled
    metrics.measured = measured
    metrics.netCharge = netCharge
    metrics.kineticEnergy = kineticEnergy
    metrics.netMomentum = Math.hypot(momentumX, momentumY, momentumZ)
    energyPulseResidue *= 0.985
    captureBoundResidue *= 0.992
    captureRadiatedResidue *= 0.988
    metrics.energyInput = energyPulseResidue
    metrics.captureBoundEnergy = captureBoundResidue
    metrics.captureRadiatedEnergy = captureRadiatedResidue
    metrics.capturePhotons = capturePhotons
    updatePhysicsLedgerMetrics(physicsLedger)
    metrics.mttOccupancyCells = occupancyState.activeCells
    metrics.mttOccupancyCost = occupancyState.meanCost
    const colorStats = computeColorClosureStats()
    metrics.colorClosure = colorStats.closure
    metrics.leftShare = fermionCount > 0 ? leftCount / fermionCount : 0
    metrics.meanGamma = meanGamma / Math.max(1, n)
    computeSmInvariants()
    buildAtomComposites()
    applyMttClosureGradient()
    collectOrbitalSamples()
    updateProjectionEvents()
}

function colorForParticle(p: ProtoParticle, alpha = 1) {
    if (viewMode.value === 'nil') {
        if (p.nil === 0) return `rgba(72, 213, 151, ${alpha})`
        if (p.nil === 1) return `rgba(255, 195, 92, ${alpha})`
        if (p.nil === 2) return `rgba(111, 169, 255, ${alpha})`
        return `rgba(142, 148, 162, ${alpha})`
    }
    if (viewMode.value === 'phase') {
        const hue = Math.floor(wrapAngle(p.theta + p.sigma * 0.5) / TAU * 360)
        return `hsla(${hue}, 86%, 64%, ${alpha})`
    }
    if (viewMode.value === 'cost') {
        const hue = Math.floor((1 - p.J) * 145)
        return `hsla(${hue}, 86%, 58%, ${alpha})`
    }
    if (viewMode.value === 'pressure') {
        const hue = Math.floor((1 - p.pressure) * 210)
        return `hsla(${hue}, 90%, 62%, ${alpha})`
    }
    if (isSmPreset() && p.smKind !== 'generic') return smColor(p.smKind, alpha)
    if (p.mode === 1) return `rgba(111, 245, 190, ${alpha})`
    if (p.mode === 2) return `rgba(184, 138, 255, ${alpha})`
    if (p.mode === 3) return `rgba(255, 210, 115, ${alpha})`
    return `rgba(150, 177, 205, ${alpha})`
}

function emitProjectionEvent(p: ProtoParticle, hue: number, strength: number) {
    const projected = projectParticle(p)
    projectionEvents.push({
        x: projected.x,
        y: projected.y,
        radius: 4 + strength * 6,
        maxRadius: 34 + strength * 64,
        life: 1,
        maxLife: 52 + Math.floor(strength * 42),
        hue,
        width: 0.8 + strength * 1.8,
    })
    if (projectionEvents.length > 240) projectionEvents.splice(0, projectionEvents.length - 240)
}

function updateProjectionEvents() {
    for (const event of projectionEvents) {
        const t = event.life / event.maxLife
        event.radius += (event.maxRadius - event.radius) * 0.045 + 0.18
        event.life += 1 + t * 0.25
    }
    projectionEvents = projectionEvents.filter(event => event.life < event.maxLife)
}

function draw() {
    if (!ctx) return
    frame += 1

    ctx.fillStyle = 'rgba(3, 6, 13, 0.34)'
    ctx.fillRect(0, 0, viewportWidth, viewportHeight)

    ctx.save()
    applyCameraTransform()
    if (showGeometryField.value) drawGeometryField()

    if (layerView.value === 'spinor') {
        if (showEntanglement.value) drawEntanglementLinks()
        drawSpinorCarrierView()
        if (showProjectionEvents.value) drawProjectionEvents()
        if (showLookingGlassOverlay.value) drawLookingGlass()
        ctx.restore()
        return
    }

    if (layerView.value === 'atom') {
        drawAtomView()
        if (showProjectionEvents.value) drawProjectionEvents()
        if (showLookingGlassOverlay.value) drawLookingGlass()
        ctx.restore()
        return
    }

    if (layerView.value === 'orbital') {
        drawOrbitalView()
        if (showProjectionEvents.value) drawProjectionEvents()
        if (showLookingGlassOverlay.value) drawLookingGlass()
        ctx.restore()
        return
    }

    if (showWaves.value) drawUnresolvedWaves()
    if (showEntanglement.value) drawEntanglementLinks()
    if (showLinks.value) drawCompositeLinks()
    drawParticleViewAtomOverlays()
    if (showProjectionEvents.value) drawProjectionEvents()

    for (const p of particles) {
        if (p.mode !== 1 && p.mode !== 3) continue
        if (isUnmeasuredChargedCloud(p)) continue
        const projected = projectParticle(p)
        const sizeBase = p.mode === 1 ? 3.8 + p.coherence * 3.2 : 4.5
        const size = sizeBase * projected.scale
        const glow = size * (3.5 + p.coherence * 3)
        const gradient = ctx.createRadialGradient(projected.x, projected.y, 0, projected.x, projected.y, glow)
        gradient.addColorStop(0, colorForParticle(p, 0.42))
        gradient.addColorStop(1, colorForParticle(p, 0))
        ctx.fillStyle = gradient
        ctx.beginPath()
        ctx.arc(projected.x, projected.y, glow, 0, TAU)
        ctx.fill()

        ctx.fillStyle = colorForParticle(p, 0.92)
        ctx.beginPath()
        ctx.arc(projected.x, projected.y, size, 0, TAU)
        ctx.fill()

        if (isSmPreset() && showSmMarkers.value) drawSmMarker(p, projected.x, projected.y, size)

        if (p.mode === 1) {
            ctx.strokeStyle = colorForParticle(p, 0.8)
            ctx.lineWidth = 1
            ctx.beginPath()
            ctx.arc(projected.x, projected.y, size + 3.5, p.theta + p.properTime * 0.01, p.theta + p.properTime * 0.01 + Math.PI * 1.35)
            ctx.stroke()
        }
    }

    if (showLookingGlassOverlay.value) drawLookingGlass()
    ctx.restore()
}

function drawProjectionEvents() {
    if (!ctx) return
    for (const event of projectionEvents) {
        const t = event.life / event.maxLife
        const alpha = Math.max(0, 1 - t)
        ctx.strokeStyle = `hsla(${event.hue}, 90%, 68%, ${alpha * 0.42})`
        ctx.lineWidth = event.width * (1 - t * 0.35)
        ctx.beginPath()
        ctx.arc(event.x, event.y, event.radius, 0, TAU)
        ctx.stroke()
    }
}

function branchHue(branch: 0 | 1 | 2) {
    if (branch === 0) return 154
    if (branch === 1) return 42
    return 212
}

function drawSmMarker(p: ProtoParticle, x: number, y: number, size: number) {
    if (!ctx || p.smKind === 'generic') return
    ctx.save()
    ctx.strokeStyle = smColor(p.smKind, 0.92)
    ctx.lineWidth = 1.2

    if (p.smKind === 'electron' || p.smKind === 'muon') {
        ctx.beginPath()
        ctx.moveTo(x - size * 0.72, y)
        ctx.lineTo(x + size * 0.72, y)
        ctx.stroke()
        if (p.smKind === 'muon') {
            ctx.beginPath()
            ctx.arc(x, y, size + 3.4, Math.PI * 0.12, Math.PI * 1.88)
            ctx.stroke()
        }
    } else if (p.smKind === 'positron' || p.smKind === 'antimuon') {
        ctx.beginPath()
        ctx.moveTo(x - size * 0.68, y)
        ctx.lineTo(x + size * 0.68, y)
        ctx.moveTo(x, y - size * 0.68)
        ctx.lineTo(x, y + size * 0.68)
        ctx.stroke()
        if (p.smKind === 'antimuon') {
            ctx.beginPath()
            ctx.arc(x, y, size + 3.4, Math.PI * 0.12, Math.PI * 1.88)
            ctx.stroke()
        }
    } else if (p.smKind === 'neutrino' || p.smKind === 'antineutrino') {
        ctx.setLineDash([2, 3])
        ctx.beginPath()
        ctx.arc(x, y, size + 3.6, 0, TAU)
        ctx.stroke()
        if (p.smKind === 'antineutrino') {
            ctx.setLineDash([])
            ctx.beginPath()
            ctx.moveTo(x - size * 0.5, y - size * 0.5)
            ctx.lineTo(x + size * 0.5, y + size * 0.5)
            ctx.stroke()
        }
    } else if (p.smKind === 'quarkR' || p.smKind === 'quarkG' || p.smKind === 'quarkB') {
        ctx.beginPath()
        for (let i = 0; i < 3; i++) {
            const a = p.theta + i * TAU / 3
            const px = x + Math.cos(a) * (size + 2.6)
            const py = y + Math.sin(a) * (size + 2.6)
            if (i === 0) ctx.moveTo(px, py)
            else ctx.lineTo(px, py)
        }
        ctx.closePath()
        ctx.stroke()
    }

    if (isFermionKind(p.smKind)) {
        ctx.fillStyle = p.chirality === 'L' ? 'rgba(255, 255, 255, 0.85)' : 'rgba(255, 255, 255, 0.38)'
        ctx.beginPath()
        ctx.arc(x - size * 1.15, y - size * 1.15, p.chirality === 'L' ? 1.8 : 1.2, 0, TAU)
        ctx.fill()

        if (isQuarkKind(p.smKind)) {
            ctx.fillStyle = p.electricCharge > 0 ? 'rgba(255, 244, 188, 0.72)' : 'rgba(205, 225, 255, 0.72)'
            ctx.beginPath()
            ctx.arc(x + size * 1.18, y - size * 1.12, p.electricCharge > 0 ? 1.9 : 1.35, 0, TAU)
            ctx.fill()
        }
    }

    ctx.restore()
}

function drawSpinorCarrierView() {
    if (!ctx) return
    const stride = Math.max(1, Math.ceil(particles.length / 620))

    for (let i = 0; i < particles.length; i += stride) {
        const p = particles[i]
        const projected = projectParticle(p)
        const branch = p.nil >= 0 ? (p.nil as 0 | 1 | 2) : dominantBranch(p.branchWeights)
        const baseRadius = (3.8 + p.coherence * 7.2) * projected.scale
        const carrierAlpha = 0.12 + p.coherence * 0.28
        const thetaX = projected.x + Math.cos(p.theta) * baseRadius
        const thetaY = projected.y + Math.sin(p.theta) * baseRadius
        const sigmaX = projected.x + Math.cos(p.sigma) * (baseRadius + 3.4)
        const sigmaY = projected.y + Math.sin(p.sigma) * (baseRadius + 3.4)

        ctx.strokeStyle = `hsla(${branchHue(branch)}, 86%, 66%, ${0.12 + p.branchWeights[branch] * 0.34})`
        ctx.lineWidth = p.measurement === 'focused' ? 1.2 : 0.7
        ctx.beginPath()
        ctx.arc(projected.x, projected.y, baseRadius + p.branchWeights[branch] * 5.5, 0, TAU)
        ctx.stroke()

        ctx.strokeStyle = `rgba(111, 245, 190, ${carrierAlpha})`
        ctx.beginPath()
        ctx.moveTo(projected.x, projected.y)
        ctx.lineTo(thetaX, thetaY)
        ctx.stroke()

        ctx.strokeStyle = `rgba(184, 138, 255, ${carrierAlpha * 0.84})`
        ctx.beginPath()
        ctx.moveTo(projected.x, projected.y)
        ctx.lineTo(sigmaX, sigmaY)
        ctx.stroke()

        ctx.fillStyle = colorForParticle(p, 0.18 + p.coherence * 0.28)
        ctx.beginPath()
        ctx.arc(projected.x, projected.y, Math.max(1.6, p.radius * projected.scale), 0, TAU)
        ctx.fill()
    }
}

function atomLabel(atom: AtomComposite) {
    const declared = declaredAtomById(atom.id)
    if (declared) {
        if (atom.charge > 0) return `${declared.label}+`
        if (atom.charge < 0) return `${declared.label}-`
        return declared.label
    }
    if (atom.protons === 2 && atom.neutrons === 2 && atom.electrons === 2) return 'He'
    if (atom.protons === 1 && atom.neutrons === 2 && atom.electrons === 1) return 'T'
    if (atom.protons === 1 && atom.neutrons === 1 && atom.electrons === 1) return 'D'
    if (atom.protons === 1 && atom.electrons === 1) return 'H'
    if (atom.protons === 1 && atom.electrons === 0) return 'H+'
    return 'A'
}

function drawAtomFreeField() {
    if (!ctx) return
    const stride = Math.max(1, Math.ceil(particles.length / 260))
    for (let i = 0; i < particles.length; i += stride) {
        const p = particles[i]
        if (p.mode === 2) continue
        const projected = projectParticle(p)
        const alpha = isQuarkKind(p.smKind) || p.smKind === 'electron' ? 0.12 : 0.055
        ctx.fillStyle = colorForParticle(p, alpha)
        ctx.beginPath()
        ctx.arc(projected.x, projected.y, Math.max(1.2, p.radius * 0.7 * projected.scale), 0, TAU)
        ctx.fill()
    }
}

function drawAtomNucleus(atom: AtomComposite, x: number, y: number) {
    if (!ctx) return
    const nucleons = atom.protons + atom.neutrons
    const spread = 7 + atom.neutrons * 1.8
    for (let i = 0; i < nucleons; i++) {
        const angle = frame * 0.006 + atom.id * 0.73 + i * TAU / Math.max(1, nucleons)
        const px = x + Math.cos(angle) * spread * (i % 2 === 0 ? 0.62 : 0.34)
        const py = y + Math.sin(angle) * spread * (i % 2 === 0 ? 0.62 : 0.34)
        const proton = i < atom.protons
        ctx.fillStyle = proton ? 'rgba(251, 113, 133, 0.94)' : 'rgba(203, 213, 225, 0.86)'
        ctx.beginPath()
        ctx.arc(px, py, proton ? 4.6 : 4.2, 0, TAU)
        ctx.fill()
    }
}

function drawParticleViewAtomOverlays() {
    if (!ctx || !isSmPreset() || atomComposites.length === 0) return

    for (const atom of atomComposites) {
        if (atom.stability < 0.22 || atom.protons < 1) continue

        const projected = projectPoint(atom.x, atom.y, atom.z)
        const radius = Math.max(20, Math.min(68, atom.radius * 0.72)) * projected.scale
        if (showAtomHalos.value) {
            const gradient = ctx.createRadialGradient(projected.x, projected.y, 0, projected.x, projected.y, radius * 1.25)
            gradient.addColorStop(0, atom.charge === 0 ? `rgba(103, 232, 249, ${0.045 + atom.stability * 0.09})` : `rgba(253, 230, 138, ${0.04 + atom.stability * 0.08})`)
            gradient.addColorStop(1, 'rgba(103, 232, 249, 0)')
            ctx.fillStyle = gradient
            ctx.beginPath()
            ctx.arc(projected.x, projected.y, radius * 1.25, 0, TAU)
            ctx.fill()
        }

        ctx.strokeStyle = atom.charge === 0
            ? `rgba(103, 232, 249, ${0.22 + atom.stability * 0.24})`
            : `rgba(253, 230, 138, ${0.2 + atom.stability * 0.2})`
        ctx.lineWidth = 1
        ctx.setLineDash([5, 7])
        ctx.beginPath()
        ctx.ellipse(projected.x, projected.y, radius, radius * 0.62, atom.id * 0.37, 0, TAU)
        ctx.stroke()
        ctx.setLineDash([])

        if (showAtomLabels.value) {
            ctx.fillStyle = atom.charge === 0 ? 'rgba(232, 255, 250, 0.9)' : 'rgba(255, 242, 190, 0.9)'
            ctx.font = '700 11px ui-monospace, SFMono-Regular, Consolas, monospace'
            ctx.textAlign = 'center'
            ctx.textBaseline = 'middle'
            ctx.fillText(atomLabel(atom), projected.x, projected.y - radius * 0.86)
        }
    }
}

function drawAtomShell(atom: AtomComposite, x: number, y: number, radius: number) {
    if (!ctx || !showAtomShells.value) return
    const shellAlpha = 0.14 + atom.stability * 0.28
    const orbital = atom.id * 0.37

    ctx.save()
    ctx.translate(x, y)
    ctx.rotate(orbital)
    ctx.scale(1, 0.62)
    const cloudGradient = ctx.createRadialGradient(0, 0, radius * 0.18, 0, 0, radius * 1.08)
    cloudGradient.addColorStop(0, `rgba(103, 232, 249, ${0.035 + atom.stability * 0.035})`)
    cloudGradient.addColorStop(0.72, `rgba(103, 232, 249, ${0.025 + atom.stability * 0.045})`)
    cloudGradient.addColorStop(1, 'rgba(103, 232, 249, 0)')
    ctx.fillStyle = cloudGradient
    ctx.beginPath()
    ctx.arc(0, 0, radius * 1.08, 0, TAU)
    ctx.fill()
    ctx.restore()

    ctx.strokeStyle = atom.charge === 0
        ? `rgba(103, 232, 249, ${shellAlpha})`
        : `rgba(253, 230, 138, ${shellAlpha})`
    ctx.lineWidth = 1.1
    ctx.beginPath()
    ctx.ellipse(x, y, radius, radius * 0.62, orbital, 0, TAU)
    ctx.stroke()

    for (let i = 0; i < atom.electrons; i++) {
        const electron = particles[atom.electronIds[i]]
        const measured = electron ? isRecentlyMeasuredChargedLepton(electron) : false
        const samples = measured ? 1 : 7
        for (let sample = 0; sample < samples; sample++) {
            const phase = frame * (measured ? 0.024 : 0.007)
                + atom.id * 0.61
                + i * TAU / Math.max(1, atom.electrons)
                + sample * TAU / samples
                + (electron ? electron.theta * 0.12 + electron.sigma * 0.08 : 0)
            const jitter = measured ? 1 : 0.72 + 0.2 * Math.sin(phase * 2.7 + atom.id)
            const ex = x + Math.cos(phase) * radius * jitter * Math.cos(orbital) - Math.sin(phase) * radius * 0.62 * jitter * Math.sin(orbital)
            const ey = y + Math.cos(phase) * radius * jitter * Math.sin(orbital) + Math.sin(phase) * radius * 0.62 * jitter * Math.cos(orbital)
            ctx.fillStyle = measured ? 'rgba(103, 232, 249, 0.96)' : 'rgba(103, 232, 249, 0.18)'
            ctx.beginPath()
            ctx.arc(ex, ey, measured ? 3.4 : 1.7, 0, TAU)
            ctx.fill()
        }
    }
}

function drawDeclaredBonds() {
    if (!ctx || !showMolecularBonds.value || declaredBonds.length === 0) return

    ctx.save()
    ctx.globalCompositeOperation = 'lighter'
    for (const bond of declaredBonds) {
        const left = declaredAtomById(bond.atomIds[0])
        const right = declaredAtomById(bond.atomIds[1])
        if (!left || !right || !isDeclaredBondActive(bond)) continue

        const leftPoint = projectPoint(left.x, left.y, left.z)
        const rightPoint = projectPoint(right.x, right.y, right.z)
        const midX = (leftPoint.x + rightPoint.x) * 0.5
        const midY = (leftPoint.y + rightPoint.y) * 0.5
        const alpha = 0.16 + bond.stability * 0.36
        const gradient = ctx.createLinearGradient(leftPoint.x, leftPoint.y, rightPoint.x, rightPoint.y)
        gradient.addColorStop(0, `rgba(103, 232, 249, ${alpha * 0.38})`)
        gradient.addColorStop(0.5, `rgba(253, 230, 138, ${alpha})`)
        gradient.addColorStop(1, `rgba(103, 232, 249, ${alpha * 0.38})`)

        ctx.strokeStyle = gradient
        ctx.lineWidth = 2.2 + bond.order * 0.9
        ctx.beginPath()
        ctx.moveTo(leftPoint.x, leftPoint.y)
        ctx.lineTo(rightPoint.x, rightPoint.y)
        ctx.stroke()

        const pulse = 1 + Math.sin(frame * 0.036 + bond.id) * 0.18
        ctx.fillStyle = `rgba(253, 230, 138, ${0.12 + bond.stability * 0.18})`
        ctx.beginPath()
        ctx.arc(midX, midY, (16 + bond.stability * 16) * pulse, 0, TAU)
        ctx.fill()

        ctx.fillStyle = 'rgba(255, 250, 218, 0.84)'
        ctx.font = '800 10px ui-monospace, SFMono-Regular, Consolas, monospace'
        ctx.textAlign = 'center'
        ctx.textBaseline = 'middle'
        ctx.fillText(bond.label, midX, midY - 18)
    }
    ctx.restore()
}

function drawAtomView() {
    if (!ctx) return
    if (showAtomCarrierField.value) drawAtomFreeField()

    const atoms = [...atomComposites]
        .filter(atom => atom.stability > 0.18)
        .sort((a, b) => a.stability - b.stability)

    const clusters = new Map<number, AtomComposite[]>()
    for (const atom of atoms) {
        if (atom.clusterId < 0) continue
        const members = clusters.get(atom.clusterId) ?? []
        members.push(atom)
        clusters.set(atom.clusterId, members)
    }

    if (showAtomHalos.value) {
        for (const members of clusters.values()) {
            if (members.length < 2) continue
            const cx = members.reduce((sum, atom) => sum + atom.x, 0) / members.length
            const cy = members.reduce((sum, atom) => sum + atom.y, 0) / members.length
            const cz = members.reduce((sum, atom) => sum + atom.z, 0) / members.length
            const projected = projectPoint(cx, cy, cz)
            const clusterRadius = Math.max(44, Math.sqrt(members.length) * atomClusterRadius() * 0.42)
            const gradient = ctx.createRadialGradient(projected.x, projected.y, 0, projected.x, projected.y, clusterRadius)
            gradient.addColorStop(0, `rgba(255, 242, 190, ${0.035 + settings.gravityStrength * 0.05})`)
            gradient.addColorStop(1, 'rgba(255, 242, 190, 0)')
            ctx.fillStyle = gradient
            ctx.beginPath()
            ctx.arc(projected.x, projected.y, clusterRadius, 0, TAU)
            ctx.fill()
        }
    }

    drawDeclaredBonds()

    for (const atom of atoms) {
        const projected = projectPoint(atom.x, atom.y, atom.z)
        const radius = atom.radius * projected.scale
        if (showAtomHalos.value) {
            const haloRadius = radius * (1.12 + atom.stability * 0.22)
            const gradient = ctx.createRadialGradient(projected.x, projected.y, 0, projected.x, projected.y, haloRadius)
            gradient.addColorStop(0, atom.charge === 0 ? `rgba(103, 232, 249, ${0.045 + atom.stability * 0.09})` : `rgba(253, 230, 138, ${0.045 + atom.stability * 0.08})`)
            gradient.addColorStop(1, 'rgba(103, 232, 249, 0)')
            ctx.fillStyle = gradient
            ctx.beginPath()
            ctx.arc(projected.x, projected.y, haloRadius, 0, TAU)
            ctx.fill()
        }

        drawAtomShell(atom, projected.x, projected.y, radius)
        if (showAtomNuclei.value) drawAtomNucleus(atom, projected.x, projected.y)

        if (showAtomLabels.value) {
            ctx.fillStyle = atom.charge === 0 ? 'rgba(232, 255, 250, 0.88)' : 'rgba(255, 242, 190, 0.84)'
            ctx.font = '700 11px ui-monospace, SFMono-Regular, Consolas, monospace'
            ctx.textAlign = 'center'
            ctx.textBaseline = 'middle'
            ctx.fillText(atomLabel(atom), projected.x, projected.y + radius * 0.92)
        }
    }
}

function drawReferenceOverlay(atom: AtomComposite, x: number, y: number, radius: number) {
    if (!ctx || !showOrbitalReference.value) return
    const kind = orbitalKindForAtom(atom)
    if (kind === 'none') return

    const electron = particles[atom.electronIds[0]]
    const orientation = electron ? electron.theta + electron.sigma * 0.5 : atom.id * 0.43
    ctx.save()
    ctx.globalCompositeOperation = 'lighter'

    if (kind === '1s') {
        const outer = radius * 1.34
        const gradient = ctx.createRadialGradient(x, y, radius * 0.08, x, y, outer)
        gradient.addColorStop(0, 'rgba(253, 230, 138, 0.11)')
        gradient.addColorStop(0.48, 'rgba(103, 232, 249, 0.055)')
        gradient.addColorStop(1, 'rgba(103, 232, 249, 0)')
        ctx.fillStyle = gradient
        ctx.beginPath()
        ctx.arc(x, y, outer, 0, TAU)
        ctx.fill()
    } else if (kind === '2s') {
        const inner = radius * 0.62
        const outer = radius * 1.55
        const gradient = ctx.createRadialGradient(x, y, inner * 0.2, x, y, outer)
        gradient.addColorStop(0, 'rgba(253, 230, 138, 0.075)')
        gradient.addColorStop(0.42, 'rgba(253, 230, 138, 0.012)')
        gradient.addColorStop(0.55, 'rgba(103, 232, 249, 0.05)')
        gradient.addColorStop(1, 'rgba(103, 232, 249, 0)')
        ctx.fillStyle = gradient
        ctx.beginPath()
        ctx.arc(x, y, outer, 0, TAU)
        ctx.fill()
        ctx.strokeStyle = 'rgba(253, 230, 138, 0.18)'
        ctx.lineWidth = 0.8
        ctx.beginPath()
        ctx.arc(x, y, inner, 0, TAU)
        ctx.stroke()
    } else {
        ctx.translate(x, y)
        ctx.rotate(orientation)
        ctx.scale(1, 0.58)
        for (const side of [-1, 1]) {
            const lobeX = side * radius * 0.58
            const lobeRadius = radius * 0.82
            const gradient = ctx.createRadialGradient(lobeX, 0, 0, lobeX, 0, lobeRadius)
            gradient.addColorStop(0, side < 0 ? 'rgba(103, 232, 249, 0.095)' : 'rgba(184, 138, 255, 0.095)')
            gradient.addColorStop(1, 'rgba(103, 232, 249, 0)')
            ctx.fillStyle = gradient
            ctx.beginPath()
            ctx.arc(lobeX, 0, lobeRadius, 0, TAU)
            ctx.fill()
        }
        ctx.strokeStyle = 'rgba(253, 230, 138, 0.16)'
        ctx.lineWidth = 0.8
        ctx.beginPath()
        ctx.moveTo(-radius * 1.24, 0)
        ctx.lineTo(radius * 1.24, 0)
        ctx.stroke()
    }

    ctx.restore()
}

function drawOrbitalSamples(atomById: Map<number, AtomComposite>) {
    if (!ctx || orbitalSamples.length === 0) return
    const stride = Math.max(1, Math.ceil(orbitalSamples.length / 2200))
    const currentMode = orbitalSampleMode.value

    ctx.save()
    ctx.globalCompositeOperation = 'lighter'
    for (let i = 0; i < orbitalSamples.length; i += stride) {
        const sample = orbitalSamples[i]
        if (sample.mode !== currentMode) continue
        const atom = atomById.get(sample.atomId)
        if (!atom) continue
        const projected = projectPoint(atom.x + sample.dx, atom.y + sample.dy, atom.z + sample.dz)
        const sampleLife = sample.mode === 'raw' ? RAW_ORBITAL_SAMPLE_LIFE : ORBITAL_SAMPLE_LIFE
        const fade = Math.max(0, 1 - sample.age / sampleLife)
        const alpha = sample.weight * fade * (currentMode === 'raw' ? 0.082 : sample.kind === '2p' ? 0.072 : 0.058)
        if (alpha <= 0.002) continue
        const size = (2.1 + sample.weight * 5.8) * projected.scale
        ctx.fillStyle = `hsla(${branchHue(sample.branch)}, 94%, 68%, ${alpha})`
        ctx.beginPath()
        ctx.arc(projected.x, projected.y, size, 0, TAU)
        ctx.fill()
    }
    ctx.restore()
}

function drawOrbitalView() {
    if (!ctx) return
    if (showAtomCarrierField.value) drawAtomFreeField()
    drawDeclaredBonds()

    const atoms = [...atomComposites]
        .filter(atom => atom.stability > 0.18 && atom.electrons > 0)
        .sort((a, b) => a.stability - b.stability)
    const atomById = new Map(atoms.map(atom => [atom.id, atom]))

    for (const atom of atoms) {
        const projected = projectPoint(atom.x, atom.y, atom.z)
        drawReferenceOverlay(atom, projected.x, projected.y, atom.radius * projected.scale)
    }

    drawOrbitalSamples(atomById)

    for (const atom of atoms) {
        const projected = projectPoint(atom.x, atom.y, atom.z)
        const radius = atom.radius * projected.scale
        if (showAtomNuclei.value) drawAtomNucleus(atom, projected.x, projected.y)

        const kind = orbitalKindForAtom(atom)
        ctx.strokeStyle = 'rgba(103, 232, 249, 0.18)'
        ctx.lineWidth = 0.85
        ctx.beginPath()
        ctx.arc(projected.x, projected.y, radius * 1.12, 0, TAU)
        ctx.stroke()

        if (showAtomLabels.value) {
            ctx.fillStyle = 'rgba(232, 255, 250, 0.9)'
            ctx.font = '700 11px ui-monospace, SFMono-Regular, Consolas, monospace'
            ctx.textAlign = 'center'
            ctx.textBaseline = 'middle'
            ctx.fillText(`${atomLabel(atom)} ${orbitalKindLabel(kind)}`, projected.x, projected.y + radius * 1.06)
        }
    }
}

function drawUnresolvedWaves() {
    if (!ctx) return
    const stride = Math.max(1, Math.ceil(particles.length / 260))
    for (let i = 0; i < particles.length; i += stride) {
        const p = particles[i]
        const chargedCloud = isUnmeasuredChargedCloud(p)
        if (p.mode !== 0 && p.measurement !== 'focused' && !chargedCloud) continue

        const projected = projectParticle(p)
        const branch = dominantBranch(p.branchWeights)
        const phase = p.theta + p.sigma * 0.5 + frame * 0.026
        const focusBoost = p.measurement === 'focused' ? 0.14 : 0
        const smWaveBoost = isSmPreset() && (p.smKind === 'photon' || p.smKind === 'gluon') ? 0.08 : chargedCloud ? 0.1 : 0
        const cloudRadius = chargedCloud ? 18 + p.coherence * 34 + settings.carrierSpread * 10 : 8 + p.coherence * 22
        const radius = (cloudRadius + Math.sin(phase) * (chargedCloud ? 4.2 : 2.4)) * projected.scale
        const alpha = 0.026 + p.coherence * 0.042 + focusBoost + smWaveBoost
        const hue = isSmPreset() && p.smKind !== 'generic' ? smHue(p.smKind) : branchHue(branch)

        if (chargedCloud) {
            const gradient = ctx.createRadialGradient(projected.x, projected.y, 0, projected.x, projected.y, Math.max(5, radius))
            gradient.addColorStop(0, `hsla(${hue}, 86%, 68%, ${alpha * 0.42})`)
            gradient.addColorStop(0.62, `hsla(${hue}, 86%, 68%, ${alpha * 0.18})`)
            gradient.addColorStop(1, `hsla(${hue}, 86%, 68%, 0)`)
            ctx.fillStyle = gradient
            ctx.beginPath()
            ctx.arc(projected.x, projected.y, Math.max(5, radius), 0, TAU)
            ctx.fill()
        }

        ctx.strokeStyle = `hsla(${hue}, 86%, 68%, ${alpha})`
        ctx.lineWidth = p.measurement === 'focused' || smWaveBoost > 0 ? 1.15 : 0.7
        ctx.beginPath()
        ctx.arc(projected.x, projected.y, Math.max(3, radius), 0, TAU)
        ctx.stroke()

        if (p.measurement === 'focused') {
            ctx.fillStyle = `hsla(${hue}, 86%, 68%, ${alpha * 0.45})`
            ctx.beginPath()
            ctx.arc(projected.x, projected.y, 2.2 * projected.scale, 0, TAU)
            ctx.fill()
        }
    }
}

function drawEntanglementLinks() {
    if (!ctx || settings.entanglementStrength <= 0) return
    ctx.lineWidth = 0.55
    for (let i = 0; i < particles.length; i++) {
        const a = particles[i]
        if (a.entanglementId < 0) continue
        const visibleA = a.mode === 1 || a.mode === 3 || a.measurement !== 'unresolved'
        if (!visibleA && i % 5 !== 0) continue
        const projectedA = projectParticle(a)

        for (let j = i + 1; j < Math.min(particles.length, i + 6); j++) {
            const b = particles[j]
            if (b.entanglementId !== a.entanglementId) continue
            if (!showQuarkBinding.value && isQuarkBindingPair(a, b)) continue
            const visibleB = b.mode === 1 || b.mode === 3 || b.measurement !== 'unresolved'
            if (!visibleA && !visibleB) continue

            const projectedB = projectParticle(b)
            const distance = Math.hypot(projectedB.x - projectedA.x, projectedB.y - projectedA.y)
            if (distance > Math.min(viewportWidth, viewportHeight) * 0.48) continue
            const alpha = (0.035 + Math.min(a.coherence, b.coherence) * 0.055) * settings.entanglementStrength
            ctx.strokeStyle = `rgba(183, 144, 255, ${alpha})`
            ctx.beginPath()
            ctx.moveTo(projectedA.x, projectedA.y)
            ctx.lineTo(projectedB.x, projectedB.y)
            ctx.stroke()
        }
    }
}

function drawLookingGlass() {
    if (!ctx || !lookingGlassEnabled.value) return
    const x = lookingGlass.x || width * 0.5
    const y = lookingGlass.y || height * 0.5
    const radius = settings.measurementRadius
    const active = lookingGlass.active || frame <= lookingGlass.pulseUntil

    ctx.save()
    if (measurementKind.value === 'split') {
        const split = radius * 0.48
        for (const side of [-1, 1]) {
            const lx = x + side * split
            const gradient = ctx.createRadialGradient(lx, y, radius * 0.05, lx, y, radius)
            gradient.addColorStop(0, active ? 'rgba(255, 255, 255, 0.07)' : 'rgba(255, 255, 255, 0.026)')
            gradient.addColorStop(0.62, side < 0 ? 'rgba(111, 245, 190, 0.052)' : 'rgba(184, 138, 255, 0.052)')
            gradient.addColorStop(1, 'rgba(111, 245, 190, 0)')
            ctx.fillStyle = gradient
            ctx.beginPath()
            ctx.arc(lx, y, radius, 0, TAU)
            ctx.fill()

            ctx.setLineDash(active ? [] : [6, 8])
            ctx.strokeStyle = side < 0 ? 'rgba(111, 245, 190, 0.38)' : 'rgba(184, 138, 255, 0.38)'
            ctx.lineWidth = active ? 1.1 : 0.85
            ctx.beginPath()
            ctx.arc(lx, y, radius, 0, TAU)
            ctx.stroke()
        }

        ctx.setLineDash([])
        ctx.strokeStyle = active ? 'rgba(255, 245, 190, 0.54)' : 'rgba(255, 245, 190, 0.28)'
        ctx.beginPath()
        ctx.moveTo(x, y - 12)
        ctx.lineTo(x, y + 12)
        ctx.stroke()
        ctx.restore()
        return
    }

    const gradient = ctx.createRadialGradient(x, y, radius * 0.05, x, y, radius)
    gradient.addColorStop(0, active ? 'rgba(255, 255, 255, 0.08)' : 'rgba(255, 255, 255, 0.035)')
    const operatorGlow = measurementKind.value === 'interference'
        ? 'rgba(103, 232, 249, 0.055)'
        : measurementKind.value === 'whichPath'
            ? 'rgba(253, 230, 138, 0.06)'
            : 'rgba(111, 245, 190, 0.055)'
    gradient.addColorStop(0.62, active ? operatorGlow : 'rgba(111, 245, 190, 0.025)')
    gradient.addColorStop(1, 'rgba(111, 245, 190, 0)')
    ctx.fillStyle = gradient
    ctx.beginPath()
    ctx.arc(x, y, radius, 0, TAU)
    ctx.fill()

    ctx.setLineDash(active ? [] : [6, 8])
    ctx.strokeStyle = active ? 'rgba(255, 245, 190, 0.58)' : 'rgba(111, 245, 190, 0.3)'
    ctx.lineWidth = active ? 1.25 : 0.9
    ctx.beginPath()
    ctx.arc(x, y, radius, 0, TAU)
    ctx.stroke()

    ctx.setLineDash([])
    ctx.strokeStyle = active ? 'rgba(255, 245, 190, 0.5)' : 'rgba(111, 245, 190, 0.24)'
    ctx.beginPath()
    ctx.moveTo(x - 9, y)
    ctx.lineTo(x + 9, y)
    ctx.moveTo(x, y - 9)
    ctx.lineTo(x, y + 9)
    ctx.stroke()
    ctx.restore()
}

function drawGeometryField() {
    if (!ctx) return
    ctx.save()
    ctx.strokeStyle = 'rgba(148, 163, 184, 0.18)'
    ctx.lineWidth = 1
    ctx.setLineDash([10, 14])
    ctx.strokeRect(0, 0, width, height)
    ctx.setLineDash([])
    ctx.strokeStyle = 'rgba(111, 245, 190, 0.16)'
    ctx.beginPath()
    ctx.moveTo(width * 0.5 - 14, height * 0.5)
    ctx.lineTo(width * 0.5 + 14, height * 0.5)
    ctx.moveTo(width * 0.5, height * 0.5 - 14)
    ctx.lineTo(width * 0.5, height * 0.5 + 14)
    ctx.stroke()
    ctx.restore()

    if (geometry.load <= 0) return
    const projected = projectPoint(geometry.x, geometry.y, geometry.z)
    const radius = 32 + geometry.load * 140 + geometry.pressure * 120
    const gradient = ctx.createRadialGradient(projected.x, projected.y, 0, projected.x, projected.y, radius)
    gradient.addColorStop(0, `rgba(105, 160, 255, ${0.08 + geometry.pressure * 0.1})`)
    gradient.addColorStop(1, 'rgba(105, 160, 255, 0)')
    ctx.fillStyle = gradient
    ctx.beginPath()
    ctx.arc(projected.x, projected.y, radius, 0, TAU)
    ctx.fill()

}

function drawCompositeLinks() {
    if (!ctx) return
    const linkRadius2 = 24 * 24
    ctx.lineWidth = 0.65
    for (let i = 0; i < particles.length; i += 2) {
        const a = particles[i]
        if (a.mode !== 1 && a.mode !== 3) continue
        const projectedA = projectParticle(a)
        for (let j = i + 1; j < Math.min(particles.length, i + 80); j++) {
            const b = particles[j]
            if (b.mode !== 1 && b.mode !== 3) continue
            if (!showQuarkBinding.value && isQuarkBindingPair(a, b)) continue
            if (a.lens + b.lens !== 0 && a.nil !== b.nil) continue
            const projectedB = projectParticle(b)
            const dx = projectedB.x - projectedA.x
            const dy = projectedB.y - projectedA.y
            const d2 = dx * dx + dy * dy
            if (d2 > linkRadius2) continue
            const alpha = 0.16 * (1 - d2 / linkRadius2)
            ctx.strokeStyle = `rgba(255, 226, 143, ${alpha})`
            ctx.beginPath()
            ctx.moveTo(projectedA.x, projectedA.y)
            ctx.lineTo(projectedB.x, projectedB.y)
            ctx.stroke()
        }
    }
}

function loop() {
    stepSimulation()
    draw()
    animationId = requestAnimationFrame(loop)
}

function onPointerDown(event: PointerEvent) {
    const screen = canvasPointFromEvent(event)
    const world = screenToWorld(screen.x, screen.y)
    const target = event.currentTarget as HTMLCanvasElement | null
    target?.setPointerCapture(event.pointerId)
    pointer.active = true
    pointer.id = event.pointerId
    pointer.x = world.x
    pointer.y = world.y
    pointer.lastX = world.x
    pointer.lastY = world.y
    pointer.screenX = screen.x
    pointer.screenY = screen.y
    pointer.lastScreenX = screen.x
    pointer.lastScreenY = screen.y
    pointer.dragMode = dragArena.value && (event.altKey || event.shiftKey || event.button === 1) ? 'pan' : 'field'
    if (pointer.dragMode === 'field') {
        lookingGlass.x = world.x
        lookingGlass.y = world.y
        lookingGlass.active = lookingGlassEnabled.value
        lookingGlass.pulseUntil = frame + 34
    } else {
        lookingGlass.active = false
    }
}

function onPointerMove(event: PointerEvent) {
    const screen = canvasPointFromEvent(event)
    const world = screenToWorld(screen.x, screen.y)
    if (pointer.active && pointer.dragMode === 'pan') {
        camera.x += screen.x - pointer.lastScreenX
        camera.y += screen.y - pointer.lastScreenY
        pointer.lastScreenX = screen.x
        pointer.lastScreenY = screen.y
        lookingGlass.active = false
        return
    }
    pointer.x = world.x
    pointer.y = world.y
    lookingGlass.x = world.x
    lookingGlass.y = world.y
    if (pointer.active) {
        lookingGlass.active = lookingGlassEnabled.value
        if (lookingGlass.active) lookingGlass.pulseUntil = frame + 18
    }
}

function onPointerUp(event?: PointerEvent) {
    const target = event?.currentTarget as HTMLCanvasElement | null | undefined
    if (event && pointer.id === event.pointerId) target?.releasePointerCapture(event.pointerId)
    pointer.active = false
    pointer.id = -1
    lookingGlass.active = false
}

function onCanvasWheel(event: WheelEvent) {
    const screen = canvasPointFromEvent(event)
    const direction = event.deltaY > 0 ? 0.9 : 1.1
    setCameraZoom(camera.zoom * direction, screen.x, screen.y)
}

onMounted(() => {
    resizeCanvas()
    applyInitialPresetFromQuery()
    window.addEventListener('resize', resizeCanvas)
    animationId = requestAnimationFrame(loop)
})

onUnmounted(() => {
    window.removeEventListener('resize', resizeCanvas)
    cancelAnimationFrame(animationId)
})
</script>

<style scoped>
.proto-shell {
    position: relative;
    height: 100vh;
    overflow: hidden;
    background: #03060d;
    color: #eef7f4;
}

.proto-canvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    background:
        radial-gradient(circle at 50% 48%, rgba(42, 157, 143, 0.12), transparent 30%),
        linear-gradient(180deg, rgba(6, 12, 22, 0.9), rgba(3, 6, 13, 1));
    cursor: grab;
}

.proto-canvas:active {
    cursor: grabbing;
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
.metrics-panel,
.sm-rail {
    pointer-events: auto;
}

.home-link,
.icon-button,
.segmented button,
.build-actions button,
.measure-tabs button,
.view-tabs button,
.orbital-tabs button,
.toggle-row button,
.zoom-actions button {
    border: 1px solid rgba(130, 153, 170, 0.35);
    background: rgba(13, 20, 32, 0.78);
    color: #e8f4f1;
    backdrop-filter: blur(10px);
    transition: background 0.16s ease, border-color 0.16s ease, color 0.16s ease;
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
    font-weight: 700;
}

.home-link:hover,
.icon-button:hover,
.segmented button:hover,
.build-actions button:hover,
.measure-tabs button:hover,
.view-tabs button:hover,
.orbital-tabs button:hover,
.toggle-row button:hover,
.zoom-actions button:hover {
    background: rgba(24, 38, 56, 0.9);
    border-color: rgba(111, 245, 190, 0.55);
}

.title-wrap {
    min-width: 0;
    text-align: center;
    text-shadow: 0 1px 2px rgba(0, 0, 0, 0.72);
}

.title-row {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
}

.title-row h1 {
    margin: 0;
    font-size: 21px;
    line-height: 1.1;
    font-weight: 900;
}

.title-icon {
    color: #6ff5be;
    font-size: 24px;
}

.mode-pill {
    border-radius: 7px;
    padding: 3px 7px;
    border: 1px solid rgba(217, 156, 255, 0.38);
    color: #e3c2ff;
    background: rgba(140, 70, 180, 0.23);
    font-size: 11px;
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
}

.interpretive-pill {
    border-color: rgba(253, 230, 138, 0.38);
    color: #fde68a;
    background: rgba(108, 87, 32, 0.28);
}

.title-wrap p {
    margin: 5px 0 0;
    color: rgba(226, 242, 239, 0.76);
    font-size: 13px;
}

.top-actions {
    display: flex;
    gap: 8px;
    justify-content: flex-end;
}

.icon-button {
    display: grid;
    place-items: center;
    width: 36px;
    height: 36px;
    border-radius: 8px;
    font-size: 18px;
}

.control-panel {
    position: absolute;
    left: 14px;
    top: 68px;
    width: min(330px, calc(100vw - 28px));
    max-height: calc(100vh - 92px);
    overflow: auto;
    display: flex;
    flex-direction: column;
    gap: 10px;
}

.panel-section,
.metrics-panel,
.sm-legend,
.invariant-ledger,
.source-audit,
.legend {
    border: 1px solid rgba(130, 153, 170, 0.28);
    background: rgba(8, 14, 24, 0.78);
    backdrop-filter: blur(12px);
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.24);
}

.panel-section {
    border-radius: 8px;
    padding: 12px;
}

.panel-section h2 {
    margin: 0 0 10px;
    color: #dff6f3;
    font-size: 13px;
    line-height: 1;
    text-transform: uppercase;
    font-weight: 800;
}

.segmented,
.build-actions,
.measure-tabs,
.view-tabs,
.orbital-tabs,
.toggle-row {
    display: grid;
    gap: 6px;
}

.segmented {
    grid-template-columns: repeat(2, minmax(0, 1fr));
}

.build-actions {
    grid-template-columns: repeat(2, minmax(0, 1fr));
}

.build-actions button {
    min-width: 0;
    min-height: 34px;
    border-radius: 7px;
    padding: 0 8px;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 6px;
    font-size: 12px;
    font-weight: 800;
}

.build-actions button:first-child {
    grid-column: 1 / -1;
    color: #ffd1d8;
    border-color: rgba(251, 113, 133, 0.45);
}

.build-actions button span {
    flex: 0 0 auto;
    font-size: 15px;
}

.build-actions button b {
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.measure-tabs {
    grid-template-columns: repeat(4, minmax(0, 1fr));
    margin: 6px 0 8px;
}

.view-tabs {
    grid-template-columns: repeat(4, minmax(0, 1fr));
    margin-bottom: 8px;
}

.orbital-tabs {
    grid-template-columns: repeat(2, minmax(0, 1fr));
    margin-bottom: 8px;
}

.toggle-row {
    grid-template-columns: repeat(5, minmax(0, 1fr));
}

.segmented button,
.build-actions button,
.measure-tabs button,
.view-tabs button,
.orbital-tabs button,
.toggle-row button {
    min-width: 0;
    min-height: 32px;
    border-radius: 7px;
    padding: 0 8px;
    font-size: 12px;
    font-weight: 700;
}

.segmented button.active,
.measure-tabs button.active,
.view-tabs button.active,
.orbital-tabs button.active,
.toggle-row button.active {
    color: #06211a;
    background: #6ff5be;
    border-color: rgba(111, 245, 190, 0.9);
}

label {
    display: grid;
    grid-template-columns: 72px minmax(0, 1fr) 48px;
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
    accent-color: #6ff5be;
}

.checkbox-row {
    grid-template-columns: 18px 1fr;
    margin-top: 8px;
    gap: 8px;
}

.zoom-actions {
    display: grid;
    grid-template-columns: repeat(3, 36px);
    gap: 8px;
    margin-top: 6px;
}

.zoom-actions button {
    display: grid;
    place-items: center;
    width: 36px;
    height: 32px;
    border-radius: 7px;
    font-size: 16px;
}

.engine-status {
    display: grid;
    grid-template-columns: 20px minmax(0, 1fr);
    gap: 8px 10px;
    align-items: center;
    color: rgba(226, 242, 239, 0.82);
}

.engine-status > span {
    color: #6ff5be;
    font-size: 18px;
}

.engine-status strong {
    color: #edfdf9;
    font-size: 12px;
}

.engine-status em {
    grid-column: 1 / -1;
    color: rgba(203, 219, 214, 0.68);
    font-size: 11px;
    line-height: 1.35;
    font-style: normal;
}

.metrics-panel {
    position: absolute;
    right: 14px;
    top: 72px;
    width: 178px;
    max-height: 326px;
    overflow: auto;
    border-radius: 8px;
    padding: 10px;
    display: grid;
    gap: 7px;
}

.metric {
    display: flex;
    justify-content: space-between;
    gap: 10px;
    font-size: 12px;
    color: rgba(226, 242, 239, 0.78);
}

.metric strong {
    color: #ffffff;
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
}

.sm-rail {
    position: absolute;
    right: 14px;
    top: 430px;
    width: 224px;
    max-height: calc(100vh - 444px);
    overflow: auto;
    display: grid;
    gap: 10px;
}

.sm-legend,
.invariant-ledger,
.source-audit {
    border-radius: 8px;
    padding: 10px;
    display: grid;
    gap: 8px;
}

.sm-legend h2,
.invariant-ledger h2,
.source-audit h2 {
    margin: 0 0 2px;
    color: #dff6f3;
    font-size: 12px;
    line-height: 1;
    text-transform: uppercase;
    font-weight: 800;
}

.source-item {
    display: grid;
    grid-template-columns: 52px minmax(0, 1fr);
    gap: 8px;
    align-items: center;
    color: rgba(226, 242, 239, 0.82);
}

.source-item > i {
    border-radius: 999px;
    padding: 3px 5px;
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
    background: #6ff5be;
}

.source-item.derived > i {
    background: #67e8f9;
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
    color: rgba(203, 219, 214, 0.62);
    font-size: 10px;
    line-height: 1.18;
    font-style: normal;
}

.sm-legend-item {
    display: grid;
    grid-template-columns: 12px minmax(0, 1fr);
    align-items: center;
    gap: 8px;
    color: rgba(226, 242, 239, 0.82);
    font-size: 11px;
    line-height: 1.2;
}

.sm-legend-item i {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    border: 1px solid rgba(255, 255, 255, 0.28);
}

.ledger-item {
    display: grid;
    grid-template-columns: 10px minmax(0, 1fr) auto;
    gap: 8px;
    align-items: center;
    color: rgba(226, 242, 239, 0.82);
}

.ledger-item > i {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    background: #94a3b8;
    box-shadow: 0 0 10px rgba(148, 163, 184, 0.35);
}

.ledger-item.pass > i {
    background: #6ff5be;
    box-shadow: 0 0 12px rgba(111, 245, 190, 0.48);
}

.ledger-item.warn > i {
    background: #fde68a;
    box-shadow: 0 0 12px rgba(253, 230, 138, 0.44);
}

.ledger-item.fail > i {
    background: #fb7185;
    box-shadow: 0 0 12px rgba(251, 113, 133, 0.46);
}

.ledger-item span {
    min-width: 0;
    display: grid;
    gap: 2px;
}

.ledger-item strong {
    color: #edfdf9;
    font-size: 11px;
    line-height: 1.1;
}

.ledger-item em {
    color: rgba(203, 219, 214, 0.62);
    font-size: 10px;
    line-height: 1.15;
    font-style: normal;
}

.ledger-item b {
    color: #ffffff;
    font-family: ui-monospace, SFMono-Regular, Consolas, monospace;
    font-size: 10px;
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

.dot.anchor {
    background: #6ff5be;
}

.dot.cancel {
    background: #b88aff;
}

.dot.free {
    background: #96b1cd;
}

.dot.glass {
    background: #fff2be;
}

@media (max-width: 860px) {
    .topbar {
        left: 10px;
        right: 10px;
        grid-template-columns: minmax(0, 1fr) auto;
        gap: 8px;
    }

    .title-wrap {
        display: none;
    }

    .control-panel {
        left: 10px;
        width: calc(100vw - 20px);
        top: auto;
        bottom: 52px;
        max-height: 46vh;
        overflow: auto;
    }

    .metrics-panel {
        top: 62px;
        right: auto;
        left: 10px;
        width: 154px;
    }

    .sm-rail {
        display: none;
    }

    .metric {
        font-size: 11px;
    }

    .legend {
        display: none;
    }
}
</style>
