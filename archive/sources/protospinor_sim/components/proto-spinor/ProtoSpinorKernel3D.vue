<template>
    <section ref="shellRef" class="proto3d-shell">
        <canvas ref="canvasRef" class="proto3d-canvas" @pointerdown="onPointerDown" @pointermove="onPointerMove" @pointerup="onPointerUp" @pointerleave="onPointerUp"></canvas>

        <header class="topbar">
            <NuxtLink to="/" class="home-link" title="Home">
                <span class="i-tabler-arrow-left"></span>
                <span>SandboxScience</span>
            </NuxtLink>
            <div class="title-wrap">
                <div class="title-row">
                    <span class="i-tabler-atom-2 title-icon"></span>
                    <h1>Proto-Spinor Kernel 3D</h1>
                    <span class="mode-pill">Three.js</span>
                    <span class="mode-pill bridge-pill">MTT + energy bridge</span>
                    <span class="mode-pill interpretive-pill">labels: interp.</span>
                </div>
                <p>Upper-world carriers in 3D, with SM labels as interpretive overlays.</p>
            </div>
            <div class="top-actions">
                <button type="button" class="icon-button" :title="isRunning ? 'Pause' : 'Run'" @click="toggleRunning">
                    <span :class="isRunning ? 'i-tabler-player-pause' : 'i-tabler-player-play'"></span>
                </button>
                <button type="button" class="icon-button" title="Reset" @click="resetSimulation">
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
                <h2>Forces</h2>
                <label class="checkbox-row">
                    <input v-model="settings.nativeMtt" type="checkbox">
                    <span>Native MTT</span>
                </label>
                <label class="checkbox-row">
                    <input v-model="settings.energyBridge" type="checkbox">
                    <span>Energy bridge</span>
                </label>
                <label>
                    <span>Particles</span>
                    <input v-model.number="settings.particleCount" type="range" min="48" max="720" step="24" @change="resetSimulation">
                    <strong>{{ settings.particleCount }}</strong>
                </label>
                <label>
                    <span>MTT</span>
                    <input v-model.number="settings.nativeStrength" type="range" min="0" max="1.8" step="0.02">
                    <strong>{{ settings.nativeStrength.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Ledger</span>
                    <input v-model.number="settings.ledgerStrength" type="range" min="0" max="1.8" step="0.02">
                    <strong>{{ settings.ledgerStrength.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Spread</span>
                    <input v-model.number="settings.carrierSpread" type="range" min="0.6" max="2.4" step="0.02">
                    <strong>{{ settings.carrierSpread.toFixed(2) }}</strong>
                </label>
                <label>
                    <span>Time</span>
                    <input v-model.number="settings.timeScale" type="range" min="0.2" max="1.4" step="0.02">
                    <strong>{{ settings.timeScale.toFixed(2) }}</strong>
                </label>
            </section>

            <section class="panel-section">
                <h2>Build</h2>
                <div class="build-actions">
                    <button type="button" title="Clear all carriers and molecule declarations" @click="clearSimulation">
                        <span class="i-tabler-trash"></span>
                        <b>Clear</b>
                    </button>
                    <button type="button" title="Add a zero-net-momentum energy pulse" @click="addEnergyPulse">
                        <span class="i-tabler-flame"></span>
                        <b>Energy</b>
                    </button>
                    <button type="button" title="Add one free electron cloud; net arena charge changes by -1" @click="addEntity('electron')">
                        <span class="i-tabler-bolt"></span>
                        <b>e-</b>
                    </button>
                    <button type="button" title="Add a conserved electron-positron pair" @click="addEntity('electronPair')">
                        <span class="i-tabler-arrows-exchange"></span>
                        <b>e-/e+</b>
                    </button>
                    <button type="button" title="Add a conserved muon-antimuon pair" @click="addEntity('muonPair')">
                        <span class="i-tabler-wave-saw-tool"></span>
                        <b>mu-/mu+</b>
                    </button>
                    <button type="button" title="Add a conserved neutrino-antineutrino pair" @click="addEntity('neutrinoPair')">
                        <span class="i-tabler-circle-dashed"></span>
                        <b>nu/anti-nu</b>
                    </button>
                    <button type="button" title="Add a neutral photon wave packet" @click="addEntity('photon')">
                        <span class="i-tabler-sun-electricity"></span>
                        <b>gamma</b>
                    </button>
                    <button type="button" title="Add one proton-like RGB quark triplet" @click="addEntity('proton')">
                        <span class="i-tabler-circle-plus"></span>
                        <b>p+</b>
                    </button>
                    <button type="button" title="Add one neutron-like RGB quark triplet" @click="addEntity('neutron')">
                        <span class="i-tabler-circle"></span>
                        <b>n</b>
                    </button>
                    <button type="button" title="Add an interpretive hydrogen atom seed" @click="addEntity('hydrogen')">
                        <span class="i-tabler-atom"></span>
                        <b>H</b>
                    </button>
                    <button type="button" title="Add an interpretive deuterium atom seed" @click="addEntity('deuterium')">
                        <span class="i-tabler-atom"></span>
                        <b>D</b>
                    </button>
                    <button type="button" title="Add an interpretive helium-4 atom seed" @click="addEntity('helium4')">
                        <span class="i-tabler-atom-2"></span>
                        <b>He-4</b>
                    </button>
                    <button type="button" title="Add an interpretive hydrogen molecule seed" @click="addEntity('h2')">
                        <span class="i-tabler-circles"></span>
                        <b>H2</b>
                    </button>
                    <button type="button" title="Add an interpretive water molecule seed with bent closure bonds" @click="addEntity('water')">
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
                    <input v-model.number="settings.measurementRadius" type="range" min="18" max="130" step="2">
                    <strong>{{ settings.measurementRadius.toFixed(0) }}</strong>
                </label>
                <label>
                    <span>Focus</span>
                    <input v-model.number="settings.measurementStrength" type="range" min="0" max="1.4" step="0.02">
                    <strong>{{ settings.measurementStrength.toFixed(2) }}</strong>
                </label>
            </section>

            <section class="panel-section">
                <h2>View</h2>
                <div class="toggle-row">
                    <button type="button" :class="{ active: showNuclei }" @click="showNuclei = !showNuclei">Nuclei</button>
                    <button type="button" :class="{ active: showAtomShells }" @click="showAtomShells = !showAtomShells">Atoms</button>
                    <button type="button" :class="{ active: showParticles }" @click="showParticles = !showParticles">Carriers</button>
                    <button type="button" :class="{ active: showCores }" @click="showCores = !showCores">Cores</button>
                    <button type="button" :class="{ active: showPhotons }" @click="showPhotons = !showPhotons">Waves</button>
                    <button type="button" :class="{ active: showInternalCarriers }" @click="showInternalCarriers = !showInternalCarriers">Inside</button>
                    <button type="button" :class="{ active: showMolecularBonds }" @click="showMolecularBonds = !showMolecularBonds">Bonds</button>
                    <button type="button" :class="{ active: showCarrierRings }" @click="showCarrierRings = !showCarrierRings">Rings</button>
                    <button type="button" :class="{ active: showLookingGlass }" @click="showLookingGlass = !showLookingGlass">Glass</button>
                    <button type="button" :class="{ active: showLegend }" @click="showLegend = !showLegend">Legend</button>
                </div>
            </section>
        </aside>

        <aside class="metric-panel">
            <div v-for="metric in metricCards" :key="metric.label" class="metric">
                <span>{{ metric.label }}</span>
                <strong>{{ metric.value }}</strong>
            </div>
        </aside>

        <aside v-if="showLegend" class="legend-panel">
            <section class="sm-legend">
                <h2>SM overlays</h2>
                <div v-for="item in smLegendItems" :key="item.label" class="sm-legend-item">
                    <i :style="{ background: item.color, boxShadow: `0 0 12px ${item.glow}` }"></i>
                    <span>{{ item.label }}</span>
                </div>
            </section>
            <section class="invariant-ledger">
                <h2>Ledger</h2>
                <div v-for="item in invariantLedger" :key="item.label" class="ledger-item" :class="item.status">
                    <i></i>
                    <span>
                        <strong>{{ item.label }}</strong>
                        <em>{{ item.detail }}</em>
                    </span>
                    <b>{{ item.value }}</b>
                </div>
            </section>
        </aside>
    </section>
</template>

<script setup lang="ts">
import * as THREE from 'three'
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls.js'

type PresetId = 'sm' | 'oneAtom' | 'cloud'
type SmKind = 'electron' | 'positron' | 'muon' | 'antimuon' | 'quarkR' | 'quarkG' | 'quarkB' | 'photon' | 'gluon' | 'neutrino' | 'antineutrino' | 'generic'
type GaugeColor = 'none' | 'red' | 'green' | 'blue'
type NucleonKind = 'proton' | 'neutron'
type SpawnKind = 'electron' | 'electronPair' | 'muonPair' | 'neutrinoPair' | 'photon' | 'proton' | 'neutron' | 'hydrogen' | 'deuterium' | 'helium4' | 'h2' | 'water' | 'waterCluster'
type MeasurementKind = 'projector' | 'interference' | 'whichPath' | 'split'
type LedgerStatus = 'pass' | 'warn' | 'fail'

interface ProtoParticle3D {
    id: number
    packetId: number
    slot: number
    kind: SmKind
    position: THREE.Vector3
    velocity: THREE.Vector3
    force: THREE.Vector3
    theta: number
    sigma: number
    lens: -1 | 0 | 1
    nil: -1 | 0 | 1 | 2
    charge: number
    spin: number
    color: GaugeColor
    coherence: number
    recurrence: number
    J: number
    mass: number
    radius: number
    age: number
    atomId: number
    moleculeId: number
    measurement: 'unresolved' | 'focused' | 'split'
    label: string
}

interface NucleusCandidate {
    packetId: number
    kind: NucleonKind
    indices: number[]
    charge: number
    center: THREE.Vector3
    velocity: THREE.Vector3
    stability: number
    atomId: number
    moleculeId: number
}

interface AtomAggregate3D {
    atomId: number
    moleculeId: number
    center: THREE.Vector3
    velocity: THREE.Vector3
    protonCount: number
    neutronCount: number
    stability: number
    electronIndices: number[]
    nucleusParticleIndices: number[]
    allParticleIndices: number[]
}

interface EnergyLedger3D {
    kinetic: number
    native: number
    coulomb: number
    string: number
    pauli: number
    orbital: number
    photon: number
    radiated: number
    total: number
}

interface DeclaredBond3D {
    moleculeId: number
    atomA: number
    atomB: number
    a: THREE.Vector3
    b: THREE.Vector3
    kind: 'covalent' | 'hydrogen'
    restLength: number
}

interface InvariantEntry {
    label: string
    detail: string
    value: string
    status: LedgerStatus
}

const TAU = Math.PI * 2
const WORLD_RADIUS = 170
const MAX_PARTICLES = 900
const MAX_NUCLEI = 240
const MAX_ATOMS = 180
const MAX_LINKS = 1400
const MAX_BONDS = 320

const shellRef = ref<HTMLElement | null>(null)
const canvasRef = ref<HTMLCanvasElement | null>(null)
const isRunning = ref(true)
const activePreset = ref<PresetId>('sm')
const lookingGlassEnabled = ref(true)
const measurementKind = ref<MeasurementKind>('projector')
const showParticles = ref(true)
const showCores = ref(true)
const showPhotons = ref(true)
const showNuclei = ref(true)
const showAtomShells = ref(true)
const showInternalCarriers = ref(false)
const showQuarkBinding = ref(false)
const showMolecularBonds = ref(true)
const showCarrierRings = ref(true)
const showLookingGlass = ref(true)
const showLegend = ref(true)

const settings = reactive({
    particleCount: 240,
    nativeMtt: true,
    energyBridge: true,
    nativeStrength: 0.9,
    ledgerStrength: 0.78,
    carrierSpread: 1.25,
    timeScale: 0.78,
    measurementRadius: 58,
    measurementStrength: 0.72,
})

const metrics = reactive({
    particles: 0,
    nuclei: 0,
    protons: 0,
    neutrons: 0,
    atoms: 0,
    molecules: 0,
    photons: 0,
    electrons: 0,
    muons: 0,
    netCharge: 0,
    kinetic: 0,
    native: 0,
    coulomb: 0,
    string: 0,
    pauli: 0,
    orbital: 0,
    radiated: 0,
    drift: 0,
    colorClosure: 0,
    closureCost: 0,
    measurementHits: 0,
})

const metricCards = computed(() => [
    { label: 'Particles', value: metrics.particles.toString() },
    { label: 'Nuclei', value: metrics.nuclei.toString() },
    { label: 'p+', value: metrics.protons.toString() },
    { label: 'n', value: metrics.neutrons.toString() },
    { label: 'Atoms', value: metrics.atoms.toString() },
    { label: 'Molecules', value: metrics.molecules.toString() },
    { label: 'Photons', value: metrics.photons.toString() },
    { label: 'e-', value: metrics.electrons.toString() },
    { label: 'mu', value: metrics.muons.toString() },
    { label: 'Net Q', value: metrics.netCharge.toFixed(2) },
    { label: 'K', value: metrics.kinetic.toFixed(1) },
    { label: 'U MTT', value: metrics.native.toFixed(2) },
    { label: 'U EM', value: metrics.coulomb.toFixed(2) },
    { label: 'U string', value: metrics.string.toFixed(2) },
    { label: 'U Pauli', value: metrics.pauli.toFixed(2) },
    { label: 'U orb', value: metrics.orbital.toFixed(2) },
    { label: 'Rad', value: metrics.radiated.toFixed(2) },
    { label: 'Closure', value: metrics.closureCost.toFixed(2) },
    { label: 'Drift', value: metrics.drift.toFixed(2) },
])

const smLegendItems = [
    { label: 'aggregate nucleus', color: '#ff9f3d', glow: 'rgba(255, 159, 61, 0.58)' },
    { label: 'atom shell aggregate', color: '#8bdcff', glow: 'rgba(139, 220, 255, 0.44)' },
    { label: 'electron cloud', color: '#38dfff', glow: 'rgba(56, 223, 255, 0.55)' },
    { label: 'positron / anti-lepton', color: '#ff6678', glow: 'rgba(255, 102, 120, 0.55)' },
    { label: 'internal RGB carriers', color: '#77ffe0', glow: 'rgba(119, 255, 224, 0.5)' },
    { label: 'photon wave carrier', color: '#ffe66d', glow: 'rgba(255, 230, 109, 0.55)' },
    { label: 'measurement sphere', color: '#fef3c7', glow: 'rgba(254, 243, 199, 0.5)' },
    { label: 'molecular bond', color: '#fde68a', glow: 'rgba(253, 230, 138, 0.5)' },
]

const invariantLedger = computed<InvariantEntry[]>(() => {
    const chargeDrift = Math.abs(metrics.netCharge - baselineCharge)
    const energyScale = Math.max(1, Math.abs(metrics.kinetic + metrics.native + metrics.coulomb + metrics.string + metrics.pauli + metrics.orbital))
    const driftShare = Math.abs(metrics.drift) / energyScale
    return [
        {
            label: 'Charge',
            detail: 'arena charge vs reset baseline',
            value: formatSignedCharge(metrics.netCharge - baselineCharge),
            status: chargeDrift < 0.001 ? 'pass' : chargeDrift < 1.001 ? 'warn' : 'fail',
        },
        {
            label: 'Color',
            detail: 'RGB closure inside triplets',
            value: `${Math.round(metrics.colorClosure * 100)}%`,
            status: scoreStatus(metrics.colorClosure, 0.98, 0.75),
        },
        {
            label: 'Energy',
            detail: 'toy ledger drift',
            value: metrics.drift.toFixed(2),
            status: driftShare < 0.18 ? 'pass' : driftShare < 0.5 ? 'warn' : 'fail',
        },
        {
            label: 'MTT closure',
            detail: 'J/coherence/recurrence cost',
            value: metrics.closureCost.toFixed(3),
            status: metrics.closureCost < 0.24 ? 'pass' : metrics.closureCost < 0.42 ? 'warn' : 'fail',
        },
        {
            label: 'Measure',
            detail: measurementKind.value,
            value: metrics.measurementHits.toString(),
            status: lookingGlassEnabled.value ? 'pass' : 'warn',
        },
    ]
})

const presets = [
    { id: 'sm' as PresetId, label: 'SM 3D', particles: 240, nativeStrength: 0.9, ledgerStrength: 0.78, carrierSpread: 1.25 },
    { id: 'oneAtom' as PresetId, label: 'One Atom', particles: 48, nativeStrength: 1.05, ledgerStrength: 0.92, carrierSpread: 1.55 },
    { id: 'cloud' as PresetId, label: 'Cloud', particles: 360, nativeStrength: 0.7, ledgerStrength: 0.58, carrierSpread: 1.7 },
]

function clamp01(value: number) {
    return Math.max(0, Math.min(1, value))
}

function scoreStatus(value: number, pass: number, warn: number): LedgerStatus {
    if (value >= pass) return 'pass'
    if (value >= warn) return 'warn'
    return 'fail'
}

function formatSignedCharge(value: number) {
    if (Math.abs(value) < 0.001) return '0.00'
    return `${value > 0 ? '+' : ''}${value.toFixed(2)}`
}

function canAddParticles(count: number) {
    return particles.length + count <= MAX_PARTICLES
}

function spawnSite(radius = 32) {
    if (lookingGlass.center.lengthSq() > 0.01) return lookingGlass.center.clone()
    return randUnitVector().multiplyScalar(Math.random() * radius)
}

function offsetPoint(origin: THREE.Vector3, radius: number, angle: number, z = 0) {
    return origin.clone().add(new THREE.Vector3(Math.cos(angle) * radius, Math.sin(angle) * radius, z * WORLD_RADIUS))
}

let renderer: THREE.WebGLRenderer | null = null
let scene: THREE.Scene | null = null
let camera: THREE.PerspectiveCamera | null = null
let controls: OrbitControls | null = null
let particleMesh: THREE.InstancedMesh | null = null
let particlePoints: THREE.Points | null = null
let pointGeometry: THREE.BufferGeometry | null = null
let pointPositions: Float32Array | null = null
let pointColors: Float32Array | null = null
let nucleusMesh: THREE.InstancedMesh | null = null
let atomShellMesh: THREE.InstancedMesh | null = null
let photonMesh: THREE.InstancedMesh | null = null
let linkGeometry: THREE.BufferGeometry | null = null
let linkPositions: Float32Array | null = null
let linkColors: Float32Array | null = null
let linkLines: THREE.LineSegments | null = null
let bondGeometry: THREE.BufferGeometry | null = null
let bondPositions: Float32Array | null = null
let bondLines: THREE.LineSegments | null = null
let carrierGroup: THREE.Group | null = null
let measurementMesh: THREE.Mesh | null = null
let measurementSplitA: THREE.Mesh | null = null
let measurementSplitB: THREE.Mesh | null = null
let animationId = 0
let particles: ProtoParticle3D[] = []
let declaredBonds: DeclaredBond3D[] = []
let frame = 0
let nextId = 1
let nextAtomId = 1
let nextMoleculeId = 1
let baselineEnergy: number | null = null
let baselineCharge = 0
let measurementHitsThisFrame = 0

const tempMatrix = new THREE.Matrix4()
const tempQuaternion = new THREE.Quaternion()
const tempScale = new THREE.Vector3()
const tempColor = new THREE.Color()
const axisY = new THREE.Vector3(0, 1, 0)
const raycaster = new THREE.Raycaster()
const pointerNdc = new THREE.Vector2()
const measurePlane = new THREE.Plane(new THREE.Vector3(0, 0, 1), 0)
const tempPoint = new THREE.Vector3()
const lookingGlass = {
    active: false,
    pulseUntil: -1,
    center: new THREE.Vector3(0, 0, 0),
}

function selectPreset(id: PresetId) {
    activePreset.value = id
    const preset = presets.find(item => item.id === id) ?? presets[0]
    settings.particleCount = preset.particles
    settings.nativeStrength = preset.nativeStrength
    settings.ledgerStrength = preset.ledgerStrength
    settings.carrierSpread = preset.carrierSpread
    resetSimulation()
}

function toggleRunning() {
    isRunning.value = !isRunning.value
}

function randUnitVector() {
    const z = Math.random() * 2 - 1
    const a = Math.random() * TAU
    const r = Math.sqrt(Math.max(0, 1 - z * z))
    return new THREE.Vector3(Math.cos(a) * r, Math.sin(a) * r, z)
}

function smKindForSlot(slot: number): SmKind {
    if (slot < 9) return slot % 3 === 0 ? 'quarkR' : slot % 3 === 1 ? 'quarkG' : 'quarkB'
    if (slot < 12) return 'electron'
    if (slot < 15) return 'positron'
    if (slot < 18) return 'neutrino'
    if (slot < 22) return 'photon'
    return 'gluon'
}

function quarkChargeForSlot(slot: number) {
    return Math.floor(slot / 3) === 0 ? 2 / 3 : -1 / 3
}

function chargeForKind(kind: SmKind, slot: number) {
    if (kind === 'electron') return -1
    if (kind === 'positron') return 1
    if (kind === 'muon') return -1
    if (kind === 'antimuon') return 1
    if (kind === 'quarkR' || kind === 'quarkG' || kind === 'quarkB') return quarkChargeForSlot(slot)
    return 0
}

function colorForKind(kind: SmKind): GaugeColor {
    if (kind === 'quarkR') return 'red'
    if (kind === 'quarkG') return 'green'
    if (kind === 'quarkB') return 'blue'
    return 'none'
}

function nilForKind(kind: SmKind, theta: number, sigma: number): -1 | 0 | 1 | 2 {
    if (kind === 'quarkR') return 0
    if (kind === 'quarkG') return 1
    if (kind === 'quarkB') return 2
    if (kind === 'photon' || kind === 'gluon' || kind === 'neutrino' || kind === 'antineutrino') return -1
    return Math.floor((((theta + sigma * 0.5) % TAU + TAU) % TAU) / (TAU / 3)) as 0 | 1 | 2
}

function lensFromCharge(charge: number): -1 | 0 | 1 {
    if (charge < -0.001) return -1
    if (charge > 0.001) return 1
    return 0
}

function kindRadius(kind: SmKind) {
    if (kind === 'photon' || kind === 'gluon') return 2.2
    if (kind === 'electron' || kind === 'positron') return 2.6
    if (kind === 'muon' || kind === 'antimuon') return 3.2
    if (kind === 'neutrino' || kind === 'antineutrino') return 2.0
    if (kind === 'quarkR' || kind === 'quarkG' || kind === 'quarkB') return 2.8
    return 2.4
}

function kindMass(kind: SmKind) {
    if (kind === 'photon' || kind === 'gluon') return 0.18
    if (kind === 'neutrino' || kind === 'antineutrino') return 0.22
    if (kind === 'muon' || kind === 'antimuon') return 0.78
    if (kind === 'quarkR' || kind === 'quarkG' || kind === 'quarkB') return 0.48
    return 0.42
}

function labelForKind(kind: SmKind) {
    if (kind === 'electron') return 'e-'
    if (kind === 'positron') return 'e+'
    if (kind === 'muon') return 'mu-'
    if (kind === 'antimuon') return 'mu+'
    if (kind === 'neutrino') return 'nu'
    if (kind === 'antineutrino') return 'anti-nu'
    if (kind === 'photon') return 'gamma'
    if (kind === 'gluon') return 'g'
    if (kind === 'quarkR' || kind === 'quarkG' || kind === 'quarkB') return quarkChargeForSlot(kind === 'quarkR' ? 0 : kind === 'quarkG' ? 1 : 5) > 0 ? 'u' : 'd'
    return 'carrier'
}

function particleColor(p: ProtoParticle3D) {
    if (p.kind === 'electron') return tempColor.setRGB(0.0, 0.92, 1)
    if (p.kind === 'positron') return tempColor.setRGB(1, 0.18, 0.36)
    if (p.kind === 'muon') return tempColor.setRGB(0.2, 0.52, 1)
    if (p.kind === 'antimuon') return tempColor.setRGB(1, 0.34, 0.78)
    if (p.kind === 'photon') return tempColor.setRGB(1, 0.82, 0.05)
    if (p.kind === 'gluon') return tempColor.setRGB(0.95, 0.42, 1)
    if (p.kind === 'neutrino') return tempColor.setRGB(0.58, 0.62, 1)
    if (p.kind === 'antineutrino') return tempColor.setRGB(0.82, 0.72, 1)
    if (p.color === 'red') return tempColor.setRGB(1, 0.08, 0.08)
    if (p.color === 'green') return tempColor.setRGB(0.05, 1, 0.34)
    if (p.color === 'blue') return tempColor.setRGB(0.16, 0.42, 1)
    return tempColor.setRGB(0.66, 0.74, 0.86)
}

function isInternalQuark(p: ProtoParticle3D) {
    return p.kind === 'quarkR' || p.kind === 'quarkG' || p.kind === 'quarkB'
}

function shouldRenderCarrier(p: ProtoParticle3D) {
    return showInternalCarriers.value || !isInternalQuark(p)
}

function nucleusColor(nucleus: NucleusCandidate) {
    if (nucleus.kind === 'proton') return tempColor.setRGB(1, 0.62, 0.24)
    return tempColor.setRGB(0.72, 0.82, 0.95)
}

function shellRadiusForAtom(atom: Pick<AtomAggregate3D, 'protonCount'>) {
    if (atom.protonCount <= 1) return 38 * settings.carrierSpread
    if (atom.protonCount <= 2) return 44 * settings.carrierSpread
    return (50 + Math.min(20, Math.sqrt(atom.protonCount) * 4.4)) * settings.carrierSpread
}

function visualRadiusForAtom(atom: AtomAggregate3D) {
    if (atom.protonCount <= 1) return 13
    if (atom.protonCount <= 2) return 19
    if (atom.protonCount >= 8) return 30
    return 18 + Math.sqrt(atom.protonCount) * 3.5
}

function atomColor(atom: AtomAggregate3D) {
    if (atom.protonCount === 1 && atom.neutronCount === 0) return tempColor.setRGB(0.5, 0.86, 1)
    if (atom.protonCount === 1) return tempColor.setRGB(0.56, 0.75, 1)
    if (atom.protonCount === 2) return tempColor.setRGB(0.76, 0.66, 1)
    if (atom.protonCount >= 8) return tempColor.setRGB(1, 0.48, 0.38)
    return tempColor.setRGB(0.88, 0.96, 1)
}

function pushParticle(
    kind: SmKind,
    packetId: number,
    slot: number,
    position: THREE.Vector3,
    velocity = randUnitVector().multiplyScalar(0.25),
    options: Partial<Pick<ProtoParticle3D, 'atomId' | 'moleculeId' | 'label' | 'spin'>> = {},
) {
    if (!canAddParticles(1)) return -1
    const theta = Math.random() * TAU
    const sigma = Math.random() * TAU
    const charge = chargeForKind(kind, slot)
    const index = particles.length
    particles.push({
        id: nextId++,
        packetId,
        slot,
        kind,
        position,
        velocity,
        force: new THREE.Vector3(),
        theta,
        sigma,
        lens: lensFromCharge(charge),
        nil: nilForKind(kind, theta, sigma),
        charge,
        spin: options.spin ?? (Math.sin(theta + sigma) >= 0 ? 0.5 : -0.5),
        color: colorForKind(kind),
        coherence: kind === 'photon' || kind === 'gluon' ? 0.68 : 0.76,
        recurrence: kind === 'photon' ? 0.22 : 0.18,
        J: kind === 'photon' ? 0.34 : 0.28,
        mass: kindMass(kind),
        radius: kindRadius(kind),
        age: 0,
        atomId: options.atomId ?? -1,
        moleculeId: options.moleculeId ?? -1,
        measurement: 'unresolved',
        label: options.label ?? labelForKind(kind),
    })
    return index
}

function seedPacket(packetId: number, center: THREE.Vector3, compact = 1) {
    for (let slot = 0; slot < 24; slot++) {
        const kind = smKindForSlot(slot)
        let offset = randUnitVector().multiplyScalar((18 + Math.random() * 18) * compact)
        if (kind === 'electron') offset = randUnitVector().multiplyScalar((42 + Math.random() * 18) * compact)
        if (kind === 'positron') offset = randUnitVector().multiplyScalar((58 + Math.random() * 18) * compact)
        if (kind === 'photon' || kind === 'gluon' || kind === 'neutrino') offset = randUnitVector().multiplyScalar((72 + Math.random() * 38) * compact)
        pushParticle(kind, packetId, slot, center.clone().add(offset), randUnitVector().multiplyScalar(0.18))
    }
}

function resetSimulation() {
    particles = []
    declaredBonds = []
    nextId = 1
    nextAtomId = 1
    nextMoleculeId = 1
    baselineEnergy = null
    const count = Math.max(24, settings.particleCount)
    const packets = Math.max(1, Math.ceil(count / 24))
    for (let packet = 0; packet < packets; packet++) {
        const center = activePreset.value === 'oneAtom'
            ? new THREE.Vector3()
            : randUnitVector().multiplyScalar(Math.random() * WORLD_RADIUS * 0.62)
        seedPacket(packet + 1, center, activePreset.value === 'oneAtom' ? 0.52 : activePreset.value === 'cloud' ? 1.35 : 1)
    }
    particles = particles.slice(0, count)
    baselineCharge = totalCharge()
}

function clearSimulation() {
    particles = []
    declaredBonds = []
    baselineEnergy = null
    baselineCharge = 0
    metrics.particles = 0
    metrics.nuclei = 0
    metrics.protons = 0
    metrics.neutrons = 0
    metrics.atoms = 0
    metrics.molecules = 0
    metrics.photons = 0
    metrics.electrons = 0
    metrics.muons = 0
    metrics.netCharge = 0
    metrics.kinetic = 0
    metrics.native = 0
    metrics.coulomb = 0
    metrics.string = 0
    metrics.pauli = 0
    metrics.orbital = 0
    metrics.radiated = 0
    metrics.drift = 0
    metrics.colorClosure = 0
    metrics.closureCost = 0
    metrics.measurementHits = 0
}

function totalCharge() {
    return particles.reduce((sum, p) => sum + p.charge, 0)
}

function spawnManual(kind: SmKind, center = spawnSite(32)) {
    pushParticle(kind, nextId + 1000, 12, center.clone().add(randUnitVector().multiplyScalar(8)), randUnitVector().multiplyScalar(0.22))
}

function spawnManualNucleon(kind: NucleonKind) {
    const packetId = nextId + 2000
    const center = randUnitVector().multiplyScalar(28)
    const slots = kind === 'proton' ? [0, 1, 5] : [2, 3, 4]
    for (const slot of slots) {
        pushParticle(smKindForSlot(slot), packetId, slot, center.clone().add(randUnitVector().multiplyScalar(9)), randUnitVector().multiplyScalar(0.12))
    }
}

function spawnConservedPair(kind: SmKind, partner: SmKind, center: THREE.Vector3) {
    if (!canAddParticles(2)) return
    const angle = Math.random() * TAU
    const a = offsetPoint(center, 10, angle, 0.02)
    const b = offsetPoint(center, 10, angle + Math.PI, -0.02)
    const v = randUnitVector().multiplyScalar(0.18)
    pushParticle(kind, nextId + 3100, 12, a, v.clone())
    pushParticle(partner, nextId + 3101, 13, b, v.clone().multiplyScalar(-1))
}

function spawnNucleonAt(kind: NucleonKind, center: THREE.Vector3, atomId = -1, moleculeId = -1) {
    if (!canAddParticles(3)) return []
    const packetId = nextId + 4200
    const slots = kind === 'proton' ? [0, 1, 5] : [2, 3, 4]
    const indices: number[] = []
    for (let i = 0; i < slots.length; i++) {
        const slot = slots[i]
        const angle = TAU * i / slots.length
        const index = pushParticle(
            smKindForSlot(slot),
            packetId,
            slot,
            center.clone().add(new THREE.Vector3(Math.cos(angle) * 7.5, Math.sin(angle) * 7.5, (i - 1) * 3.4)),
            randUnitVector().multiplyScalar(0.06),
            { atomId, moleculeId },
        )
        if (index >= 0) indices.push(index)
    }
    return indices
}

function spawnBoundElectron(center: THREE.Vector3, atomId: number, moleculeId: number, shellRadius: number, ordinal: number) {
    const angle = TAU * ((ordinal * 0.61803398875) % 1)
    const z = (ordinal % 2 === 0 ? 1 : -1) * 0.12
    const position = offsetPoint(center, shellRadius, angle, z)
    const tangent = new THREE.Vector3(-Math.sin(angle), Math.cos(angle), 0.18 * (ordinal % 2 === 0 ? 1 : -1)).normalize()
    return pushParticle('electron', nextId + 5200, 12, position, tangent.multiplyScalar(0.26), {
        atomId,
        moleculeId,
        spin: ordinal % 2 === 0 ? 0.5 : -0.5,
        label: 'e- cloud',
    })
}

function spawnStructuredAtom(kind: 'hydrogen' | 'deuterium' | 'helium4' | 'oxygen16', center: THREE.Vector3, moleculeId = -1) {
    const atomId = nextAtomId++
    const spec = kind === 'hydrogen'
        ? { protons: 1, neutrons: 0, electrons: 1, shell: 38 }
        : kind === 'deuterium'
            ? { protons: 1, neutrons: 1, electrons: 1, shell: 40 }
            : kind === 'helium4'
                ? { protons: 2, neutrons: 2, electrons: 2, shell: 44 }
                : { protons: 8, neutrons: 8, electrons: 8, shell: 58 }

    const nucleonCount = spec.protons + spec.neutrons
    for (let i = 0; i < nucleonCount; i++) {
        const angle = TAU * i / Math.max(1, nucleonCount)
        const radius = nucleonCount === 1 ? 0 : 8 + Math.sqrt(nucleonCount) * 2.2
        const site = center.clone().add(new THREE.Vector3(Math.cos(angle) * radius, Math.sin(angle) * radius, (i % 3 - 1) * 4))
        spawnNucleonAt(i < spec.protons ? 'proton' : 'neutron', site, atomId, moleculeId)
    }
    for (let i = 0; i < spec.electrons; i++) spawnBoundElectron(center, atomId, moleculeId, spec.shell * (1 + Math.floor(i / 2) * 0.16), i)
    return { atomId, center: center.clone() }
}

function spawnHydrogenMolecule(center: THREE.Vector3) {
    const moleculeId = nextMoleculeId++
    const halfBond = 42
    const left = spawnStructuredAtom('hydrogen', center.clone().add(new THREE.Vector3(-halfBond, 0, 0)), moleculeId)
    const right = spawnStructuredAtom('hydrogen', center.clone().add(new THREE.Vector3(halfBond, 0, 0)), moleculeId)
    declaredBonds.push({ moleculeId, atomA: left.atomId, atomB: right.atomId, a: left.center, b: right.center, kind: 'covalent', restLength: halfBond * 2 })
}

function spawnWaterMolecule(center: THREE.Vector3, orientation = Math.random() * TAU) {
    const moleculeId = nextMoleculeId++
    const oxygen = spawnStructuredAtom('oxygen16', center, moleculeId)
    const bondLength = 76
    const bend = 104.5 * Math.PI / 180
    const leftAngle = orientation - bend / 2
    const rightAngle = orientation + bend / 2
    const left = spawnStructuredAtom('hydrogen', center.clone().add(new THREE.Vector3(Math.cos(leftAngle) * bondLength, Math.sin(leftAngle) * bondLength, 8)), moleculeId)
    const right = spawnStructuredAtom('hydrogen', center.clone().add(new THREE.Vector3(Math.cos(rightAngle) * bondLength, Math.sin(rightAngle) * bondLength, -8)), moleculeId)
    declaredBonds.push({ moleculeId, atomA: oxygen.atomId, atomB: left.atomId, a: oxygen.center, b: left.center, kind: 'covalent', restLength: bondLength })
    declaredBonds.push({ moleculeId, atomA: oxygen.atomId, atomB: right.atomId, a: oxygen.center, b: right.center, kind: 'covalent', restLength: bondLength })
}

function spawnWaterCluster(center: THREE.Vector3) {
    for (let i = 0; i < 6; i++) {
        const angle = TAU * i / 6
        const site = center.clone().add(new THREE.Vector3(Math.cos(angle) * 118, Math.sin(angle) * 118, Math.sin(angle * 2) * 26))
        spawnWaterMolecule(site, angle + Math.PI * 0.5)
    }
}

function addEntity(kind: SpawnKind) {
    const site = spawnSite(42)
    if (kind === 'electron') spawnManual('electron', site)
    if (kind === 'electronPair') spawnConservedPair('electron', 'positron', site)
    if (kind === 'muonPair') spawnConservedPair('muon', 'antimuon', site)
    if (kind === 'neutrinoPair') spawnConservedPair('neutrino', 'antineutrino', site)
    if (kind === 'photon') spawnManual('photon', site)
    if (kind === 'proton') spawnNucleonAt('proton', site)
    if (kind === 'neutron') spawnNucleonAt('neutron', site)
    if (kind === 'hydrogen') spawnStructuredAtom('hydrogen', site)
    if (kind === 'deuterium') spawnStructuredAtom('deuterium', site)
    if (kind === 'helium4') spawnStructuredAtom('helium4', site)
    if (kind === 'h2') spawnHydrogenMolecule(site)
    if (kind === 'water') spawnWaterMolecule(site)
    if (kind === 'waterCluster') spawnWaterCluster(site)
}

function addEnergyPulse() {
    let total = new THREE.Vector3()
    let touched = 0
    for (const p of particles) {
        const distance = p.position.length()
        if (distance > WORLD_RADIUS * 0.82 && touched > 36) continue
        const direction = p.position.lengthSq() > 0.01 ? p.position.clone().normalize() : randUnitVector()
        const twist = new THREE.Vector3(-direction.z, direction.x, direction.y).normalize()
        const impulse = direction.add(twist.multiplyScalar(0.55)).normalize().multiplyScalar(0.75 / Math.sqrt(p.mass))
        p.velocity.add(impulse)
        p.J = Math.min(1, p.J + 0.06)
        p.coherence = Math.max(0, p.coherence - 0.02)
        total.add(impulse.multiplyScalar(p.mass))
        touched += 1
    }
    if (touched > 0) {
        total.multiplyScalar(1 / touched)
        for (const p of particles) p.velocity.addScaledVector(total, -1 / Math.max(0.16, p.mass))
    }
}

function collectNuclei() {
    const groups = new Map<number, number[]>()
    for (let i = 0; i < particles.length; i++) {
        const p = particles[i]
        if (!(p.kind === 'quarkR' || p.kind === 'quarkG' || p.kind === 'quarkB')) continue
        const list = groups.get(p.packetId) ?? []
        list.push(i)
        groups.set(p.packetId, list)
    }

    const nuclei: NucleusCandidate[] = []
    for (const [packetId, indices] of groups.entries()) {
        const bySlot = new Map<number, number>()
        for (const index of indices) bySlot.set(particles[index].slot, index)
        const patterns = [
            { kind: 'proton' as NucleonKind, slots: [0, 1, 5] },
            { kind: 'neutron' as NucleonKind, slots: [2, 3, 4] },
        ]
        for (const pattern of patterns) {
            const triplet = pattern.slots.map(slot => bySlot.get(slot)).filter(index => index !== undefined) as number[]
            if (triplet.length !== 3) continue
            nuclei.push(buildNucleusCandidate(packetId, pattern.kind, triplet))
        }
        if (nuclei.some(item => item.packetId === packetId)) continue
        if (indices.length >= 3) nuclei.push(buildNucleusCandidate(packetId, 'proton', indices.slice(0, 3)))
    }
    return nuclei
}

function buildNucleusCandidate(packetId: number, fallbackKind: NucleonKind, triplet: number[]): NucleusCandidate {
    const charge = triplet.reduce((sum, index) => sum + particles[index].charge, 0)
    const atomIds = triplet.map(index => particles[index].atomId).filter(id => id >= 0)
    const moleculeIds = triplet.map(index => particles[index].moleculeId).filter(id => id >= 0)
    const atomId = atomIds.length > 0 ? atomIds[0] : -1
    const moleculeId = moleculeIds.length > 0 ? moleculeIds[0] : -1
    const center = new THREE.Vector3()
    const velocity = new THREE.Vector3()
    const colors = new Set(triplet.map(index => particles[index].color))
    for (const index of triplet) {
        center.add(particles[index].position)
        velocity.add(particles[index].velocity)
    }
    center.multiplyScalar(1 / triplet.length)
    velocity.multiplyScalar(1 / triplet.length)
    const rgb = colors.has('red') && colors.has('green') && colors.has('blue')
    const stability = rgb ? 0.72 + Math.min(0.24, triplet.reduce((sum, index) => sum + particles[index].coherence, 0) / triplet.length * 0.22) : 0.2
    return {
        packetId,
        kind: Math.abs(charge - 1) < 0.35 ? 'proton' : Math.abs(charge) < 0.35 ? 'neutron' : fallbackKind,
        indices: triplet,
        charge: Math.abs(charge - 1) < 0.35 ? 1 : 0,
        center,
        velocity,
        stability,
        atomId,
        moleculeId,
    }
}

function collectAtoms(nuclei: NucleusCandidate[]) {
    const atoms = new Map<number, AtomAggregate3D>()
    const ensureAtom = (atomId: number, moleculeId: number) => {
        let atom = atoms.get(atomId)
        if (!atom) {
            atom = {
                atomId,
                moleculeId,
                center: new THREE.Vector3(),
                velocity: new THREE.Vector3(),
                protonCount: 0,
                neutronCount: 0,
                stability: 0,
                electronIndices: [],
                nucleusParticleIndices: [],
                allParticleIndices: [],
            }
            atoms.set(atomId, atom)
        } else if (atom.moleculeId < 0 && moleculeId >= 0) {
            atom.moleculeId = moleculeId
        }
        return atom
    }

    for (const nucleus of nuclei) {
        if (nucleus.atomId < 0) continue
        const atom = ensureAtom(nucleus.atomId, nucleus.moleculeId)
        atom.center.add(nucleus.center)
        atom.velocity.add(nucleus.velocity)
        atom.stability += nucleus.stability
        atom.protonCount += nucleus.kind === 'proton' ? 1 : 0
        atom.neutronCount += nucleus.kind === 'neutron' ? 1 : 0
        atom.nucleusParticleIndices.push(...nucleus.indices)
        atom.allParticleIndices.push(...nucleus.indices)
    }

    for (let i = 0; i < particles.length; i++) {
        const p = particles[i]
        if (p.atomId < 0) continue
        const atom = ensureAtom(p.atomId, p.moleculeId)
        if (p.kind === 'electron') atom.electronIndices.push(i)
        if (!atom.allParticleIndices.includes(i)) atom.allParticleIndices.push(i)
    }

    for (const atom of atoms.values()) {
        const nucleonCount = atom.protonCount + atom.neutronCount
        if (nucleonCount > 0) {
            atom.center.multiplyScalar(1 / nucleonCount)
            atom.velocity.multiplyScalar(1 / nucleonCount)
            atom.stability /= nucleonCount
        } else if (atom.electronIndices.length > 0) {
            for (const index of atom.electronIndices) {
                atom.center.add(particles[index].position)
                atom.velocity.add(particles[index].velocity)
            }
            atom.center.multiplyScalar(1 / atom.electronIndices.length)
            atom.velocity.multiplyScalar(1 / atom.electronIndices.length)
            atom.stability = 0.35
        }
    }

    return atoms
}

function colorClosureScore(nuclei: NucleusCandidate[]) {
    if (nuclei.length === 0) return 1
    let closed = 0
    for (const nucleus of nuclei) {
        const colors = new Set(nucleus.indices.map(index => particles[index]?.color).filter(Boolean))
        if (colors.has('red') && colors.has('green') && colors.has('blue')) closed += 1
    }
    return closed / nuclei.length
}

function lensCompatibility(a: ProtoParticle3D, b: ProtoParticle3D) {
    if (a.lens === 0 || b.lens === 0) return 0
    return a.lens === b.lens ? -0.72 : 1
}

function resetForces() {
    for (const p of particles) p.force.set(0, 0, 0)
}

function applyPairForces(ledger: EnergyLedger3D) {
    const nativeGain = settings.nativeMtt ? settings.nativeStrength : 0
    const bridgeGain = settings.energyBridge ? settings.ledgerStrength : 0

    for (let i = 0; i < particles.length; i++) {
        const a = particles[i]
        for (let j = i + 1; j < particles.length; j++) {
            const b = particles[j]
            const delta = b.position.clone().sub(a.position)
            const d2 = delta.lengthSq()
            if (d2 < 0.001 || d2 > 220 * 220) continue
            const distance = Math.sqrt(d2)
            const u = delta.multiplyScalar(1 / distance)

            if (nativeGain > 0) {
                const phaseDelta = b.theta - a.theta
                const sigmaDelta = b.sigma - a.sigma
                const phaseAlign = Math.cos(phaseDelta) * 0.62 + Math.cos(sigmaDelta) * 0.38
                const nilMatch = a.nil >= 0 && b.nil >= 0 ? (a.nil === b.nil ? 0.42 : -0.28) : 0
                const nativeForce = (phaseAlign * 0.012 + lensCompatibility(a, b) * 0.026 + nilMatch * 0.012) * nativeGain / (1 + distance / 72)
                a.force.addScaledVector(u, nativeForce)
                b.force.addScaledVector(u, -nativeForce)
                ledger.native += Math.abs(1 - phaseAlign) * 0.008 + Math.max(0, -nilMatch) * 0.01
            }

            if (bridgeGain > 0 && Math.abs(a.charge * b.charge) > 0.001) {
                const atten = 1 / (1 + distance / (68 * settings.carrierSpread))
                const force = -a.charge * b.charge * atten * atten * 0.045 * bridgeGain
                a.force.addScaledVector(u, force)
                b.force.addScaledVector(u, -force)
                ledger.coulomb += a.charge * b.charge * atten * 0.22
            }

            const sameFermion = a.kind === b.kind && Math.abs(a.charge - b.charge) < 0.001 && a.kind !== 'photon' && a.kind !== 'gluon'
            if (bridgeGain > 0 && sameFermion) {
                const spinOverlap = Math.sign(a.spin) === Math.sign(b.spin) ? 1 : 0.16
                const closeness = Math.max(0, 1 - distance / 28)
                if (closeness > 0) {
                    const pressure = closeness * closeness * spinOverlap * 0.09
                    a.force.addScaledVector(u, -pressure * bridgeGain)
                    b.force.addScaledVector(u, pressure * bridgeGain)
                    ledger.pauli += pressure
                }
            }

            const sameQuarkSource = a.packetId === b.packetId && a.kind.startsWith('quark') && b.kind.startsWith('quark')
            if (bridgeGain > 0 && sameQuarkSource) {
                const target = 13.5
                const spring = (distance - target) / target
                const hardCore = Math.max(0, 1 - distance / 7.5)
                const stringForce = Math.max(-0.08, Math.min(0.085, spring * 0.052 - hardCore * 0.11)) * bridgeGain
                a.force.addScaledVector(u, stringForce)
                b.force.addScaledVector(u, -stringForce)
                ledger.string += 0.06 + Math.abs(spring) * 0.12 + hardCore * 0.2
            }
        }
    }
}

function applyOrbitalForces(ledger: EnergyLedger3D, nuclei: NucleusCandidate[]) {
    if (!settings.energyBridge) return
    const gain = settings.ledgerStrength
    for (const nucleus of nuclei.filter(item => item.kind === 'proton')) {
        for (let i = 0; i < particles.length; i++) {
            const electron = particles[i]
            if (electron.kind !== 'electron') continue
            if (electron.atomId >= 0) continue
            const matchedAtom = electron.atomId >= 0 && nucleus.atomId >= 0 && electron.atomId === nucleus.atomId
            if (electron.atomId >= 0 && nucleus.atomId >= 0 && !matchedAtom) continue
            const delta = electron.position.clone().sub(nucleus.center)
            const distance = Math.max(1, delta.length())
            if (distance > 120 * settings.carrierSpread) continue
            const u = delta.multiplyScalar(1 / distance)
            const shellScale = (matchedAtom ? 42 : 46) * settings.carrierSpread
            const shellTarget = (matchedAtom ? 44 : 52) * settings.carrierSpread
            const pressureScale = 16 + settings.carrierSpread * 8
            const closure = Math.max(0, Math.min(1, electron.coherence * 0.42 + (1 - electron.J) * 0.34 + electron.recurrence * 0.24))
            const alpha = nucleus.stability * 0.42
            const pressureQ = 0.16 + (1 - closure) * 0.08
            const attractionEnergy = -alpha / (1 + distance / shellScale)
            const pressureEnergy = pressureQ / (1 + distance / pressureScale) ** 2
            ledger.orbital += attractionEnergy + pressureEnergy

            const attraction = alpha / shellScale / (1 + distance / shellScale) ** 2
            const pressure = 2 * pressureQ / pressureScale / (1 + distance / pressureScale) ** 3
            const shellSpring = matchedAtom ? -(distance - shellTarget) * 0.0022 : 0
            const radialForce = (pressure - attraction + shellSpring) * gain
            electron.force.addScaledVector(u, radialForce)
            for (const index of nucleus.indices) particles[index].force.addScaledVector(u, -radialForce / nucleus.indices.length)

            const relative = electron.velocity.clone().sub(nucleus.velocity)
            const radialVelocity = relative.dot(u)
            const damp = Math.min(0.006, Math.abs(radialVelocity) * 0.0015 * closure * gain)
            electron.velocity.addScaledVector(u, -radialVelocity * damp)
            if (matchedAtom) {
                const tangent = new THREE.Vector3(-u.y, u.x, u.z * 0.22).normalize()
                const desiredFlow = 0.36 * Math.sqrt(Math.max(0.1, nucleus.stability))
                const tangentVelocity = relative.dot(tangent)
                electron.velocity.addScaledVector(tangent, (desiredFlow - tangentVelocity) * 0.012 * gain)
            }
            if (distance < shellScale * 1.5 && Math.abs(radialVelocity) > 0.2) {
                ledger.radiated += Math.abs(radialVelocity) * damp * 0.18
            }
        }
    }
}

function distributeForce(indices: number[], force: THREE.Vector3, scale = 1) {
    if (indices.length === 0) return
    const share = scale / indices.length
    for (const index of indices) particles[index]?.force.addScaledVector(force, share)
}

function applyAtomShellForces(ledger: EnergyLedger3D, atoms: Map<number, AtomAggregate3D>) {
    if (!settings.energyBridge) return
    const gain = settings.ledgerStrength
    for (const atom of atoms.values()) {
        if (atom.protonCount <= 0 || atom.electronIndices.length === 0) continue
        const baseShell = shellRadiusForAtom(atom)
        for (let ordinal = 0; ordinal < atom.electronIndices.length; ordinal++) {
            const electron = particles[atom.electronIndices[ordinal]]
            const shellTarget = baseShell * (1 + Math.floor(ordinal / 2) * 0.12)
            const delta = electron.position.clone().sub(atom.center)
            const distance = Math.max(1, delta.length())
            if (distance > Math.max(150, shellTarget * 2.6)) continue
            const u = delta.multiplyScalar(1 / distance)
            const closure = clamp01(electron.coherence * 0.48 + (1 - electron.J) * 0.34 + electron.recurrence * 0.18)
            const stretch = distance - shellTarget
            const confinement = Math.max(-0.18, Math.min(0.18, -stretch * 0.0058))
            const corePressure = Math.max(0, 1 - distance / Math.max(8, shellTarget * 0.34)) ** 2 * 0.22
            const radialForce = (confinement + corePressure) * gain * (0.7 + atom.stability * 0.5)

            electron.force.addScaledVector(u, radialForce)
            distributeForce(atom.nucleusParticleIndices, u, -radialForce)

            const relative = electron.velocity.clone().sub(atom.velocity)
            const radialVelocity = relative.dot(u)
            electron.velocity.addScaledVector(u, -radialVelocity * 0.04 * gain * closure)

            const tangent = new THREE.Vector3(-u.y, u.x, 0.32 + u.z * 0.12).normalize()
            const desiredFlow = 0.28 + Math.sqrt(Math.max(1, atom.protonCount)) * 0.032
            const tangentVelocity = relative.dot(tangent)
            electron.velocity.addScaledVector(tangent, (desiredFlow - tangentVelocity) * 0.018 * gain * closure)

            ledger.orbital += -0.18 * atom.protonCount / (1 + distance / Math.max(10, shellTarget)) + Math.abs(stretch) * 0.0022 + corePressure * 0.2
            if (Math.abs(radialVelocity) > 0.16) ledger.radiated += Math.abs(radialVelocity) * 0.0025 * gain
        }
    }
}

function atomEndpoint(atomId: number, fallback: THREE.Vector3, atoms: Map<number, AtomAggregate3D>) {
    return atoms.get(atomId)?.center ?? fallback
}

function applyMoleculeForces(ledger: EnergyLedger3D, atoms: Map<number, AtomAggregate3D>) {
    if (!settings.energyBridge) return
    const gain = settings.ledgerStrength
    for (const bond of declaredBonds) {
        const atomA = atoms.get(bond.atomA)
        const atomB = atoms.get(bond.atomB)
        if (!atomA || !atomB) continue
        const delta = atomB.center.clone().sub(atomA.center)
        const distance = Math.max(1, delta.length())
        const u = delta.multiplyScalar(1 / distance)
        const stretch = distance - bond.restLength
        const spring = Math.max(-0.22, Math.min(0.22, stretch * 0.011)) * gain
        distributeForce(atomA.allParticleIndices, u, spring)
        distributeForce(atomB.allParticleIndices, u, -spring)

        const radialVelocity = atomB.velocity.clone().sub(atomA.velocity).dot(u)
        const damping = Math.max(-0.16, Math.min(0.16, radialVelocity * 0.035)) * gain
        distributeForce(atomA.allParticleIndices, u, damping)
        distributeForce(atomB.allParticleIndices, u, -damping)
        ledger.orbital += Math.abs(stretch) * 0.018 + Math.abs(radialVelocity) * 0.01
    }

    const bondsByMolecule = new Map<number, DeclaredBond3D[]>()
    for (const bond of declaredBonds) {
        const list = bondsByMolecule.get(bond.moleculeId) ?? []
        list.push(bond)
        bondsByMolecule.set(bond.moleculeId, list)
    }

    for (const bonds of bondsByMolecule.values()) {
        for (let i = 0; i < bonds.length; i++) {
            for (let j = i + 1; j < bonds.length; j++) {
                const first = bonds[i]
                const second = bonds[j]
                if (first.atomA !== second.atomA) continue
                const center = atoms.get(first.atomA)
                const left = atoms.get(first.atomB)
                const right = atoms.get(second.atomB)
                if (!center || !left || !right || center.protonCount < 2) continue
                const a = left.center.clone().sub(center.center)
                const b = right.center.clone().sub(center.center)
                const aLen = a.length()
                const bLen = b.length()
                if (aLen < 1 || bLen < 1) continue
                const uA = a.multiplyScalar(1 / aLen)
                const uB = b.multiplyScalar(1 / bLen)
                const dot = Math.max(-1, Math.min(1, uA.dot(uB)))
                const angle = Math.acos(dot)
                const target = center.protonCount >= 8 ? 104.5 * Math.PI / 180 : Math.PI
                const error = angle - target
                const normal = uA.clone().cross(uB)
                if (normal.lengthSq() < 0.0001) continue
                normal.normalize()
                const tangentA = normal.clone().cross(uA).normalize()
                const tangentB = uB.clone().cross(normal).normalize()
                const bend = Math.max(-0.14, Math.min(0.14, error * 0.075)) * gain
                distributeForce(left.allParticleIndices, tangentA, bend)
                distributeForce(right.allParticleIndices, tangentB, bend)
                distributeForce(center.allParticleIndices, tangentA.add(tangentB), -bend * 0.5)
                ledger.orbital += Math.abs(error) * 0.08
            }
        }
    }
}

function applyNucleusCohesion(nuclei: NucleusCandidate[], ledger: EnergyLedger3D) {
    if (!settings.energyBridge) return
    const gain = settings.ledgerStrength
    for (const nucleus of nuclei) {
        const target = nucleus.kind === 'proton' ? 8.2 : 8.8
        for (const index of nucleus.indices) {
            const p = particles[index]
            const delta = p.position.clone().sub(nucleus.center)
            const distance = Math.max(0.001, delta.length())
            const u = delta.multiplyScalar(1 / distance)
            const stretch = (distance - target) / target
            const hardCore = Math.max(0, 1 - distance / 4.8)
            const force = Math.max(-0.18, Math.min(0.18, -stretch * 0.105 + hardCore * 0.16)) * gain * nucleus.stability
            p.force.addScaledVector(u, force)
            const radialVelocity = p.velocity.clone().sub(nucleus.velocity).dot(u)
            p.velocity.addScaledVector(u, -radialVelocity * 0.018 * gain)
            ledger.string += Math.abs(stretch) * 0.035 + hardCore * 0.08
        }
    }
}

function applyMeasurementForces(ledger: EnergyLedger3D) {
    measurementHitsThisFrame = 0
    if (!lookingGlassEnabled.value || settings.measurementStrength <= 0 || (!lookingGlass.active && frame > lookingGlass.pulseUntil)) return
    const center = lookingGlass.center
    const radius = Math.max(1, settings.measurementRadius)
    const gain = settings.measurementStrength
    const splitOffset = radius * 0.48
    for (const p of particles) {
        let localCenter = center
        if (measurementKind.value === 'split') {
            const left = center.clone().add(new THREE.Vector3(-splitOffset, 0, 0))
            const right = center.clone().add(new THREE.Vector3(splitOffset, 0, 0))
            localCenter = p.position.distanceTo(left) <= p.position.distanceTo(right) ? left : right
        }
        const delta = p.position.clone().sub(localCenter)
        const distance = delta.length()
        if (distance > radius) {
            p.measurement = 'unresolved'
            continue
        }
        measurementHitsThisFrame += 1
        const u = distance > 0.001 ? delta.multiplyScalar(1 / distance) : randUnitVector()
        const focus = (1 - distance / radius) * gain
        p.measurement = measurementKind.value === 'split' ? 'split' : 'focused'

        if (measurementKind.value === 'projector') {
            p.coherence = clamp01(p.coherence + focus * 0.055)
            p.J = clamp01(p.J - focus * 0.036)
            p.force.addScaledVector(u, -focus * 0.018)
            ledger.native -= focus * 0.012
        } else if (measurementKind.value === 'interference') {
            p.recurrence = clamp01(p.recurrence + focus * 0.05)
            p.theta = (p.theta + Math.sin(p.sigma - p.theta) * focus * 0.018 + TAU) % TAU
            ledger.native -= focus * 0.006
        } else if (measurementKind.value === 'whichPath') {
            p.coherence = clamp01(p.coherence - focus * 0.07)
            p.J = clamp01(p.J + focus * 0.045)
            p.force.addScaledVector(u, focus * 0.024)
            ledger.native += focus * 0.018
        } else {
            p.coherence = clamp01(p.coherence - focus * 0.035)
            p.force.addScaledVector(u, focus * 0.012)
            ledger.native += focus * 0.008
        }
    }
}

function integrate() {
    const dt = settings.timeScale
    for (const p of particles) {
        p.age += 1
        p.theta = (p.theta + (0.007 + p.lens * 0.0015) * dt) % TAU
        p.sigma = (p.sigma + (0.004 + p.nil * 0.0007) * dt) % TAU
        p.velocity.addScaledVector(p.force, dt / Math.max(0.16, p.mass))
        p.velocity.multiplyScalar(p.kind === 'photon' ? 0.995 : 0.982)
        const speed = p.velocity.length()
        const maxSpeed = p.kind === 'photon' ? 3.2 : 2.35
        if (speed > maxSpeed) p.velocity.multiplyScalar(maxSpeed / speed)
        p.position.addScaledVector(p.velocity, dt)
        const radius = p.position.length()
        if (radius > WORLD_RADIUS) {
            p.position.multiplyScalar(WORLD_RADIUS / radius)
            p.velocity.reflect(p.position.clone().normalize()).multiplyScalar(0.62)
        }
        const closure = Math.max(0, 1 - p.force.length() * 0.22)
        p.coherence += (closure - p.coherence) * 0.01
        p.recurrence = Math.min(1, p.recurrence + (p.coherence - p.J) * 0.0015)
        p.J = Math.max(0, Math.min(1, p.J + p.force.length() * 0.003 - p.coherence * 0.001))
    }
}

function simulateFrame() {
    const ledger: EnergyLedger3D = { kinetic: 0, native: 0, coulomb: 0, string: 0, pauli: 0, orbital: 0, photon: 0, radiated: 0, total: 0 }
    resetForces()
    applyPairForces(ledger)
    const nuclei = collectNuclei()
    const atoms = collectAtoms(nuclei)
    applyNucleusCohesion(nuclei, ledger)
    applyAtomShellForces(ledger, atoms)
    applyMoleculeForces(ledger, atoms)
    applyOrbitalForces(ledger, nuclei)
    applyMeasurementForces(ledger)
    integrate()

    let atomCount = 0
    let photons = 0
    let electrons = 0
    let muons = 0
    let netCharge = 0
    let closureCost = 0
    for (const p of particles) {
        ledger.kinetic += 0.5 * p.mass * p.velocity.lengthSq()
        ledger.photon += p.kind === 'photon' ? p.coherence * 0.18 + p.velocity.length() * 0.06 : 0
        photons += p.kind === 'photon' ? 1 : 0
        electrons += p.kind === 'electron' ? 1 : 0
        muons += p.kind === 'muon' || p.kind === 'antimuon' ? 1 : 0
        netCharge += p.charge
        closureCost += Math.abs(1 - p.coherence) * 0.44 + p.J * 0.38 + Math.abs(0.22 - p.recurrence) * 0.18
    }
    for (const atom of atoms.values()) {
        if (atom.protonCount > 0 && atom.electronIndices.length > 0) {
            atomCount += 1
        }
    }
    for (const nucleus of nuclei.filter(item => item.kind === 'proton' && item.atomId < 0)) {
        const nearest = particles.some(p => p.kind === 'electron' && p.position.distanceTo(nucleus.center) < 58 * settings.carrierSpread)
        if (nearest) atomCount += 1
    }
    ledger.total = ledger.kinetic + ledger.native + ledger.coulomb + ledger.string + ledger.pauli + ledger.orbital + ledger.photon
    if (baselineEnergy === null) baselineEnergy = ledger.total
    const protons = nuclei.filter(item => item.kind === 'proton').length
    const neutrons = nuclei.filter(item => item.kind === 'neutron').length
    const moleculeIds = new Set(particles.filter(p => p.moleculeId >= 0).map(p => p.moleculeId))
    metrics.particles = particles.length
    metrics.nuclei = nuclei.length
    metrics.protons = protons
    metrics.neutrons = neutrons
    metrics.atoms = atomCount
    metrics.molecules = moleculeIds.size
    metrics.photons = photons
    metrics.electrons = electrons
    metrics.muons = muons
    metrics.netCharge = netCharge
    metrics.kinetic = ledger.kinetic
    metrics.native = ledger.native
    metrics.coulomb = ledger.coulomb
    metrics.string = ledger.string
    metrics.pauli = ledger.pauli
    metrics.orbital = ledger.orbital
    metrics.radiated += ledger.radiated
    metrics.drift = ledger.total - baselineEnergy
    metrics.colorClosure = colorClosureScore(nuclei)
    metrics.closureCost = particles.length > 0 ? closureCost / particles.length : 0
    metrics.measurementHits = measurementHitsThisFrame
}

function updateMeshes() {
    if (!particleMesh || !particlePoints || !pointGeometry || !pointPositions || !pointColors || !nucleusMesh || !atomShellMesh || !photonMesh || !linkGeometry || !linkPositions || !linkColors || !bondGeometry || !bondPositions) return
    let photonCount = 0
    let carrierCursor = 0
    for (let i = 0; i < particles.length && carrierCursor < MAX_PARTICLES; i++) {
        const p = particles[i]
        const renderCarrier = shouldRenderCarrier(p)
        const pulse = p.kind === 'photon' ? 1 + Math.sin(frame * 0.08 + p.theta) * 0.16 : 1
        const measurementPulse = p.measurement === 'focused' || p.measurement === 'split' ? 1.42 : 1
        const color = particleColor(p)
        if (renderCarrier) {
            tempScale.setScalar(p.radius * pulse * 1.22)
            tempScale.multiplyScalar(measurementPulse)
            tempMatrix.compose(p.position, tempQuaternion, tempScale)
            particleMesh.setMatrixAt(carrierCursor, tempMatrix)
            particleMesh.setColorAt(carrierCursor, color)
            pointPositions[carrierCursor * 3] = p.position.x
            pointPositions[carrierCursor * 3 + 1] = p.position.y
            pointPositions[carrierCursor * 3 + 2] = p.position.z
            pointColors[carrierCursor * 3] = color.r
            pointColors[carrierCursor * 3 + 1] = color.g
            pointColors[carrierCursor * 3 + 2] = color.b
            carrierCursor += 1
        }
        if (p.kind === 'photon' && photonCount < 240) {
            tempQuaternion.setFromAxisAngle(axisY, p.theta)
            tempScale.setScalar(3.2 + p.coherence * 4.5)
            tempMatrix.compose(p.position, tempQuaternion, tempScale)
            photonMesh.setMatrixAt(photonCount, tempMatrix)
            photonMesh.setColorAt(photonCount, tempColor.setRGB(1, 0.86, 0.28))
            photonCount += 1
        }
    }
    particleMesh.count = carrierCursor
    particleMesh.visible = showParticles.value
    particleMesh.instanceMatrix.needsUpdate = true
    if (particleMesh.instanceColor) particleMesh.instanceColor.needsUpdate = true
    particlePoints.visible = showCores.value
    pointGeometry.setDrawRange(0, carrierCursor)
    pointGeometry.attributes.position.needsUpdate = true
    pointGeometry.attributes.color.needsUpdate = true
    photonMesh.count = photonCount
    photonMesh.visible = showPhotons.value
    photonMesh.instanceMatrix.needsUpdate = true
    if (photonMesh.instanceColor) photonMesh.instanceColor.needsUpdate = true
    if (carrierGroup) carrierGroup.visible = showCarrierRings.value

    let linkCursor = 0
    const nuclei = collectNuclei()
    const atoms = collectAtoms(nuclei)
    let nucleusCursor = 0
    for (const nucleus of nuclei) {
        if (nucleusCursor >= MAX_NUCLEI) break
        const size = (nucleus.kind === 'proton' ? 7.6 : 7.0) * (0.78 + nucleus.stability * 0.34)
        tempScale.setScalar(size)
        tempMatrix.compose(nucleus.center, tempQuaternion, tempScale)
        nucleusMesh.setMatrixAt(nucleusCursor, tempMatrix)
        nucleusMesh.setColorAt(nucleusCursor, nucleusColor(nucleus))
        nucleusCursor += 1
    }
    nucleusMesh.count = nucleusCursor
    nucleusMesh.visible = showNuclei.value
    nucleusMesh.instanceMatrix.needsUpdate = true
    if (nucleusMesh.instanceColor) nucleusMesh.instanceColor.needsUpdate = true

    let atomCursor = 0
    for (const atom of atoms.values()) {
        if (atomCursor >= MAX_ATOMS || atom.protonCount <= 0) continue
        const size = visualRadiusForAtom(atom)
        tempScale.setScalar(size)
        tempMatrix.compose(atom.center, tempQuaternion, tempScale)
        atomShellMesh.setMatrixAt(atomCursor, tempMatrix)
        atomShellMesh.setColorAt(atomCursor, atomColor(atom))
        atomCursor += 1
    }
    atomShellMesh.count = atomCursor
    atomShellMesh.visible = showAtomShells.value
    atomShellMesh.instanceMatrix.needsUpdate = true
    if (atomShellMesh.instanceColor) atomShellMesh.instanceColor.needsUpdate = true

    for (const nucleus of nuclei) {
        for (const index of nucleus.indices) {
            if (linkCursor >= MAX_LINKS) break
            const p = particles[index]
            linkPositions[linkCursor * 6] = nucleus.center.x
            linkPositions[linkCursor * 6 + 1] = nucleus.center.y
            linkPositions[linkCursor * 6 + 2] = nucleus.center.z
            linkPositions[linkCursor * 6 + 3] = p.position.x
            linkPositions[linkCursor * 6 + 4] = p.position.y
            linkPositions[linkCursor * 6 + 5] = p.position.z
            const color = particleColor(p)
            linkColors[linkCursor * 6] = color.r * 0.75
            linkColors[linkCursor * 6 + 1] = color.g * 0.75
            linkColors[linkCursor * 6 + 2] = color.b * 0.75
            linkColors[linkCursor * 6 + 3] = color.r
            linkColors[linkCursor * 6 + 4] = color.g
            linkColors[linkCursor * 6 + 5] = color.b
            linkCursor += 1
        }
    }
    linkGeometry.setDrawRange(0, linkCursor * 2)
    linkGeometry.attributes.position.needsUpdate = true
    linkGeometry.attributes.color.needsUpdate = true
    if (linkLines) linkLines.visible = showInternalCarriers.value || showQuarkBinding.value

    let bondCursor = 0
    for (const bond of declaredBonds) {
        if (bondCursor >= MAX_BONDS) break
        const a = atomEndpoint(bond.atomA, bond.a, atoms)
        const b = atomEndpoint(bond.atomB, bond.b, atoms)
        bondPositions[bondCursor * 6] = a.x
        bondPositions[bondCursor * 6 + 1] = a.y
        bondPositions[bondCursor * 6 + 2] = a.z
        bondPositions[bondCursor * 6 + 3] = b.x
        bondPositions[bondCursor * 6 + 4] = b.y
        bondPositions[bondCursor * 6 + 5] = b.z
        bondCursor += 1
    }
    bondGeometry.setDrawRange(0, bondCursor * 2)
    bondGeometry.attributes.position.needsUpdate = true
    if (bondLines) bondLines.visible = showMolecularBonds.value && bondCursor > 0

    updateMeasurementMeshes()
}

function updateMeasurementMeshes() {
    if (!measurementMesh || !measurementSplitA || !measurementSplitB) return
    const active = lookingGlassEnabled.value && showLookingGlass.value && (lookingGlass.active || frame <= lookingGlass.pulseUntil)
    const radius = settings.measurementRadius
    measurementMesh.visible = active && measurementKind.value !== 'split'
    measurementSplitA.visible = active && measurementKind.value === 'split'
    measurementSplitB.visible = active && measurementKind.value === 'split'
    measurementMesh.position.copy(lookingGlass.center)
    measurementMesh.scale.setScalar(radius)
    const splitOffset = radius * 0.48
    measurementSplitA.position.copy(lookingGlass.center).add(new THREE.Vector3(-splitOffset, 0, 0))
    measurementSplitB.position.copy(lookingGlass.center).add(new THREE.Vector3(splitOffset, 0, 0))
    measurementSplitA.scale.setScalar(radius * 0.72)
    measurementSplitB.scale.setScalar(radius * 0.72)
}

function animate() {
    animationId = requestAnimationFrame(animate)
    frame += 1
    if (isRunning.value) simulateFrame()
    updateMeshes()
    controls?.update()
    renderer?.render(scene!, camera!)
}

function createPointTexture() {
    const canvas = document.createElement('canvas')
    canvas.width = 64
    canvas.height = 64
    const context = canvas.getContext('2d')
    if (!context) return null
    const gradient = context.createRadialGradient(32, 32, 0, 32, 32, 32)
    gradient.addColorStop(0, 'rgba(255, 255, 255, 1)')
    gradient.addColorStop(0.42, 'rgba(255, 255, 255, 0.86)')
    gradient.addColorStop(1, 'rgba(255, 255, 255, 0)')
    context.fillStyle = gradient
    context.fillRect(0, 0, 64, 64)
    const texture = new THREE.CanvasTexture(canvas)
    texture.colorSpace = THREE.SRGBColorSpace
    return texture
}

function addWhiteVertexColors(geometry: THREE.BufferGeometry) {
    const position = geometry.getAttribute('position')
    const colors = new Float32Array(position.count * 3)
    colors.fill(1)
    geometry.setAttribute('color', new THREE.BufferAttribute(colors, 3))
    return geometry
}

function initThree() {
    if (!canvasRef.value || !shellRef.value) return
    scene = new THREE.Scene()
    scene.background = new THREE.Color(0x061019)
    scene.fog = new THREE.FogExp2(0x061019, 0.0018)
    camera = new THREE.PerspectiveCamera(56, shellRef.value.clientWidth / shellRef.value.clientHeight, 0.1, 1200)
    camera.position.set(0, 72, 320)

    renderer = new THREE.WebGLRenderer({ canvas: canvasRef.value, antialias: true })
    renderer.setPixelRatio(Math.min(window.devicePixelRatio, 2))
    renderer.setSize(shellRef.value.clientWidth, shellRef.value.clientHeight)
    renderer.toneMapping = THREE.ACESFilmicToneMapping
    renderer.toneMappingExposure = 1.35

    controls = new OrbitControls(camera, renderer.domElement)
    controls.enableDamping = true
    controls.dampingFactor = 0.06
    controls.minDistance = 90
    controls.maxDistance = 520

    scene.add(new THREE.AmbientLight(0xb8d7ff, 1.35))
    const key = new THREE.PointLight(0x9fffe0, 3.6, 560)
    key.position.set(120, 160, 120)
    scene.add(key)
    const fill = new THREE.PointLight(0xffd38a, 2.1, 460)
    fill.position.set(-160, -80, -120)
    scene.add(fill)

    const sphere = addWhiteVertexColors(new THREE.SphereGeometry(1, 18, 12))
    const material = new THREE.MeshBasicMaterial({
        color: 0xffffff,
        vertexColors: true,
        transparent: true,
        opacity: 0.52,
        depthWrite: false,
    })
    particleMesh = new THREE.InstancedMesh(sphere, material, 900)
    particleMesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage)
    scene.add(particleMesh)

    pointPositions = new Float32Array(900 * 3)
    pointColors = new Float32Array(900 * 3)
    pointGeometry = new THREE.BufferGeometry()
    const positionAttribute = new THREE.BufferAttribute(pointPositions, 3)
    const colorAttribute = new THREE.BufferAttribute(pointColors, 3)
    positionAttribute.setUsage(THREE.DynamicDrawUsage)
    colorAttribute.setUsage(THREE.DynamicDrawUsage)
    pointGeometry.setAttribute('position', positionAttribute)
    pointGeometry.setAttribute('color', colorAttribute)
    pointGeometry.setDrawRange(0, 0)
    const pointMaterial = new THREE.PointsMaterial({
        color: 0xffffff,
        size: 9.4,
        sizeAttenuation: true,
        map: createPointTexture(),
        vertexColors: true,
        transparent: true,
        opacity: 0.96,
        depthTest: false,
        depthWrite: false,
        blending: THREE.AdditiveBlending,
    })
    particlePoints = new THREE.Points(pointGeometry, pointMaterial)
    scene.add(particlePoints)

    const nucleusGeometry = addWhiteVertexColors(new THREE.SphereGeometry(1, 24, 16))
    const nucleusMaterial = new THREE.MeshBasicMaterial({
        color: 0xffffff,
        vertexColors: true,
        transparent: true,
        opacity: 0.86,
        depthWrite: false,
    })
    nucleusMesh = new THREE.InstancedMesh(nucleusGeometry, nucleusMaterial, MAX_NUCLEI)
    nucleusMesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage)
    scene.add(nucleusMesh)

    const atomShellGeometry = addWhiteVertexColors(new THREE.SphereGeometry(1, 32, 18))
    const atomShellMaterial = new THREE.MeshBasicMaterial({
        color: 0xffffff,
        vertexColors: true,
        transparent: true,
        opacity: 0.14,
        wireframe: true,
        blending: THREE.AdditiveBlending,
        depthWrite: false,
    })
    atomShellMesh = new THREE.InstancedMesh(atomShellGeometry, atomShellMaterial, MAX_ATOMS)
    atomShellMesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage)
    scene.add(atomShellMesh)

    const torus = addWhiteVertexColors(new THREE.TorusGeometry(1, 0.02, 8, 36))
    const waveMaterial = new THREE.MeshBasicMaterial({ transparent: true, opacity: 0.78, vertexColors: true, blending: THREE.AdditiveBlending })
    photonMesh = new THREE.InstancedMesh(torus, waveMaterial, 240)
    photonMesh.instanceMatrix.setUsage(THREE.DynamicDrawUsage)
    scene.add(photonMesh)

    linkPositions = new Float32Array(MAX_LINKS * 2 * 3)
    linkColors = new Float32Array(MAX_LINKS * 2 * 3)
    linkGeometry = new THREE.BufferGeometry()
    const linkPositionAttribute = new THREE.BufferAttribute(linkPositions, 3)
    const linkColorAttribute = new THREE.BufferAttribute(linkColors, 3)
    linkPositionAttribute.setUsage(THREE.DynamicDrawUsage)
    linkColorAttribute.setUsage(THREE.DynamicDrawUsage)
    linkGeometry.setAttribute('position', linkPositionAttribute)
    linkGeometry.setAttribute('color', linkColorAttribute)
    linkGeometry.setDrawRange(0, 0)
    const linkMaterial = new THREE.LineBasicMaterial({ vertexColors: true, transparent: true, opacity: 0.78, blending: THREE.AdditiveBlending })
    linkLines = new THREE.LineSegments(linkGeometry, linkMaterial)
    scene.add(linkLines)

    bondPositions = new Float32Array(MAX_BONDS * 2 * 3)
    bondGeometry = new THREE.BufferGeometry()
    bondGeometry.setAttribute('position', new THREE.BufferAttribute(bondPositions, 3))
    bondGeometry.setDrawRange(0, 0)
    const bondMaterial = new THREE.LineBasicMaterial({ color: 0xfde68a, transparent: true, opacity: 0.82, blending: THREE.AdditiveBlending })
    bondLines = new THREE.LineSegments(bondGeometry, bondMaterial)
    scene.add(bondLines)

    carrierGroup = new THREE.Group()
    for (const radius of [46, 92, 138]) {
        const ring = new THREE.Mesh(
            new THREE.TorusGeometry(radius, 0.08, 8, 160),
            new THREE.MeshBasicMaterial({ color: 0x3ff5c4, transparent: true, opacity: 0.16, blending: THREE.AdditiveBlending }),
        )
        ring.rotation.x = Math.PI / 2
        carrierGroup.add(ring)
    }
    scene.add(carrierGroup)

    const measurementMaterial = new THREE.MeshBasicMaterial({ color: 0xfef3c7, transparent: true, opacity: 0.12, wireframe: true, blending: THREE.AdditiveBlending })
    measurementMesh = new THREE.Mesh(new THREE.SphereGeometry(1, 28, 16), measurementMaterial)
    measurementSplitA = new THREE.Mesh(new THREE.SphereGeometry(1, 28, 16), measurementMaterial.clone())
    measurementSplitB = new THREE.Mesh(new THREE.SphereGeometry(1, 28, 16), measurementMaterial.clone())
    measurementMesh.visible = false
    measurementSplitA.visible = false
    measurementSplitB.visible = false
    scene.add(measurementMesh)
    scene.add(measurementSplitA)
    scene.add(measurementSplitB)
}

function resize() {
    if (!renderer || !camera || !shellRef.value) return
    const width = shellRef.value.clientWidth
    const height = shellRef.value.clientHeight
    camera.aspect = width / height
    camera.updateProjectionMatrix()
    renderer.setSize(width, height)
}

function worldPointFromPointer(event: PointerEvent) {
    if (!camera || !canvasRef.value) return null
    const rect = canvasRef.value.getBoundingClientRect()
    pointerNdc.x = ((event.clientX - rect.left) / rect.width) * 2 - 1
    pointerNdc.y = -(((event.clientY - rect.top) / rect.height) * 2 - 1)
    raycaster.setFromCamera(pointerNdc, camera)
    const hit = raycaster.ray.intersectPlane(measurePlane, tempPoint)
    if (!hit) return null
    if (tempPoint.length() > WORLD_RADIUS) tempPoint.setLength(WORLD_RADIUS * 0.92)
    return tempPoint.clone()
}

function pulseLookingGlass(point: THREE.Vector3, hold = false) {
    lookingGlass.center.copy(point)
    lookingGlass.active = hold
    lookingGlass.pulseUntil = frame + 42
}

function onPointerDown(event: PointerEvent) {
    const point = worldPointFromPointer(event)
    if (!point) return
    pulseLookingGlass(point, true)
}

function onPointerMove(event: PointerEvent) {
    if (!lookingGlass.active) return
    const point = worldPointFromPointer(event)
    if (point) pulseLookingGlass(point, true)
}

function onPointerUp() {
    lookingGlass.active = false
}

onMounted(() => {
    initThree()
    resetSimulation()
    window.addEventListener('resize', resize)
    animate()
})

onBeforeUnmount(() => {
    cancelAnimationFrame(animationId)
    window.removeEventListener('resize', resize)
    controls?.dispose()
    renderer?.dispose()
})
</script>

<style scoped lang="scss">
.proto3d-shell {
    position: relative;
    min-height: 100vh;
    overflow: hidden;
    background: #05080d;
    color: #e5fdf7;
}

.proto3d-canvas {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    display: block;
}

.topbar {
    position: absolute;
    z-index: 10;
    top: 0;
    left: 0;
    right: 0;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
    padding: 0.8rem 1rem;
    background: linear-gradient(180deg, rgba(5, 8, 13, 0.86), rgba(5, 8, 13, 0.28));
}

.home-link,
.title-row,
.top-actions,
.metric {
    display: flex;
    align-items: center;
}

.home-link {
    gap: 0.35rem;
    color: #c9fff0;
}

.title-wrap {
    flex: 1;
    min-width: 0;
}

.title-row {
    gap: 0.5rem;
    flex-wrap: wrap;
}

h1 {
    font-size: 1.05rem;
    font-weight: 800;
    margin: 0;
}

p {
    margin: 0.12rem 0 0;
    color: rgba(226, 255, 247, 0.72);
    font-size: 0.78rem;
}

.title-icon {
    color: #6ff5be;
    font-size: 1.35rem;
}

.mode-pill {
    font-size: 0.68rem;
    color: #dffef7;
    border: 1px solid rgba(111, 245, 190, 0.28);
    background: rgba(111, 245, 190, 0.1);
    border-radius: 999px;
    padding: 0.12rem 0.42rem;
}

.bridge-pill {
    border-color: rgba(253, 230, 138, 0.35);
    background: rgba(253, 230, 138, 0.1);
}

.interpretive-pill {
    border-color: rgba(216, 180, 254, 0.35);
    background: rgba(126, 34, 206, 0.16);
}

.top-actions {
    gap: 0.45rem;
}

.icon-button,
.segmented button,
.build-actions button,
.measure-tabs button,
.toggle-row button {
    border: 1px solid rgba(226, 255, 247, 0.14);
    color: #e5fdf7;
    background: rgba(10, 20, 28, 0.72);
    transition: border-color 0.15s ease, background 0.15s ease;
}

.icon-button {
    width: 2rem;
    height: 2rem;
    display: grid;
    place-items: center;
    border-radius: 0.35rem;
}

.control-panel,
.metric-panel,
.legend-panel {
    position: absolute;
    z-index: 9;
    background: rgba(5, 8, 13, 0.72);
    border: 1px solid rgba(226, 255, 247, 0.12);
    backdrop-filter: blur(14px);
    box-shadow: 0 18px 50px rgba(0, 0, 0, 0.36);
}

.control-panel {
    top: 5.5rem;
    left: 1rem;
    width: min(19rem, calc(100vw - 2rem));
    max-height: calc(100vh - 7rem);
    overflow: auto;
    border-radius: 0.5rem;
    padding: 0.85rem;
}

.metric-panel {
    right: 1rem;
    bottom: 1rem;
    width: min(19rem, calc(100vw - 2rem));
    border-radius: 0.5rem;
    padding: 0.55rem;
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 0.35rem;
}

.legend-panel {
    right: 1rem;
    top: 5.5rem;
    width: min(19rem, calc(100vw - 2rem));
    max-height: calc(100vh - 15rem);
    overflow: auto;
    border-radius: 0.5rem;
    padding: 0.65rem;
    display: grid;
    gap: 0.65rem;
}

.panel-section + .panel-section {
    margin-top: 0.9rem;
}

h2 {
    margin: 0 0 0.55rem;
    font-size: 0.76rem;
    letter-spacing: 0;
    text-transform: uppercase;
    color: rgba(226, 255, 247, 0.62);
}

label {
    display: grid;
    grid-template-columns: 4.4rem 1fr 2.7rem;
    align-items: center;
    gap: 0.55rem;
    font-size: 0.78rem;
    margin: 0.46rem 0;
}

label strong {
    text-align: right;
    font-size: 0.74rem;
    color: #c9fff0;
}

input[type='range'] {
    width: 100%;
}

.checkbox-row {
    display: flex;
    gap: 0.45rem;
    grid-template-columns: none;
}

.segmented,
.build-actions,
.measure-tabs,
.toggle-row {
    display: grid;
    gap: 0.4rem;
}

.segmented {
    grid-template-columns: repeat(3, minmax(0, 1fr));
}

.build-actions {
    grid-template-columns: repeat(2, minmax(0, 1fr));
}

.build-actions button:first-child {
    grid-column: 1 / -1;
    color: #ffd1d8;
    border-color: rgba(251, 113, 133, 0.42);
}

.measure-tabs {
    grid-template-columns: repeat(4, minmax(0, 1fr));
    margin: 0.45rem 0;
}

.toggle-row {
    grid-template-columns: repeat(4, minmax(0, 1fr));
}

.segmented button,
.build-actions button,
.measure-tabs button,
.toggle-row button {
    min-height: 2rem;
    border-radius: 0.35rem;
    font-size: 0.76rem;
}

.build-actions button {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 0.35rem;
}

.segmented button.active,
.measure-tabs button.active,
.toggle-row button.active,
.icon-button:hover,
.segmented button:hover,
.build-actions button:hover,
.measure-tabs button:hover,
.toggle-row button:hover {
    border-color: rgba(111, 245, 190, 0.55);
    background: rgba(111, 245, 190, 0.14);
}

.measure-tabs button.active,
.toggle-row button.active {
    color: #08231d;
    background: #6ff5be;
}

.metric {
    justify-content: space-between;
    gap: 0.45rem;
    padding: 0.36rem 0.45rem;
    border-radius: 0.35rem;
    background: rgba(226, 255, 247, 0.055);
    font-size: 0.72rem;
}

.metric span {
    color: rgba(226, 255, 247, 0.64);
}

.metric strong {
    color: #e5fdf7;
    font-variant-numeric: tabular-nums;
}

.sm-legend,
.invariant-ledger {
    display: grid;
    gap: 0.45rem;
}

.sm-legend h2,
.invariant-ledger h2 {
    margin: 0 0 0.15rem;
    font-size: 0.72rem;
    text-transform: uppercase;
    color: rgba(226, 255, 247, 0.64);
}

.sm-legend-item {
    display: grid;
    grid-template-columns: 0.7rem minmax(0, 1fr);
    align-items: center;
    gap: 0.45rem;
    font-size: 0.72rem;
    color: rgba(226, 255, 247, 0.82);
}

.sm-legend-item i {
    width: 0.55rem;
    height: 0.55rem;
    border-radius: 50%;
}

.ledger-item {
    display: grid;
    grid-template-columns: 0.65rem minmax(0, 1fr) auto;
    align-items: center;
    gap: 0.45rem;
    padding: 0.34rem 0.42rem;
    border-radius: 0.35rem;
    background: rgba(226, 255, 247, 0.055);
}

.ledger-item > i {
    width: 0.52rem;
    height: 0.52rem;
    border-radius: 50%;
    background: #94a3b8;
}

.ledger-item.pass > i {
    background: #6ff5be;
}

.ledger-item.warn > i {
    background: #fde68a;
}

.ledger-item.fail > i {
    background: #fb7185;
}

.ledger-item span {
    display: grid;
    gap: 0.08rem;
    min-width: 0;
}

.ledger-item strong {
    font-size: 0.68rem;
    line-height: 1.1;
}

.ledger-item em {
    color: rgba(226, 255, 247, 0.58);
    font-size: 0.62rem;
    line-height: 1.1;
    font-style: normal;
}

.ledger-item b {
    color: #e5fdf7;
    font-size: 0.68rem;
    font-variant-numeric: tabular-nums;
}

@media (max-width: 820px) {
    .topbar {
        align-items: flex-start;
    }

    .home-link span:last-child,
    .title-wrap p {
        display: none;
    }

    .mode-pill {
        display: none;
    }

    .control-panel {
        top: auto;
        bottom: 0.75rem;
        left: 0.75rem;
        max-height: 42vh;
    }

    .metric-panel {
        top: 4.6rem;
        bottom: auto;
        right: 0.75rem;
    }

    .legend-panel {
        display: none;
    }
}
</style>
