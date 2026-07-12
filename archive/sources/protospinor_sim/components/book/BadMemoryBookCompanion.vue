<template>
    <main class="book-companion anchor-only" :style="stageVars">
        <section class="chapter-rail" aria-label="Book chapter simulations">
            <div class="rail-header">
                <div>
                    <p class="eyebrow">The Universe Has a Bad Memory</p>
                    <h1>Chapter Simulation Companion</h1>
                </div>
                <div class="rail-meta">
                    <div class="edition-chip">Chapters 1-12 loaded</div>
                    <div class="edition-chip">Second edition v5</div>
                </div>
            </div>

            <div class="chapter-grid">
                <button
                    v-for="(item, index) in chapters"
                    :key="item.id"
                    type="button"
                    class="chapter-button"
                    :class="{ active: index === activeIndex }"
                    @click="activeIndex = index"
                >
                    <span class="chapter-number">{{ item.chapter }}</span>
                    <span class="chapter-copy">
                        <span>{{ item.title }}</span>
                        <small>{{ item.arc }} - {{ item.modeLabel }}</small>
                    </span>
                </button>
            </div>
        </section>

        <section class="view-rail" aria-label="Chapter visual scenes">
            <button
                v-for="(item, index) in activeViewItems"
                :key="item.id"
                type="button"
                class="view-button"
                :class="{ active: index === activeViewIndex }"
                :aria-label="item.name"
                :title="item.name"
                @click="activeViewIndex = index"
            >
                <span>{{ item.shortLabel }}</span>
            </button>
        </section>

        <section class="sim-layout">
            <aside class="control-panel">
                <div class="panel-title">
                    <span class="i-tabler-adjustments-horizontal"></span>
                    <span>Conditions</span>
                </div>

                <label class="range-row">
                    <span>Capacity</span>
                    <input v-model.number="capacity" min="0.15" max="1" step="0.01" type="range">
                    <strong>{{ percent(capacity) }}</strong>
                </label>

                <label class="range-row">
                    <span>Disturbance</span>
                    <input v-model.number="disturbance" min="0" max="1" step="0.01" type="range">
                    <strong>{{ percent(disturbance) }}</strong>
                </label>

                <label class="range-row">
                    <span>Reuse</span>
                    <input v-model.number="reuse" min="1" max="8" step="1" type="range">
                    <strong>{{ reuse }}x</strong>
                </label>

                <div class="readout-list">
                    <div>
                        <span>Closure</span>
                        <strong>{{ percent(closureScore) }}</strong>
                    </div>
                    <div>
                        <span>Regime</span>
                        <strong>{{ activeChapter.modeLabel }}</strong>
                    </div>
                    <div>
                        <span>Kept</span>
                        <strong>{{ activeChapter.readouts.kept }}</strong>
                    </div>
                    <div>
                        <span>Dropped</span>
                        <strong>{{ activeChapter.readouts.dropped }}</strong>
                    </div>
                </div>
            </aside>

            <section class="stage-panel">
                <div class="stage-heading">
                    <div>
                        <p class="eyebrow">{{ activeChapter.arc }} - chapter {{ activeChapter.chapter }}</p>
                        <h2>{{ activeChapter.title }}</h2>
                    </div>
                    <span class="mode-icon" aria-hidden="true">
                        <span v-if="activeChapter.mode === 'admissibility'" class="i-tabler-filter-cog"></span>
                        <span v-else-if="activeChapter.mode === 'particle'" class="i-tabler-atom-2"></span>
                        <span v-else-if="activeChapter.mode === 'quantum'" class="i-tabler-wave-sine"></span>
                        <span v-else-if="activeChapter.mode === 'relation'" class="i-tabler-circuit-ground"></span>
                        <span v-else-if="activeChapter.mode === 'proto'" class="i-tabler-layers-intersect"></span>
                        <span v-else class="i-tabler-world-star"></span>
                    </span>
                </div>

                <div class="instrument-strip">
                    <div>
                        <span>Constraint</span>
                        <strong>{{ activeConstraint }}</strong>
                    </div>
                    <div>
                        <span>Observable</span>
                        <strong>{{ activeObservable }}</strong>
                    </div>
                    <div>
                        <span>Status</span>
                        <strong>Pedagogical model, not a numerical proof</strong>
                    </div>
                </div>

                <div
                    ref="stageFrameRef"
                    class="stage-frame"
                    @pointermove="handleStagePointer"
                    @pointerdown="triggerStagePulse"
                    @pointerup="releaseStagePointer"
                    @pointerleave="clearStagePointer"
                >
                    <svg viewBox="0 0 920 540" role="img" :aria-label="activeChapter.title">
                        <defs>
                            <pattern id="book-grid" width="46" height="46" patternUnits="userSpaceOnUse">
                                <path d="M 46 0 L 0 0 0 46" fill="none" stroke="rgba(255,255,255,.055)" stroke-width="1" />
                            </pattern>
                            <pattern id="ledger-halftone" width="5" height="5" patternUnits="userSpaceOnUse">
                                <circle cx="1" cy="1" r=".55" fill="#56f6ff" opacity=".52" />
                                <circle cx="3" cy="2" r=".45" fill="#ff4ff3" opacity=".36" />
                                <circle cx="2" cy="4" r=".5" fill="#ffffff" opacity=".42" />
                            </pattern>
                            <radialGradient id="ledger-plate-vignette" cx="50%" cy="46%" r="78%">
                                <stop offset="0%" stop-color="#16211f" />
                                <stop offset="42%" stop-color="#07100f" />
                                <stop offset="100%" stop-color="#000000" />
                            </radialGradient>
                            <filter id="book-soft-glow" x="-50%" y="-50%" width="200%" height="200%">
                                <feGaussianBlur stdDeviation="8" result="blur" />
                                <feMerge>
                                    <feMergeNode in="blur" />
                                    <feMergeNode in="SourceGraphic" />
                                </feMerge>
                            </filter>
                            <filter id="ledger-rgb-bleed" x="-20%" y="-20%" width="140%" height="140%">
                                <feDropShadow dx="-1.2" dy=".2" stdDeviation=".35" flood-color="#00f5ff" flood-opacity=".45" />
                                <feDropShadow dx="1.2" dy="-.2" stdDeviation=".35" flood-color="#ff2bd6" flood-opacity=".34" />
                            </filter>
                            <marker id="arrow-head" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto">
                                <path d="M 0 0 L 10 5 L 0 10 z" fill="rgba(255,255,255,.42)" />
                            </marker>
                        </defs>

                        <rect width="920" height="540" rx="0" fill="#000000" />
                        <rect width="920" height="540" fill="url(#ledger-plate-vignette)" opacity=".96" />
                        <rect width="920" height="540" fill="url(#ledger-halftone)" opacity=".32" />
                        <g class="ledger-plate-grain">
                            <circle
                                v-for="grain in ledgerPlateGrain"
                                :key="grain.key"
                                :cx="grain.x"
                                :cy="grain.y"
                                :r="grain.r"
                                :fill="grain.fill"
                                :opacity="grain.opacity"
                            />
                        </g>
                        <path
                            v-for="band in ledgerScanBands"
                            :key="band.key"
                            :d="band.path"
                            fill="none"
                            :stroke="band.stroke"
                            :stroke-width="band.width"
                            :stroke-opacity="band.opacity"
                        />
                        <rect width="920" height="540" fill="url(#book-grid)" opacity=".16" />
                        <g class="axis-overlay">
                            <path d="M 64 474 L 856 474" stroke="rgba(255,255,255,.24)" stroke-width="2" />
                            <path d="M 64 474 L 64 110" stroke="rgba(255,255,255,.24)" stroke-width="2" />
                            <text x="70" y="500" class="svg-micro">capacity-limited projection</text>
                            <text x="28" y="132" class="svg-micro" transform="rotate(-90 28 132)">closure pressure</text>
                        </g>
                        <path
                            v-for="lane in backdropLanes"
                            :key="lane.key"
                            :d="lane.path"
                            fill="none"
                            stroke="rgba(255,255,255,.07)"
                            :stroke-width="lane.width"
                        />
                        <g v-if="isOpeningLedgerScene" opacity=".78" filter="url(#ledger-rgb-bleed)">
                            <path
                                v-for="edge in ledgerMeshEdges"
                                :key="edge.key"
                                :d="edge.path"
                                fill="none"
                                :stroke="edge.hot ? 'var(--accent)' : 'rgba(255,255,255,.13)'"
                                :stroke-width="edge.width"
                                :stroke-opacity="edge.opacity"
                            />
                            <ellipse
                                v-for="ring in ledgerBasinRings"
                                :key="ring.key"
                                :cx="ring.x"
                                :cy="ring.y"
                                :rx="ring.rx"
                                :ry="ring.ry"
                                fill="none"
                                :stroke="ring.primary ? 'var(--accent2)' : 'rgba(255,255,255,.18)'"
                                :stroke-width="ring.width"
                                :opacity="ring.opacity"
                            />
                        </g>

                        <g v-if="activeSceneKey === 'ch-01-admissible-chapter'">
                            <g v-if="chapterOnePointerVisible" filter="url(#book-soft-glow)">
                                <circle
                                    :cx="stagePointer.x"
                                    :cy="stagePointer.y"
                                    :r="42 + pointerStrength * 44"
                                    fill="none"
                                    stroke="var(--accent)"
                                    :stroke-width="1.5 + pointerStrength * 2.5"
                                    :opacity=".16 + pointerStrength * .24"
                                />
                                <circle
                                    :cx="stagePointer.x"
                                    :cy="stagePointer.y"
                                    :r="7 + pointerStrength * 5"
                                    fill="var(--accent2)"
                                    :opacity=".32 + pointerStrength * .5"
                                />
                            </g>
                            <g v-if="pulseStrength > 0" filter="url(#book-soft-glow)">
                                <circle
                                    :cx="stagePointer.pulseX"
                                    :cy="stagePointer.pulseY"
                                    :r="pulseRadius"
                                    fill="none"
                                    stroke="var(--accent2)"
                                    stroke-width="5"
                                    :opacity="pulseStrength * .72"
                                />
                                <circle
                                    :cx="stagePointer.pulseX"
                                    :cy="stagePointer.pulseY"
                                    :r="pulseRadius * .42"
                                    fill="var(--accent)"
                                    :opacity="pulseStrength * .16"
                                />
                            </g>
                            <g opacity=".92">
                                <path
                                    v-for="stream in chapterOneStreams"
                                    :key="stream.key"
                                    :d="stream.path"
                                    fill="none"
                                    :stroke="stream.carried ? 'var(--accent)' : 'rgba(255,255,255,.18)'"
                                    :stroke-width="stream.carried ? 2.4 : 1.1"
                                    :stroke-opacity="stream.opacity"
                                />
                                <circle
                                    v-for="mark in chapterOneMicroMarks"
                                    :key="mark.key"
                                    :cx="mark.x"
                                    :cy="mark.y"
                                    :r="mark.r"
                                    :fill="mark.carried ? 'var(--accent)' : mark.fill"
                                    :opacity="mark.opacity"
                                />
                            </g>

                            <g filter="url(#book-soft-glow)">
                                <circle
                                    v-for="particle in chapterOneFlowParticles"
                                    :key="particle.key"
                                    :cx="particle.x"
                                    :cy="particle.y"
                                    :r="particle.r"
                                    :fill="particle.carried ? 'var(--accent)' : 'rgba(255,255,255,.5)'"
                                    :opacity="particle.opacity"
                                />
                            </g>

                            <g filter="url(#book-soft-glow)">
                                <rect x="384" y="86" width="92" height="368" rx="46" fill="rgba(255,255,255,.06)" stroke="var(--accent2)" stroke-width="4" />
                                <rect
                                    x="389"
                                    :y="chapterOneScanY"
                                    width="82"
                                    height="34"
                                    rx="17"
                                    fill="var(--accent2)"
                                    opacity=".14"
                                />
                                <circle
                                    v-for="sample in chapterOneSamples"
                                    :key="sample.key"
                                    :cx="430"
                                    :cy="sample.y"
                                    :r="sample.r"
                                    fill="rgba(255,255,255,.08)"
                                    stroke="var(--accent)"
                                    :stroke-width="sample.width"
                                />
                                <path d="M 430 112 C 408 178 408 362 430 428 C 452 362 452 178 430 112" fill="rgba(255,255,255,.035)" stroke="rgba(255,255,255,.2)" stroke-width="2" />
                            </g>

                            <path
                                v-for="thread in chapterOneCarriedThreads"
                                :key="thread.key"
                                :d="thread.path"
                                fill="none"
                                stroke="var(--accent2)"
                                :stroke-width="thread.width"
                                :stroke-opacity="thread.opacity"
                                stroke-linecap="round"
                            />

                            <g :transform="`translate(706 ${270 + wobble(2, 4)})`" filter="url(#book-soft-glow)">
                                <circle
                                    v-for="echo in chapterOneEchoes"
                                    :key="echo.key"
                                    :r="echo.r"
                                    fill="none"
                                    :stroke="echo.primary ? 'var(--accent2)' : 'rgba(255,255,255,.2)'"
                                    :stroke-width="echo.width"
                                    :opacity="echo.opacity"
                                />
                                <path
                                    :d="chapterOneStableGlyph"
                                    fill="rgba(255,255,255,.045)"
                                    stroke="var(--accent)"
                                    stroke-width="5"
                                    stroke-linejoin="round"
                                />
                                <circle
                                    v-for="satellite in chapterOneSatellites"
                                    :key="satellite.key"
                                    :cx="satellite.x"
                                    :cy="satellite.y"
                                    :r="satellite.r"
                                    fill="var(--accent2)"
                                    :opacity="satellite.opacity"
                                />
                                <circle r="12" fill="var(--accent2)" />
                            </g>

                            <g opacity=".58">
                                <path
                                    v-for="alias in chapterOneAliases"
                                    :key="alias.key"
                                    :d="alias.path"
                                    fill="none"
                                    stroke="rgba(255,255,255,.16)"
                                    :stroke-width="alias.width"
                                    stroke-dasharray="6 12"
                                />
                            </g>
                        </g>

                        <g v-else-if="activeSceneKey === 'ch-01-bell'">
                            <g opacity=".82">
                                <path
                                    v-for="field in bellSharedFields"
                                    :key="field.key"
                                    :d="field.path"
                                    fill="none"
                                    :stroke="field.primary ? 'var(--accent2)' : 'rgba(255,255,255,.16)'"
                                    :stroke-width="field.width"
                                    :stroke-opacity="field.opacity"
                                />
                            </g>

                            <g
                                v-for="region in bellRegions"
                                :key="region.key"
                                :transform="`translate(${region.x} ${region.y})`"
                                filter="url(#book-soft-glow)"
                            >
                                <circle :r="region.r" fill="rgba(255,255,255,.035)" stroke="rgba(255,255,255,.22)" stroke-width="2" />
                                <circle :r="region.r * .68" fill="rgba(255,255,255,.025)" stroke="var(--accent)" :stroke-width="region.active ? 4 : 2" :opacity="region.active ? .95 : .54" />
                                <circle
                                    v-for="beable in region.beables"
                                    :key="beable.key"
                                    :cx="beable.x"
                                    :cy="beable.y"
                                    :r="beable.r"
                                    :fill="beable.local ? 'var(--accent)' : 'rgba(255,255,255,.35)'"
                                    :opacity="beable.opacity"
                                />
                            </g>

                            <g filter="url(#book-soft-glow)">
                                <path :d="bellJointStatePath" fill="rgba(255,255,255,.035)" stroke="var(--accent2)" stroke-width="4" />
                                <circle :cx="stagePointer.x" :cy="stagePointer.y" :r="chapterOnePointerVisible ? 16 + pointerStrength * 18 : 0" fill="var(--accent2)" :opacity="chapterOnePointerVisible ? .3 : 0" />
                            </g>
                        </g>

                        <g v-else-if="activeSceneKey === 'ch-01-sampling'">
                            <g opacity=".82">
                                <path
                                    v-for="wave in samplingRawWaves"
                                    :key="wave.key"
                                    :d="wave.path"
                                    fill="none"
                                    :stroke="wave.primary ? 'var(--accent)' : 'rgba(255,255,255,.18)'"
                                    :stroke-width="wave.width"
                                    :stroke-opacity="wave.opacity"
                                />
                            </g>

                            <g filter="url(#book-soft-glow)">
                                <path :d="samplingReconstructionPath" fill="none" stroke="var(--accent2)" stroke-width="5" stroke-linecap="round" />
                                <path :d="samplingAliasPath" fill="none" stroke="rgba(255,255,255,.25)" stroke-width="3" stroke-dasharray="8 12" />
                                <circle
                                    v-for="sample in samplingPoints"
                                    :key="sample.key"
                                    :cx="sample.x"
                                    :cy="sample.y"
                                    :r="sample.r"
                                    :fill="sample.valid ? 'var(--accent2)' : 'rgba(255,255,255,.38)'"
                                    :opacity="sample.opacity"
                                />
                                <rect :x="samplingApertureX" y="92" width="18" height="356" rx="9" fill="var(--accent)" opacity=".18" />
                            </g>

                            <g v-if="pulseStrength > 0" filter="url(#book-soft-glow)">
                                <circle :cx="stagePointer.pulseX" :cy="stagePointer.pulseY" :r="pulseRadius * .7" fill="none" stroke="var(--accent2)" stroke-width="4" :opacity="pulseStrength * .68" />
                            </g>
                        </g>

                        <g v-else-if="activeChapter.mode === 'admissibility'">
                            <text x="80" y="78" class="svg-label">raw distinctions</text>
                            <text x="382" y="78" class="svg-label">finite gate</text>
                            <text x="650" y="78" class="svg-label">reusable description</text>

                            <rect
                                :x="gateX"
                                :y="118 - gateHeight / 2"
                                width="34"
                                :height="gateHeight"
                                rx="7"
                                fill="rgba(255,255,255,.08)"
                                stroke="var(--accent)"
                                stroke-width="2"
                            />
                            <path
                                v-for="trace in memoryTraces"
                                :key="trace.key"
                                :d="trace.rawPath"
                                fill="none"
                                :stroke="trace.carried ? 'var(--accent)' : 'rgba(255,255,255,.18)'"
                                :stroke-width="trace.carried ? 2.5 : 1.2"
                                :stroke-opacity="trace.opacity"
                            />
                            <path
                                v-for="trace in carriedTraces"
                                :key="`${trace.key}-out`"
                                :d="trace.outPath"
                                fill="none"
                                stroke="var(--accent2)"
                                stroke-width="2"
                                :stroke-opacity="trace.opacity"
                            />
                            <circle
                                v-for="trace in memoryTraces"
                                :key="`${trace.key}-dot`"
                                :cx="trace.startX"
                                :cy="trace.startY"
                                :r="trace.carried ? 5 : 3"
                                :fill="trace.carried ? 'var(--accent)' : 'rgba(255,255,255,.25)'"
                            />
                            <g filter="url(#book-soft-glow)">
                                <circle cx="718" cy="270" :r="projectionRadius" fill="none" stroke="var(--accent2)" stroke-width="4" />
                                <circle cx="718" cy="270" :r="projectionRadius * .58" fill="rgba(255,255,255,.04)" stroke="var(--accent)" stroke-width="2" />
                                <circle cx="718" cy="270" :r="Math.max(8, projectionRadius * .16)" fill="var(--accent)" />
                            </g>
                        </g>

                        <g v-else-if="activeChapter.mode === 'particle'">
                            <text x="84" y="76" class="svg-label">inner cost</text>
                            <text x="396" y="76" class="svg-label">identity rule</text>
                            <text x="662" y="76" class="svg-label">physical role</text>

                            <g :transform="`translate(198 ${270 + wobble(0, 14)})`">
                                <circle r="68" fill="rgba(255,255,255,.035)" stroke="var(--accent)" stroke-width="2" />
                                <circle r="24" fill="var(--accent)" opacity=".88" />
                                <path
                                    v-for="i in 3"
                                    :key="`orbit-${i}`"
                                    :d="orbitPath(0, 0, 62 + i * 21, i * 26)"
                                    fill="none"
                                    stroke="rgba(255,255,255,.35)"
                                    stroke-width="1.6"
                                />
                            </g>

                            <g v-if="activeChapter.variant === 'quark'">
                                <line x1="444" y1="216" x2="516" y2="336" stroke="var(--accent2)" stroke-width="6" stroke-linecap="round" />
                                <line x1="516" y1="336" x2="374" y2="336" stroke="var(--accent2)" stroke-width="6" stroke-linecap="round" />
                                <line x1="374" y1="336" x2="444" y2="216" stroke="var(--accent2)" stroke-width="6" stroke-linecap="round" />
                                <circle cx="444" cy="216" r="26" fill="#ff6b6b" />
                                <circle cx="516" cy="336" r="26" fill="#63e6be" />
                                <circle cx="374" cy="336" r="26" fill="#74c0fc" />
                                <text x="406" y="394" class="svg-note">isolation cost rises outward</text>
                            </g>
                            <g v-else-if="activeChapter.variant === 'atom'">
                                <circle cx="452" cy="270" r="42" fill="var(--accent)" filter="url(#book-soft-glow)" />
                                <ellipse cx="452" cy="270" rx="116" ry="46" fill="none" stroke="var(--accent2)" stroke-width="4" />
                                <ellipse cx="452" cy="270" rx="72" ry="108" fill="none" stroke="rgba(255,255,255,.35)" stroke-width="2" />
                                <circle :cx="452 + Math.cos(phase) * 116" :cy="270 + Math.sin(phase) * 46" r="9" fill="var(--accent2)" />
                                <circle :cx="452 + Math.cos(phase + 2.2) * 72" :cy="270 + Math.sin(phase + 2.2) * 108" r="7" fill="#f8f9fa" />
                            </g>
                            <g v-else-if="activeChapter.variant === 'neutrino'">
                                <path d="M 326 270 C 390 250 480 250 548 270 S 638 292 686 270" fill="none" stroke="var(--accent2)" stroke-width="3" stroke-dasharray="5 12" />
                                <path d="M 326 270 C 418 268 520 268 686 270" fill="none" stroke="var(--accent)" stroke-width="1.6" opacity=".72" />
                                <circle cx="446" cy="270" r="36" fill="rgba(255,255,255,.025)" stroke="rgba(255,255,255,.18)" stroke-width="2" />
                                <text x="386" y="352" class="svg-note">tiny exposed footprint</text>
                            </g>
                            <g v-else-if="activeChapter.variant === 'positron'">
                                <circle :cx="410 - Math.cos(phase) * 18" cy="270" r="34" fill="none" stroke="var(--accent)" stroke-width="4" />
                                <circle :cx="496 + Math.cos(phase) * 18" cy="270" r="34" fill="none" stroke="var(--accent2)" stroke-width="4" />
                                <path d="M 364 270 C 408 232 496 232 542 270 C 496 308 408 308 364 270" fill="rgba(255,255,255,.035)" stroke="rgba(255,255,255,.32)" stroke-width="2" />
                                <path d="M 452 210 L 452 330" stroke="rgba(255,255,255,.18)" stroke-width="2" stroke-dasharray="8 10" />
                                <text x="384" y="370" class="svg-note">inverse identity cancels</text>
                            </g>
                            <g v-else-if="activeChapter.variant === 'muon' || activeChapter.variant === 'tau'">
                                <circle cx="452" cy="270" :r="48 + disturbance * 48" fill="rgba(255,255,255,.035)" stroke="var(--accent)" stroke-width="4" />
                                <circle cx="452" cy="270" :r="92 + disturbance * 42" fill="none" stroke="var(--accent2)" stroke-width="3" stroke-dasharray="10 8" />
                                <path d="M 514 270 C 564 246 604 246 648 270" fill="none" stroke="rgba(255,255,255,.42)" stroke-width="3" marker-end="url(#arrow-head)" />
                                <circle cx="452" cy="270" r="18" fill="var(--accent)" />
                                <text x="386" y="384" class="svg-note">cost ring outruns closure</text>
                            </g>
                            <g v-else-if="activeChapter.variant === 'boson'">
                                <path d="M 336 218 C 398 218 420 246 452 270 C 486 296 514 322 584 322" fill="none" stroke="var(--accent)" stroke-width="5" stroke-linecap="round" />
                                <path d="M 336 322 C 398 322 420 294 452 270 C 486 244 514 218 584 218" fill="none" stroke="var(--accent2)" stroke-width="5" stroke-linecap="round" />
                                <rect x="424" y="230" width="58" height="80" rx="8" fill="rgba(255,255,255,.08)" stroke="rgba(255,255,255,.32)" stroke-width="2" />
                                <text x="394" y="382" class="svg-note">identity rewrite channel</text>
                            </g>
                            <g v-else-if="activeChapter.variant === 'higgs'">
                                <circle cx="452" cy="270" r="124" fill="rgba(245, 158, 11, .08)" stroke="rgba(255,255,255,.16)" stroke-width="2" />
                                <circle cx="452" cy="270" r="86" fill="rgba(255,255,255,.035)" stroke="var(--accent2)" stroke-width="3" />
                                <circle cx="452" cy="270" r="42" fill="var(--accent)" opacity=".9" />
                                <path
                                    v-for="i in 4"
                                    :key="`higgs-ring-${i}`"
                                    :d="orbitPath(452, 270, 54 + i * 24, i * 22)"
                                    fill="none"
                                    stroke="rgba(255,255,255,.25)"
                                    stroke-width="1.6"
                                />
                                <text x="388" y="388" class="svg-note">persistence has a price</text>
                            </g>
                            <g v-else>
                                <circle cx="446" cy="270" :r="52 + effectiveMemory * 34" fill="rgba(255,255,255,.035)" stroke="var(--accent2)" stroke-width="4" />
                                <path
                                    v-for="wave in transportWaves"
                                    :key="wave.key"
                                    :d="wave.path"
                                    fill="none"
                                    stroke="var(--accent)"
                                    :stroke-width="wave.width"
                                    :stroke-opacity="wave.opacity"
                                />
                            </g>

                            <g filter="url(#book-soft-glow)">
                                <circle cx="720" cy="270" :r="42 + activeChapter.params.anchors * 11" fill="rgba(255,255,255,.05)" stroke="var(--accent2)" stroke-width="3" />
                                <path :d="identityNeedlePath" fill="none" stroke="var(--accent)" stroke-width="5" stroke-linecap="round" />
                                <text x="668" y="356" class="svg-note">{{ activeChapter.readouts.result }}</text>
                            </g>
                        </g>

                        <g v-else-if="activeChapter.mode === 'quantum'">
                            <text x="84" y="76" class="svg-label">deferred branches</text>
                            <text x="412" y="76" class="svg-label">measurement aperture</text>
                            <text x="650" y="76" class="svg-label">selected continuation</text>

                            <circle cx="138" cy="270" r="24" fill="var(--accent)" filter="url(#book-soft-glow)" />
                            <path
                                v-for="branch in branchPaths"
                                :key="branch.key"
                                :d="branch.path"
                                fill="none"
                                :stroke="branch.selected ? 'var(--accent2)' : 'rgba(255,255,255,.22)'"
                                :stroke-width="branch.selected ? 4 : 1.7"
                                :stroke-opacity="branch.opacity"
                            />
                            <rect
                                x="430"
                                :y="166 + measurementShift"
                                width="36"
                                :height="208 - measurementShift * .5"
                                rx="8"
                                fill="rgba(255,255,255,.08)"
                                stroke="var(--accent2)"
                                stroke-width="3"
                            />
                            <circle cx="688" cy="270" :r="44 + closureScore * 42" fill="rgba(255,255,255,.035)" stroke="var(--accent2)" stroke-width="4" />
                            <circle :cx="688 + Math.cos(phase * 1.4) * 24" :cy="270 + Math.sin(phase * 1.4) * 16" r="10" fill="var(--accent)" />
                            <path d="M760 210 C810 238 810 302 760 330" fill="none" stroke="rgba(255,255,255,.23)" stroke-width="2" />
                            <text x="628" y="366" class="svg-note">{{ activeChapter.readouts.result }}</text>
                        </g>

                        <g v-else-if="activeChapter.mode === 'relation'">
                            <text x="86" y="76" class="svg-label">local parts</text>
                            <text x="388" y="76" class="svg-label">agreement loop</text>
                            <text x="650" y="76" class="svg-label">regime</text>

                            <circle
                                v-for="node in relationNodes"
                                :key="node.key"
                                :cx="node.x"
                                :cy="node.y"
                                :r="node.r"
                                fill="rgba(255,255,255,.06)"
                                stroke="var(--accent)"
                                stroke-width="2"
                            />
                            <path
                                v-for="edge in relationEdges"
                                :key="edge.key"
                                :d="edge.path"
                                fill="none"
                                stroke="var(--accent2)"
                                :stroke-width="edge.width"
                                stroke-linecap="round"
                                opacity=".84"
                            />
                            <path :d="loopPath" fill="none" stroke="rgba(255,255,255,.28)" stroke-width="3" stroke-dasharray="8 12" />
                            <circle cx="700" cy="270" :r="64 + effectiveMemory * 34" fill="rgba(255,255,255,.035)" stroke="var(--accent2)" stroke-width="3" />
                            <path
                                d="M656 270 C662 218 732 218 744 270 C732 322 662 322 656 270"
                                fill="rgba(255,255,255,.06)"
                                stroke="var(--accent)"
                                stroke-width="3"
                            />
                            <text x="638" y="368" class="svg-note">{{ activeChapter.readouts.result }}</text>
                        </g>

                        <g v-else-if="activeChapter.mode === 'proto'">
                            <text x="82" y="76" class="svg-label">circle</text>
                            <text x="316" y="76" class="svg-label">nil gap</text>
                            <text x="538" y="76" class="svg-label">lens twist</text>
                            <text x="710" y="76" class="svg-label">projection</text>

                            <g :transform="`translate(166 ${270})`">
                                <circle r="76" fill="rgba(255,255,255,.035)" stroke="var(--accent)" stroke-width="3" />
                                <circle :cx="Math.cos(phase) * 76" :cy="Math.sin(phase) * 76" r="12" fill="var(--accent2)" filter="url(#book-soft-glow)" />
                                <path :d="orbitPath(0, 0, 112, 0)" fill="none" stroke="rgba(255,255,255,.22)" stroke-width="2" />
                            </g>
                            <path
                                :d="nilGapPath"
                                fill="none"
                                stroke="var(--accent2)"
                                stroke-width="9"
                                stroke-linecap="round"
                                opacity=".84"
                            />
                            <g :transform="`translate(520 270) rotate(${twistDegrees})`">
                                <ellipse rx="104" ry="34" fill="none" stroke="var(--accent)" stroke-width="4" />
                                <ellipse rx="104" ry="34" fill="none" stroke="rgba(255,255,255,.24)" stroke-width="2" transform="rotate(90)" />
                            </g>
                            <g filter="url(#book-soft-glow)">
                                <circle cx="738" cy="270" :r="42 + closureScore * 36" fill="rgba(255,255,255,.05)" stroke="var(--accent2)" stroke-width="4" />
                                <circle cx="738" cy="270" :r="12 + activeChapter.params.anchors * 8" fill="var(--accent)" />
                            </g>
                            <text x="676" y="366" class="svg-note">{{ activeChapter.readouts.result }}</text>
                        </g>

                        <g v-else>
                            <text x="78" y="76" class="svg-label">global constraint</text>
                            <text x="392" y="76" class="svg-label">history</text>
                            <text x="660" y="76" class="svg-label">local realization</text>

                            <path :d="cosmicPlanePath" fill="rgba(255,255,255,.035)" stroke="var(--accent2)" stroke-width="3" />
                            <circle
                                v-for="well in gravityWells"
                                :key="well.key"
                                :cx="well.x"
                                :cy="well.y"
                                :r="well.r"
                                fill="var(--accent)"
                                :opacity="well.opacity"
                            />
                            <path
                                v-for="arc in cosmicArcs"
                                :key="arc.key"
                                :d="arc.path"
                                fill="none"
                                stroke="rgba(255,255,255,.26)"
                                :stroke-width="arc.width"
                            />
                            <circle cx="708" cy="270" :r="60 + closureScore * 34" fill="rgba(255,255,255,.04)" stroke="var(--accent2)" stroke-width="4" />
                            <path d="M650 270 C674 230 736 230 764 270 C736 310 674 310 650 270" fill="none" stroke="var(--accent)" stroke-width="4" />
                            <text x="638" y="368" class="svg-note">{{ activeChapter.readouts.result }}</text>
                        </g>
                    </svg>
                </div>
            </section>

            <aside class="explain-panel">
                <div class="panel-title">
                    <span class="i-tabler-book-2"></span>
                    <span>Chapter Fit</span>
                </div>
                <p>{{ activeChapter.premise }}</p>
                <div class="claim-block">
                    <span>Simulation</span>
                    <strong>{{ activeChapter.simulation }}</strong>
                </div>
                <div class="claim-block">
                    <span>MTT / book reading</span>
                    <strong>{{ activeChapter.mtt }}</strong>
                </div>
                <div class="claim-block">
                    <span>Visible outcome</span>
                    <strong>{{ activeChapter.readouts.result }}</strong>
                </div>
                <div class="claim-block">
                    <span>Scientific caution</span>
                    <strong>Physics labels are interpretive bridges; the native rule shown here is admissible projection under finite capacity.</strong>
                </div>
            </aside>
        </section>
    </main>
</template>

<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'

type ChapterMode = 'admissibility' | 'particle' | 'quantum' | 'relation' | 'proto' | 'cosmos'
type ChapterVariant = 'none' | 'electron' | 'photon' | 'neutrino' | 'positron' | 'muon' | 'tau' | 'quark' | 'boson' | 'higgs' | 'atom' | 'record' | 'life' | 'gravity' | 'time' | 'bad-memory' | 'interlude'
type MechanismKind = 'bell-local-beables' | 'sampling-reconstruction'

interface MechanismVisual {
    id: string
    name: string
    shortLabel: string
    kind: MechanismKind
    accent?: string
    accent2?: string
}

interface ChapterSim {
    id: string
    chapter: string
    arc: 'Arc I' | 'Arc II'
    title: string
    mode: ChapterMode
    modeLabel: string
    variant: ChapterVariant
    accent: string
    accent2: string
    premise: string
    simulation: string
    mtt: string
    readouts: {
        kept: string
        dropped: string
        result: string
    }
    params: {
        capacity: number
        disturbance: number
        memory: number
        anchors: number
        branches: number
        gravity: number
        twist: number
        closure: number
    }
    mechanisms?: MechanismVisual[]
}

const chapters: ChapterSim[] = [
    {
        id: 'ch-01-admissible',
        chapter: '1',
        arc: 'Arc I',
        title: 'Why Anything Can Be Described at All',
        mode: 'admissibility',
        modeLabel: 'projection gate',
        variant: 'none',
        accent: '#64dfdf',
        accent2: '#ffd166',
        premise: 'Physics begins where projection can be reused without destroying its own variables.',
        simulation: 'A finite gate keeps only distinctions that can survive disturbance and repeated application.',
        mtt: 'Locality, finiteness, and reusability act as the entry conditions for an admissible physical description.',
        readouts: {
            kept: 'stable distinctions',
            dropped: 'aliasing detail',
            result: 'law-like projection',
        },
        params: { capacity: .72, disturbance: .25, memory: .54, anchors: 2, branches: 5, gravity: .2, twist: .18, closure: .72 },
        mechanisms: [
            {
                id: 'ch-01-bell',
                name: 'Mechanism 1',
                shortLabel: 'M1',
                kind: 'bell-local-beables',
                accent: '#80ffdb',
                accent2: '#ffb703',
            },
            {
                id: 'ch-01-sampling',
                name: 'Mechanism 2',
                shortLabel: 'M2',
                kind: 'sampling-reconstruction',
                accent: '#74c0fc',
                accent2: '#ffdd57',
            },
        ],
    },
    {
        id: 'ch-02-forgetting',
        chapter: '2',
        arc: 'Arc I',
        title: 'What Remains After Forgetting',
        mode: 'admissibility',
        modeLabel: 'memory decay',
        variant: 'bad-memory',
        accent: '#f77f00',
        accent2: '#80ed99',
        premise: 'Forgetting is not a defect in the argument. It is the structural condition that lets stable variables exist.',
        simulation: 'Repeated passes erase expensive detail while preserving the lower-cost residue that can be reinstated.',
        mtt: 'The physical world is the part of richer structure that remains admissible after capacity limits do their work.',
        readouts: {
            kept: 'low-cost residue',
            dropped: 'over-specific history',
            result: 'surviving pattern',
        },
        params: { capacity: .58, disturbance: .38, memory: .38, anchors: 1, branches: 7, gravity: .12, twist: .15, closure: .64 },
    },
    {
        id: 'ch-03-physics-needs',
        chapter: '3',
        arc: 'Arc I',
        title: 'What Physics Cannot Do Without',
        mode: 'admissibility',
        modeLabel: 'minimal ledger',
        variant: 'none',
        accent: '#4cc9f0',
        accent2: '#fcbf49',
        premise: 'The chapter asks which structural ingredients must exist before physics can be stable at all.',
        simulation: 'Local sampling, bounded storage, and repeatable reconstruction are shown as the three minimal ledgers.',
        mtt: 'This is the pre-particle constraint layer: before labels like electron or photon, there must be reusable closure.',
        readouts: {
            kept: 'local, finite, reusable',
            dropped: 'unbounded distinction',
            result: 'minimal physics interface',
        },
        params: { capacity: .69, disturbance: .28, memory: .5, anchors: 2, branches: 5, gravity: .16, twist: .24, closure: .7 },
    },
    {
        id: 'ch-04-electron',
        chapter: '4',
        arc: 'Arc I',
        title: 'The Electron: The Cheapest Durable Identity',
        mode: 'particle',
        modeLabel: 'identity anchor',
        variant: 'electron',
        accent: '#5eead4',
        accent2: '#fca5a5',
        premise: 'A stable particle is shown as a low-cost identity that keeps returning to the same admissible anchor.',
        simulation: 'The central identity rule resists disturbance because its closure cost stays below the reuse threshold.',
        mtt: 'The label electron is interpretive here; the native piece is a cheap stable anchor under repeated projection.',
        readouts: {
            kept: 'charge identity',
            dropped: 'internal phase detail',
            result: 'durable lepton-like role',
        },
        params: { capacity: .76, disturbance: .18, memory: .65, anchors: 2, branches: 3, gravity: .16, twist: .42, closure: .82 },
    },
    {
        id: 'ch-05-photon',
        chapter: '5',
        arc: 'Arc I',
        title: 'The Photon: Influence Without Memory',
        mode: 'particle',
        modeLabel: 'transport pulse',
        variant: 'photon',
        accent: '#facc15',
        accent2: '#38bdf8',
        premise: 'The photon chapter is represented as influence that travels without becoming an anchored identity.',
        simulation: 'A wave packet crosses the identity rule with little retained residue and no durable rest anchor.',
        mtt: 'This is the book transport side: influence can be coherent without carrying the cost of local persistence.',
        readouts: {
            kept: 'phase relation',
            dropped: 'rest anchor',
            result: 'unanchored transport',
        },
        params: { capacity: .7, disturbance: .22, memory: .2, anchors: 0, branches: 4, gravity: .06, twist: .3, closure: .7 },
    },
    {
        id: 'ch-06-neutrino',
        chapter: '6',
        arc: 'Arc I',
        title: 'The Neutrino: Participation Without Anchoring Structure',
        mode: 'particle',
        modeLabel: 'weak footprint',
        variant: 'neutrino',
        accent: '#99f6e4',
        accent2: '#a5b4fc',
        premise: 'The neutrino is shown as participation with almost no exposed anchoring in the visible layer.',
        simulation: 'A faint phase trace passes through the identity rule while leaving only a narrow projection footprint.',
        mtt: 'The label neutrino is interpretive; the native rule is shared participation without strong local anchoring.',
        readouts: {
            kept: 'directional participation',
            dropped: 'strong local anchor',
            result: 'weakly visible role',
        },
        params: { capacity: .68, disturbance: .18, memory: .24, anchors: 0, branches: 5, gravity: .05, twist: .52, closure: .62 },
    },
    {
        id: 'ch-07-positron',
        chapter: '7',
        arc: 'Arc I',
        title: 'The Positron: Clean Cancellation of Identity',
        mode: 'particle',
        modeLabel: 'cancellation pair',
        variant: 'positron',
        accent: '#fb7185',
        accent2: '#67e8f9',
        premise: 'The positron chapter is represented as an opposite identity whose clean meeting cancels exposed charge memory.',
        simulation: 'Two mirrored identity residues converge; successful cancellation removes the local anchor while preserving transport.',
        mtt: 'The native point is not that antimatter is decorative, but that inverse closure can erase an exposed identity cleanly.',
        readouts: {
            kept: 'balanced inverse',
            dropped: 'persistent charge anchor',
            result: 'clean cancellation',
        },
        params: { capacity: .74, disturbance: .2, memory: .56, anchors: 2, branches: 4, gravity: .1, twist: .44, closure: .78 },
    },
    {
        id: 'ch-08-muon-tau',
        chapter: '8',
        arc: 'Arc I',
        title: 'The Muon and the Tau: Identity That Costs Too Much',
        mode: 'particle',
        modeLabel: 'costly identity',
        variant: 'muon',
        accent: '#f0abfc',
        accent2: '#fde047',
        premise: 'The muon and tau are shown as electron-like identities whose higher cost makes durable persistence harder.',
        simulation: 'The identity anchor exists, but disturbance grows the cost ring until decay becomes the cheaper continuation.',
        mtt: 'This visual treats mass/lifetime as an interpretive bridge to closure cost under repeated projection.',
        readouts: {
            kept: 'lepton pattern',
            dropped: 'long persistence',
            result: 'temporary heavy identity',
        },
        params: { capacity: .61, disturbance: .44, memory: .52, anchors: 2, branches: 5, gravity: .2, twist: .58, closure: .57 },
    },
    {
        id: 'ch-09-quarks',
        chapter: '9',
        arc: 'Arc I',
        title: 'Quarks and Gluons: Identity Forbidden from Isolation',
        mode: 'particle',
        modeLabel: 'confinement',
        variant: 'quark',
        accent: '#74c0fc',
        accent2: '#ff922b',
        premise: 'The visual emphasizes that the exposed components are not individually admissible as free stable identities.',
        simulation: 'Three fractional roles lower cost together, while pulling one outward increases closure strain.',
        mtt: 'Standard color is only an interpretive label here; the native story is admissibility of a composite, not isolated parts.',
        readouts: {
            kept: 'composite closure',
            dropped: 'isolated quark',
            result: 'bound triplet identity',
        },
        params: { capacity: .66, disturbance: .34, memory: .58, anchors: 3, branches: 3, gravity: .22, twist: .64, closure: .74 },
    },
    {
        id: 'ch-10-wz',
        chapter: '10',
        arc: 'Arc I',
        title: 'The W and Z Bosons: Identity Rewriting Itself',
        mode: 'particle',
        modeLabel: 'rewrite channel',
        variant: 'boson',
        accent: '#60a5fa',
        accent2: '#f472b6',
        premise: 'The W and Z chapter is shown as a rule that changes which exposed identity can continue.',
        simulation: 'A central rewrite channel redirects the carried trace, exchanging one admissible identity for another.',
        mtt: 'The standard weak boson labels are interpretive; the native mechanism is constrained identity rewriting.',
        readouts: {
            kept: 'allowed rewrite',
            dropped: 'fixed identity path',
            result: 'weak transition role',
        },
        params: { capacity: .63, disturbance: .36, memory: .48, anchors: 1, branches: 6, gravity: .12, twist: .7, closure: .64 },
    },
    {
        id: 'ch-11-higgs',
        chapter: '11',
        arc: 'Arc I',
        title: 'The Higgs: The Price of Persistence',
        mode: 'particle',
        modeLabel: 'persistence cost',
        variant: 'higgs',
        accent: '#f59e0b',
        accent2: '#7dd3fc',
        premise: 'The Higgs chapter is represented as the background cost of turning possible identity into persistent identity.',
        simulation: 'A field-like cost basin surrounds the identity rule; stronger anchoring increases the price paid for persistence.',
        mtt: 'This is not a Higgs calculation; it is the book-level bridge from persistence cost to mass-like behavior.',
        readouts: {
            kept: 'persistence price',
            dropped: 'free identity',
            result: 'mass-like cost',
        },
        params: { capacity: .7, disturbance: .3, memory: .66, anchors: 3, branches: 4, gravity: .34, twist: .38, closure: .76 },
    },
    {
        id: 'ch-12-elementary-composite',
        chapter: '12',
        arc: 'Arc I',
        title: 'Interlude: From Elementary to Composite Persistence',
        mode: 'relation',
        modeLabel: 'composition bridge',
        variant: 'interlude',
        accent: '#c4b5fd',
        accent2: '#86efac',
        premise: 'The interlude turns the early particle roles into a bridge toward composite persistence.',
        simulation: 'Stable anchors become nodes in an agreement graph, preparing the shift from isolated roles to compounds.',
        mtt: 'The native rule is that exposed identities can become cheaper when some history is shared or concealed.',
        readouts: {
            kept: 'composable roles',
            dropped: 'isolated-only view',
            result: 'bridge to composites',
        },
        params: { capacity: .68, disturbance: .26, memory: .6, anchors: 4, branches: 4, gravity: .18, twist: .32, closure: .74 },
    },
    {
        id: 'ch-16-atom',
        chapter: '16',
        arc: 'Arc I',
        title: 'The Atom: Remembering Charge and Identity Together',
        mode: 'particle',
        modeLabel: 'compound identity',
        variant: 'atom',
        accent: '#ff8787',
        accent2: '#69db7c',
        premise: 'The atom is shown as a stable compound projection where charge memory and identity memory coexist.',
        simulation: 'The nucleus is treated as a combined anchor while the electron appears as a probability-like cloud around it.',
        mtt: 'This keeps the proto-spinor philosophy: visible particles are stable anchors or clouds projected from richer structure.',
        readouts: {
            kept: 'charge plus identity',
            dropped: 'unresolved orbital detail',
            result: 'atom-like compound',
        },
        params: { capacity: .73, disturbance: .25, memory: .7, anchors: 3, branches: 4, gravity: .18, twist: .36, closure: .8 },
    },
    {
        id: 'ch-19-quantum',
        chapter: '19',
        arc: 'Arc I',
        title: 'Quantum Description: Deferred Commitment',
        mode: 'quantum',
        modeLabel: 'branch field',
        variant: 'none',
        accent: '#c084fc',
        accent2: '#22d3ee',
        premise: 'Quantum description is rendered as multiple admissible continuations before the interface forces a branch.',
        simulation: 'Branches remain live until a measurement aperture restricts which continuation can be carried forward.',
        mtt: 'The display separates spacetime footprint from the fuller shared state behind the projected description.',
        readouts: {
            kept: 'coherent alternatives',
            dropped: 'which-path excess',
            result: 'deferred commitment',
        },
        params: { capacity: .68, disturbance: .31, memory: .52, anchors: 1, branches: 7, gravity: .1, twist: .58, closure: .7 },
    },
    {
        id: 'ch-24-molecule',
        chapter: '24',
        arc: 'Arc I',
        title: 'The Molecule: Identity by Agreement',
        mode: 'relation',
        modeLabel: 'agreement graph',
        variant: 'none',
        accent: '#a7f3d0',
        accent2: '#fb7185',
        premise: 'A molecule appears where several identities agree to expose less than their isolated histories.',
        simulation: 'Agreement loops lower the exposed cost of the whole, so the compound becomes the reusable description.',
        mtt: 'Bond labels are interpretive; the native mechanism is shared closure that makes a composite projection cheaper.',
        readouts: {
            kept: 'shared constraints',
            dropped: 'separate histories',
            result: 'molecular agreement',
        },
        params: { capacity: .64, disturbance: .28, memory: .62, anchors: 5, branches: 5, gravity: .15, twist: .33, closure: .76 },
    },
    {
        id: 'ch-34-records',
        chapter: '34',
        arc: 'Arc I',
        title: 'Records: When Structure Can Be Reinstated',
        mode: 'relation',
        modeLabel: 'reinstatement',
        variant: 'record',
        accent: '#38bdf8',
        accent2: '#f59e0b',
        premise: 'A record is not perfect storage. It is enough structure to reliably rebuild a state when needed.',
        simulation: 'The loop carries a sparse key that can regenerate the visible pattern after disturbance.',
        mtt: 'The book bad-memory theme becomes constructive: persistence needs reinstatement, not infinite retention.',
        readouts: {
            kept: 'reinstatement key',
            dropped: 'full microstate',
            result: 'usable record',
        },
        params: { capacity: .6, disturbance: .42, memory: .74, anchors: 4, branches: 6, gravity: .12, twist: .22, closure: .68 },
    },
    {
        id: 'ch-37-life',
        chapter: '37',
        arc: 'Arc I',
        title: 'Life as a Regime, Not a Premise',
        mode: 'relation',
        modeLabel: 'maintenance loop',
        variant: 'life',
        accent: '#80ed99',
        accent2: '#f4a261',
        premise: 'Life is shown as a self-maintaining loop that spends energy to keep admissible organization available.',
        simulation: 'Inputs, gradients, repair, and reproduction close into a loop once passive persistence is not enough.',
        mtt: 'The simulation does not add life as a magic property; it shows the regime change where maintenance becomes required.',
        readouts: {
            kept: 'regulated loop',
            dropped: 'passive stability',
            result: 'living regime',
        },
        params: { capacity: .62, disturbance: .52, memory: .82, anchors: 6, branches: 5, gravity: .14, twist: .44, closure: .72 },
    },
    {
        id: 'ch-63-time',
        chapter: '63',
        arc: 'Arc II',
        title: 'Time as Ordered Sequence',
        mode: 'cosmos',
        modeLabel: 'ordered ledger',
        variant: 'time',
        accent: '#fbbf24',
        accent2: '#4ade80',
        premise: 'Time is presented as the order in which admissible updates can be reused without contradiction.',
        simulation: 'Each tick leaves a bounded residue, and later ticks inherit only what the sequence can still carry.',
        mtt: 'This matches the book setup: time is not merely motion, but ordered continuation under finite bookkeeping.',
        readouts: {
            kept: 'ordered residue',
            dropped: 'reversible excess',
            result: 'directional sequence',
        },
        params: { capacity: .66, disturbance: .36, memory: .46, anchors: 2, branches: 8, gravity: .28, twist: .22, closure: .66 },
    },
    {
        id: 'ch-65-gravity',
        chapter: '65',
        arc: 'Arc II',
        title: 'Gravity as Compatibility Geometry',
        mode: 'cosmos',
        modeLabel: 'elastic plane',
        variant: 'gravity',
        accent: '#60a5fa',
        accent2: '#f97316',
        premise: 'Gravity is represented as the geometry required for anchored structure to remain mutually compatible.',
        simulation: 'Anchors press into a compatibility plane; the plane relaxes, but repeated anchors establish a baseline.',
        mtt: 'This is deliberately the book/proto-spinor reading, not a replacement for GR field equations.',
        readouts: {
            kept: 'compatibility curvature',
            dropped: 'perfect local flatness',
            result: 'geometry from anchored cost',
        },
        params: { capacity: .72, disturbance: .3, memory: .64, anchors: 4, branches: 5, gravity: .72, twist: .2, closure: .74 },
    },
    {
        id: 'ch-70-proto-spinor',
        chapter: '70',
        arc: 'Arc II',
        title: 'The Proto-Spinor',
        mode: 'proto',
        modeLabel: 'inner construction',
        variant: 'none',
        accent: '#22c55e',
        accent2: '#e879f9',
        premise: 'The proto-spinor is treated as an internal construction candidate for how global closure becomes local projection.',
        simulation: 'Circle, nil gap, lens twist, and projected anchor are separated so the construction can be seen step by step.',
        mtt: 'This is the most MTT-native view in the companion: stable particles appear as projected closure residues.',
        readouts: {
            kept: 'closure residue',
            dropped: 'upper-world detail',
            result: 'stable anchor',
        },
        params: { capacity: .74, disturbance: .22, memory: .68, anchors: 2, branches: 4, gravity: .36, twist: .78, closure: .78 },
    },
    {
        id: 'ch-72-entanglement',
        chapter: '72',
        arc: 'Arc II',
        title: 'Entanglement as Shared State',
        mode: 'quantum',
        modeLabel: 'shared state',
        variant: 'none',
        accent: '#a78bfa',
        accent2: '#2dd4bf',
        premise: 'Entanglement is shown as one admissible joint description with two separated spacetime footprints.',
        simulation: 'The two visible outputs stay coupled because the carried state is shared before it is locally read out.',
        mtt: 'This follows the book locality distinction: spacetime propagation remains local while the description can be joint.',
        readouts: {
            kept: 'joint description',
            dropped: 'separable inventory',
            result: 'shared state',
        },
        params: { capacity: .67, disturbance: .26, memory: .72, anchors: 2, branches: 6, gravity: .08, twist: .66, closure: .73 },
    },
    {
        id: 'ch-92-bad-memory',
        chapter: '92',
        arc: 'Arc II',
        title: 'The Universe Has a Bad Memory',
        mode: 'cosmos',
        modeLabel: 'cosmic residue',
        variant: 'bad-memory',
        accent: '#fb7185',
        accent2: '#5eead4',
        premise: 'The closing chapter returns to the core thesis: stable law is what remains when the universe cannot remember everything.',
        simulation: 'A cosmic field repeatedly forgets over-specific history while preserving reusable anchors and transport rules.',
        mtt: 'The result is not emptiness after forgetting, but the reduced structure capable of being physics at all.',
        readouts: {
            kept: 'reusable physics',
            dropped: 'total history',
            result: 'bad memory, stable law',
        },
        params: { capacity: .6, disturbance: .48, memory: .44, anchors: 5, branches: 8, gravity: .46, twist: .48, closure: .68 },
    },
]

const activeIndex = ref(0)
const activeViewIndex = ref(0)
const capacity = ref(chapters[0].params.capacity)
const disturbance = ref(chapters[0].params.disturbance)
const reuse = ref(3)
const elapsed = ref(0)
const stageFrameRef = ref<HTMLElement | null>(null)
const stagePointer = ref({
    active: false,
    down: false,
    x: 210,
    y: 270,
    pulseX: 210,
    pulseY: 270,
    pulseAt: -99,
})

let frameId = 0

const activeChapter = computed(() => chapters[activeIndex.value])
const activeViewItems = computed(() => [
    {
        id: `${activeChapter.value.id}-chapter`,
        name: 'Chapter',
        shortLabel: 'C',
        kind: 'chapter',
    },
    ...(activeChapter.value.mechanisms ?? []),
])
const activeView = computed(() => activeViewItems.value[Math.min(activeViewIndex.value, activeViewItems.value.length - 1)])
const activeSceneKey = computed(() => activeView.value.id)
const phase = computed(() => elapsed.value * (.65 + reuse.value * .08))
const isOpeningLedgerScene = computed(() => {
    const chapterNumber = Number.parseInt(activeChapter.value.chapter, 10)
    return Number.isFinite(chapterNumber) && chapterNumber <= 12
})

const stageVars = computed(() => ({
    '--accent': 'accent' in activeView.value && activeView.value.accent ? activeView.value.accent : activeChapter.value.accent,
    '--accent2': 'accent2' in activeView.value && activeView.value.accent2 ? activeView.value.accent2 : activeChapter.value.accent2,
}))

const effectiveCapacity = computed(() => {
    return clamp((capacity.value * .72) + (activeChapter.value.params.capacity * .28) - disturbance.value * .08, .08, 1)
})

const effectiveMemory = computed(() => {
    return clamp(activeChapter.value.params.memory * (.72 + capacity.value * .28) - disturbance.value * .22 + reuse.value * .018, .08, 1)
})

const closureScore = computed(() => {
    const base = activeChapter.value.params.closure
    const reusePenalty = Math.max(0, reuse.value - 4) * .028
    return clamp(base * .48 + effectiveCapacity.value * .34 + effectiveMemory.value * .18 - disturbance.value * .2 - reusePenalty, .02, .98)
})

const chapterOnePointerVisible = computed(() => {
    return activeChapter.value.id === 'ch-01-admissible' && stagePointer.value.active
})

const pointerStrength = computed(() => {
    if (!chapterOnePointerVisible.value)
        return 0

    const centerBias = 1 - Math.min(1, Math.abs(stagePointer.value.x - 430) / 440)
    return clamp((stagePointer.value.down ? .95 : .52) + centerBias * .22, 0, 1)
})

const pulseStrength = computed(() => {
    if (activeChapter.value.id !== 'ch-01-admissible')
        return 0

    const age = elapsed.value - stagePointer.value.pulseAt
    return age < 0 ? 0 : clamp(1 - age / 1.15, 0, 1)
})

const pulseRadius = computed(() => {
    return 26 + (1 - pulseStrength.value) * 150
})

const activeConstraint = computed(() => {
    switch (activeChapter.value.variant) {
        case 'neutrino':
            return 'shared phase allowed; anchor residue near zero'
        case 'positron':
            return 'inverse identity plus identity -> exposed charge cancels'
        case 'muon':
        case 'tau':
            return 'closure cost exceeds durable identity threshold'
        case 'quark':
            return 'composite closure allowed; isolated role forbidden'
        case 'boson':
            return 'identity can continue only through a rewrite channel'
        case 'higgs':
            return 'persistence requires paid anchoring cost'
        case 'atom':
            return 'charge memory and identity memory must co-close'
        case 'interlude':
            return 'stable roles become composable ledgers'
        default:
            if (activeChapter.value.mode === 'admissibility')
                return 'locality + finiteness + reuse -> admissible description'
            if (activeChapter.value.mode === 'quantum')
                return 'branches remain valid until projection restricts continuation'
            if (activeChapter.value.mode === 'relation')
                return 'shared agreement lowers exposed history cost'
            if (activeChapter.value.mode === 'proto')
                return 'circle + nil gap + lens twist -> projected anchor'
            return 'global bookkeeping selects stable local realization'
    }
})

const activeObservable = computed(() => {
    switch (activeChapter.value.mode) {
        case 'admissibility':
            return 'which traces survive the finite projection gate'
        case 'particle':
            return 'anchor strength, rewrite cost, and exposed footprint'
        case 'quantum':
            return 'branch visibility before and after the aperture'
        case 'relation':
            return 'agreement links that survive repeated disturbance'
        case 'proto':
            return 'nil gap, lens twist, closure residue, and pressure'
        case 'cosmos':
            return 'history residue and compatibility geometry'
        default:
            return 'stable projected structure'
    }
})

const chapterOneMicroMarks = computed(() => {
    return Array.from({ length: 92 }, (_, index) => {
        const band = index % 11
        const layer = Math.floor(index / 11)
        const baseX = 70 + ((index * 53) % 260) + Math.sin(phase.value * .35 + index) * (2 + disturbance.value * 6)
        const baseY = 98 + ((layer * 43 + band * 17) % 344) + Math.cos(phase.value * .42 + index * .7) * (2 + disturbance.value * 7)
        const local = chapterOneInfluence(baseX, baseY, 150)
        const dx = baseX - stagePointer.value.x
        const dy = baseY - stagePointer.value.y
        const x = baseX + dx * local * .18
        const y = baseY + dy * local * .18
        const carried = (index % 7 === 0 || index % 13 === 0) && Math.abs(y - 270) < 146 + effectiveCapacity.value * 52

        return {
            key: `chapter-one-mark-${index}`,
            x,
            y,
            r: carried ? 3.8 + effectiveCapacity.value * 2 : 1.6 + (index % 4) * .7,
            fill: index % 5 === 0 ? 'rgba(255,255,255,.42)' : 'rgba(255,255,255,.26)',
            opacity: carried ? .86 : .16 + (1 - disturbance.value) * .22 + local * .28,
            carried,
        }
    })
})

const chapterOneStreams = computed(() => {
    return Array.from({ length: 26 }, (_, index) => {
        const row = index - 12.5
        const startY = 270 + row * 13 + Math.sin(phase.value * .5 + index) * 14 * disturbance.value
        const apertureY = 270 + row * 4.4 * effectiveCapacity.value
        const carried = Math.abs(row) < 4.2 + effectiveCapacity.value * 3.8 + pulseStrength.value * 1.4
        const local = chapterOneInfluence(222, startY, 190)
        const bend = Math.sin(index * 1.7) * 34 + (startY - stagePointer.value.y) * local * .32

        return {
            key: `chapter-one-stream-${index}`,
            carried,
            opacity: carried ? .62 + closureScore.value * .24 + local * .18 : .08 + (1 - disturbance.value) * .18 + local * .16,
            path: `M 62 ${startY} C 178 ${startY + bend} 280 ${apertureY - bend * .35} 430 ${apertureY}`,
        }
    })
})

const chapterOneFlowParticles = computed(() => {
    return Array.from({ length: 34 }, (_, index) => {
        const seed = index * 1.618
        const t = (phase.value * (.08 + (index % 5) * .012) + index * .071) % 1
        const curve = Math.sin((t + seed) * Math.PI)
        const startY = 96 + ((index * 61) % 350)
        const targetY = 270 + (((index % 13) - 6) * 6.5 * effectiveCapacity.value)
        const x = 70 + t * 650
        const rawY = startY * (1 - t) + targetY * t + Math.sin(seed + phase.value * .9) * (1 - t) * (12 + disturbance.value * 20) + curve * ((index % 2 === 0 ? -1 : 1) * 18)
        const local = chapterOneInfluence(x, rawY, 128)
        const y = rawY + (rawY - stagePointer.value.y) * local * .22
        const carried = Math.abs(targetY - 270) < 58 + effectiveCapacity.value * 28 + pulseStrength.value * 24
        const pastGate = x > 474

        return {
            key: `chapter-one-flow-${index}`,
            x: pastGate ? x : Math.min(x, 426 + Math.sin(seed) * 8),
            y: pastGate ? y * .28 + (270 + Math.sin(seed) * 22) * .72 : y,
            r: carried ? 2.8 + closureScore.value * 2.2 : 1.6,
            opacity: carried ? .22 + closureScore.value * .62 + local * .18 : .1 + (1 - t) * .25 + local * .28,
            carried,
        }
    })
})

const chapterOneSamples = computed(() => {
    return Array.from({ length: 5 }, (_, index) => {
        const offset = index - 2
        return {
            key: `chapter-one-sample-${index}`,
            y: 270 + offset * 54 + Math.sin(phase.value + index) * 3,
            r: 12 + effectiveCapacity.value * 10 - Math.abs(offset) * 2,
            width: 1.5 + closureScore.value * 2,
        }
    })
})

const chapterOneScanY = computed(() => {
    const autonomous = 104 + ((Math.sin(phase.value * .74) + 1) / 2) * 298
    const target = clamp(stagePointer.value.y - 17, 104, 402)
    return chapterOnePointerVisible.value ? autonomous * .38 + target * .62 : autonomous
})

const chapterOneCarriedThreads = computed(() => {
    return Array.from({ length: 12 }, (_, index) => {
        const row = index - 5.5
        const sourceY = 270 + row * 10 * effectiveCapacity.value
        const pulsePull = pulseStrength.value * Math.sin(index * 1.7 + phase.value) * 10
        const outputY = 270 + row * 3.4 * closureScore.value + pulsePull
        return {
            key: `chapter-one-carried-${index}`,
            opacity: .4 + closureScore.value * .46 - Math.abs(row) * .025 + pulseStrength.value * .18,
            width: 1.4 + closureScore.value * 1.6 + pulseStrength.value * 1.2,
            path: `M 476 ${sourceY} C 550 ${sourceY + row * 9} 610 ${outputY - row * 6} 706 ${outputY}`,
        }
    })
})

const chapterOneSatellites = computed(() => {
    return Array.from({ length: 10 }, (_, index) => {
        const angle = phase.value * (.36 + index * .006) + index * Math.PI * .2
        const radius = 34 + (index % 5) * 16 + pulseStrength.value * 18
        const squash = .58 + (index % 3) * .08

        return {
            key: `chapter-one-satellite-${index}`,
            x: Math.cos(angle) * radius,
            y: Math.sin(angle) * radius * squash,
            r: index % 4 === 0 ? 3.8 : 2.4,
            opacity: .42 + closureScore.value * .36 - (index % 5) * .035 + pulseStrength.value * .18,
        }
    })
})

const chapterOneEchoes = computed(() => {
    return Array.from({ length: 7 }, (_, index) => {
        return {
            key: `chapter-one-echo-${index}`,
            r: 34 + index * 16 + Math.sin(phase.value * .7 + index) * (index % 2 === 0 ? 2.5 : 1.2),
            width: index === 2 ? 4 : 1.6,
            opacity: index === 2 ? .92 : .16 + Math.max(0, .5 - Math.abs(index - 3) * .08),
            primary: index === 2,
        }
    })
})

const chapterOneAliases = computed(() => {
    return Array.from({ length: 7 }, (_, index) => {
        const y = 112 + index * 52
        const amplitude = 16 + disturbance.value * 26
        return {
            key: `chapter-one-alias-${index}`,
            width: 1 + (index % 2) * .8,
            path: `M 510 ${y} C 554 ${y - amplitude} 602 ${y + amplitude} 648 ${y} S 742 ${y - amplitude} 786 ${y}`,
        }
    })
})

const chapterOneStableGlyph = computed(() => {
    const pulse = Math.sin(phase.value * .85) * 3 + pulseStrength.value * 10
    return `M ${-58 - pulse} 0
        C ${-44} ${-42 - pulse} ${4} ${-58} ${38 + pulse} ${-30}
        C ${72} ${-2} ${52} ${44 + pulse} ${4} ${54}
        C ${-44} ${44 + pulse} ${-72} ${14} ${-58 - pulse} 0 Z`
})

const ledgerPlateGrain = computed(() => {
    const palette = ['#f8ffff', '#55f8ff', '#ff51e8', '#9dffea']
    return Array.from({ length: 360 }, (_, index) => {
        const baseX = (index * 197) % 920
        const baseY = (index * 389) % 540
        const shimmer = Math.sin(phase.value * (1.7 + (index % 9) * .13) + index)
        const local = chapterOneInfluence(baseX, baseY, 170)
        const driftX = Math.sin(index * 1.21 + phase.value * .33) * (1.2 + local * 4)
        const driftY = Math.cos(index * .91 - phase.value * .27) * (1.2 + local * 4)

        return {
            key: `ledger-grain-${index}`,
            x: baseX + driftX,
            y: baseY + driftY,
            r: .45 + (index % 5) * .18 + local * .9,
            fill: palette[index % palette.length],
            opacity: .08 + Math.max(0, shimmer) * .14 + local * .2 + (isOpeningLedgerScene.value ? .04 : 0),
        }
    })
})

const ledgerScanBands = computed(() => {
    return Array.from({ length: 9 }, (_, index) => {
        const y = 54 + index * 58 + Math.sin(phase.value * .45 + index) * 10
        const jitter = Math.sin(phase.value * 1.7 + index * 2.2) * 18
        const color = index % 3 === 0 ? '#ffffff' : index % 3 === 1 ? '#56f6ff' : '#ff51e8'
        return {
            key: `ledger-scan-${index}`,
            path: `M 0 ${y} C 156 ${y + jitter} 280 ${y - jitter * .5} 438 ${y} S 720 ${y + jitter * .4} 920 ${y - jitter * .2}`,
            stroke: color,
            width: index % 3 === 0 ? .9 : .55,
            opacity: .045 + (index % 4) * .012 + pulseStrength.value * .025,
        }
    })
})

const ledgerMeshEdges = computed(() => {
    const edges: Array<{ key: string, path: string, hot: boolean, width: number, opacity: number }> = []
    const cols = 11
    const rows = 7

    for (let row = 0; row < rows; row += 1) {
        for (let col = 0; col < cols; col += 1) {
            if (col < cols - 1)
                edges.push(makeLedgerEdge(row, col, row, col + 1, `h-${row}-${col}`))
            if (row < rows - 1)
                edges.push(makeLedgerEdge(row, col, row + 1, col, `v-${row}-${col}`))
            if (row < rows - 1 && col < cols - 1 && (row + col) % 2 === 0)
                edges.push(makeLedgerEdge(row, col, row + 1, col + 1, `d-${row}-${col}`))
        }
    }

    return edges
})

const ledgerBasinRings = computed(() => {
    return Array.from({ length: 7 }, (_, index) => {
        const focus = activeSceneKey.value === 'ch-01-sampling' ? { x: 456, y: 270 } : { x: 462, y: 270 }
        const pulse = pulseStrength.value * 18
        return {
            key: `ledger-basin-ring-${index}`,
            x: focus.x,
            y: focus.y + index * 2,
            rx: 28 + index * 20 + pulse * .45,
            ry: 10 + index * 7 + pulse * .18,
            primary: index === 2,
            width: index === 2 ? 3.2 : 1.3,
            opacity: index === 2 ? .56 + pulseStrength.value * .28 : .13 + (6 - index) * .025,
        }
    })
})

const bellRegions = computed(() => {
    return [
        makeBellRegion('left', 260, 270, 122),
        makeBellRegion('right', 660, 270, 122),
    ]
})

const bellSharedFields = computed(() => {
    return Array.from({ length: 9 }, (_, index) => {
        const row = index - 4
        const wobbleAmount = Math.sin(phase.value * .52 + index) * 16
        const y = 270 + row * 18
        const primary = index === 4

        return {
            key: `bell-field-${index}`,
            primary,
            width: primary ? 4 : 1.5,
            opacity: primary ? .7 + pulseStrength.value * .22 : .12 + effectiveMemory.value * .22,
            path: `M 150 ${y + wobbleAmount} C 288 ${y - 82 - wobbleAmount} 410 ${y + 92} 460 ${y} C 510 ${y - 92} 636 ${y + 82 + wobbleAmount} 770 ${y - wobbleAmount}`,
        }
    })
})

const bellJointStatePath = computed(() => {
    const pulse = pulseStrength.value * 34
    return `M 288 ${270 - 54 - pulse * .25}
        C 382 ${206 - pulse} 540 ${206 - pulse} 632 ${270 - 54 - pulse * .25}
        C 548 ${334 + pulse} 376 ${334 + pulse} 288 ${270 + 54 + pulse * .25}
        C 358 ${292} 562 ${292} 632 ${270 + 54 + pulse * .25}
        C 540 ${234 - pulse * .35} 382 ${234 - pulse * .35} 288 ${270 - 54 - pulse * .25} Z`
})

const samplingApertureX = computed(() => {
    return chapterOnePointerVisible.value ? clamp(stagePointer.value.x - 9, 92, 810) : 452 + Math.sin(phase.value * .42) * 260
})

const samplingRawWaves = computed(() => {
    return Array.from({ length: 5 }, (_, index) => {
        const primary = index === 2
        const frequency = 1.2 + index * .7 + disturbance.value * 1.4
        const amplitude = 30 + index * 12 + pulseStrength.value * 20
        const offset = (index - 2) * 20
        return {
            key: `sampling-wave-${index}`,
            primary,
            width: primary ? 3.4 : 1.4,
            opacity: primary ? .78 : .14 + (1 - disturbance.value) * .2,
            path: buildWavePath(70, 846, 270 + offset, amplitude, frequency, phase.value * (.7 + index * .12)),
        }
    })
})

const samplingPoints = computed(() => {
    const step = 58 + (1 - effectiveCapacity.value) * 36
    const start = 112 + (Math.sin(phase.value * .3) + 1) * 14
    const count = 12

    return Array.from({ length: count }, (_, index) => {
        const x = start + index * step
        const y = sampleSignalY(x)
        const valid = index % 3 !== 1 || effectiveCapacity.value > .6
        const local = chapterOneInfluence(x, y, 115)
        return {
            key: `sampling-point-${index}`,
            x,
            y,
            r: valid ? 5 + local * 4 : 3,
            opacity: valid ? .62 + closureScore.value * .3 + local * .2 : .22,
            valid,
        }
    }).filter(sample => sample.x < 850)
})

const samplingReconstructionPath = computed(() => {
    const points = samplingPoints.value.filter(point => point.valid)
    if (!points.length)
        return ''

    return points.reduce((path, point, index) => {
        if (index === 0)
            return `M ${point.x} ${point.y}`
        const previous = points[index - 1]
        const midX = (previous.x + point.x) / 2
        return `${path} C ${midX} ${previous.y} ${midX} ${point.y} ${point.x} ${point.y}`
    }, '')
})

const samplingAliasPath = computed(() => {
    return buildWavePath(70, 846, 270, 96 - effectiveCapacity.value * 50 + disturbance.value * 22, .55 + disturbance.value * .7, -phase.value * .24)
})

const gateX = 392
const gateHeight = computed(() => 86 + effectiveCapacity.value * 280)
const projectionRadius = computed(() => 44 + closureScore.value * 78)
const measurementShift = computed(() => (disturbance.value - .5) * 54)
const twistDegrees = computed(() => activeChapter.value.params.twist * 180 + Math.sin(phase.value * .8) * 18)

const backdropLanes = computed(() => {
    return Array.from({ length: 5 }, (_, i) => {
        const y = 120 + i * 76
        const offset = Math.sin(phase.value * .4 + i) * 12
        return {
            key: `lane-${i}`,
            width: i === 2 ? 1.8 : 1,
            path: `M 40 ${y + offset} C 220 ${y - 38} 320 ${y + 52} 468 ${y + offset} S 744 ${y - 44} 884 ${y + offset * .4}`,
        }
    })
})

const memoryTraces = computed(() => {
    const count = 18
    const carriedCount = Math.round(count * effectiveCapacity.value)

    return Array.from({ length: count }, (_, i) => {
        const row = i - (count - 1) / 2
        const startX = 72 + (i % 3) * 24
        const startY = 270 + row * 17 + Math.sin(phase.value * .7 + i) * (5 + disturbance.value * 10)
        const gateY = 270 + row * 7 * effectiveCapacity.value
        const outY = 270 + row * 4 * closureScore.value
        const carried = Math.abs(row) <= carriedCount / 2
        return {
            key: `trace-${i}`,
            startX,
            startY,
            carried,
            opacity: carried ? .52 + closureScore.value * .42 : .12 + (1 - disturbance.value) * .16,
            rawPath: `M ${startX} ${startY} C 210 ${startY - row * 3} 285 ${gateY} ${gateX} ${gateY}`,
            outPath: `M ${gateX + 34} ${gateY} C 500 ${gateY} 594 ${outY} 700 ${outY}`,
        }
    })
})

const carriedTraces = computed(() => memoryTraces.value.filter(trace => trace.carried))

const transportWaves = computed(() => {
    return Array.from({ length: 6 }, (_, i) => {
        const y = 210 + i * 24
        const spread = 18 + i * 8 + Math.sin(phase.value + i) * 6
        return {
            key: `transport-${i}`,
            width: 1.4 + i * .28,
            opacity: .28 + (6 - i) * .08,
            path: `M 338 ${y} C 390 ${y - spread} 445 ${y + spread} 512 ${y} S 620 ${y - spread} 672 ${y}`,
        }
    })
})

const identityNeedlePath = computed(() => {
    const swing = Math.sin(phase.value) * (18 + disturbance.value * 30)
    return `M 720 270 L ${720 + Math.cos(swing * Math.PI / 180) * 74} ${270 + Math.sin(swing * Math.PI / 180) * 74}`
})

const branchPaths = computed(() => {
    const count = Math.max(4, activeChapter.value.params.branches)
    const selected = Math.floor(count / 2)

    return Array.from({ length: count }, (_, i) => {
        const row = i - (count - 1) / 2
        const midY = 270 + row * (28 + disturbance.value * 20)
        const endY = 270 + row * (14 + (1 - closureScore.value) * 26)
        const isSelected = Math.abs(i - selected) <= (activeChapter.value.id === 'ch-72-entanglement' ? 1 : 0)
        return {
            key: `branch-${i}`,
            selected: isSelected || i === selected,
            opacity: isSelected || i === selected ? .95 : .18 + effectiveMemory.value * .24,
            path: `M 138 270 C 268 ${270 + row * 12} 344 ${midY} 448 ${midY} S 600 ${endY} 688 ${endY}`,
        }
    })
})

const relationNodes = computed(() => {
    const count = Math.max(4, activeChapter.value.params.anchors)
    return Array.from({ length: count }, (_, i) => {
        const angle = (Math.PI * 2 * i / count) + phase.value * .12
        const radius = 86 + Math.sin(phase.value + i) * 9
        return {
            key: `node-${i}`,
            x: 204 + Math.cos(angle) * radius,
            y: 270 + Math.sin(angle) * radius * .72,
            r: 15 + (i % 3) * 3,
        }
    })
})

const relationEdges = computed(() => {
    const nodes = relationNodes.value
    return nodes.map((node, i) => {
        const next = nodes[(i + 1) % nodes.length]
        const lift = 32 + effectiveMemory.value * 26
        return {
            key: `edge-${i}`,
            width: 2 + closureScore.value * 3,
            path: `M ${node.x} ${node.y} C ${(node.x + next.x) / 2} ${(node.y + next.y) / 2 - lift} ${next.x} ${next.y} ${next.x} ${next.y}`,
        }
    })
})

const loopPath = computed(() => {
    const pulse = Math.sin(phase.value) * 18
    return `M 358 ${270 + pulse} C 414 166 546 168 596 270 C 548 374 414 374 358 ${270 + pulse}`
})

const nilGapPath = computed(() => {
    const gap = 48 + activeChapter.value.params.twist * 70 + Math.sin(phase.value) * 18
    return `M 312 ${270 - gap / 2} C 350 ${250 - gap * .2} 376 ${250 + gap * .2} 410 ${270 + gap / 2}`
})

const cosmicPlanePath = computed(() => {
    const gravity = activeChapter.value.params.gravity + disturbance.value * .28
    const dip = gravity * 96
    const relaxation = (1 - effectiveMemory.value) * 28
    return `M 58 318 C 164 ${300 + relaxation} 242 ${306} 326 ${318}
        C 402 ${330 + dip * .45} 486 ${330 + dip} 560 ${318}
        C 654 ${300 + relaxation} 760 ${286 + relaxation} 858 310
        L 858 396 C 700 374 578 414 456 386 C 324 356 214 374 58 390 Z`
})

const gravityWells = computed(() => {
    const count = Math.max(3, activeChapter.value.params.anchors)
    return Array.from({ length: count }, (_, i) => ({
        key: `well-${i}`,
        x: 190 + i * (520 / Math.max(1, count - 1)),
        y: 265 + Math.sin(phase.value * .5 + i) * 22 + (i % 2) * 24,
        r: 10 + activeChapter.value.params.gravity * 18 + (i % 3) * 3,
        opacity: .42 + i / count * .34,
    }))
})

const cosmicArcs = computed(() => {
    const count = Math.max(5, activeChapter.value.params.branches)
    return Array.from({ length: count }, (_, i) => {
        const x = 96 + i * 92
        const height = 52 + Math.sin(phase.value * .4 + i) * 20
        return {
            key: `cosmic-${i}`,
            width: i % 3 === 0 ? 2.8 : 1.5,
            path: `M ${x} 210 C ${x + 26} ${160 - height * .35} ${x + 78} ${160 + height * .35} ${x + 104} 210`,
        }
    })
})

watch(activeIndex, (index) => {
    activeViewIndex.value = 0
    capacity.value = chapters[index].params.capacity
    disturbance.value = chapters[index].params.disturbance
    reuse.value = chapters[index].mode === 'relation' ? 5 : 3
})

onMounted(() => {
    const animate = (time: number) => {
        elapsed.value = time / 1000
        frameId = window.requestAnimationFrame(animate)
    }

    frameId = window.requestAnimationFrame(animate)
})

onBeforeUnmount(() => {
    window.cancelAnimationFrame(frameId)
})

function handleStagePointer(event: PointerEvent) {
    const frame = stageFrameRef.value
    if (!frame)
        return

    const rect = frame.getBoundingClientRect()
    const x = clamp(((event.clientX - rect.left) / rect.width) * 920, 0, 920)
    const y = clamp(((event.clientY - rect.top) / rect.height) * 540, 0, 540)
    stagePointer.value = {
        ...stagePointer.value,
        active: true,
        x,
        y,
    }
}

function triggerStagePulse(event: PointerEvent) {
    handleStagePointer(event)
    stagePointer.value = {
        ...stagePointer.value,
        down: true,
        pulseX: stagePointer.value.x,
        pulseY: stagePointer.value.y,
        pulseAt: elapsed.value,
    }
    ;(event.currentTarget as HTMLElement).setPointerCapture?.(event.pointerId)
}

function releaseStagePointer(event: PointerEvent) {
    stagePointer.value = {
        ...stagePointer.value,
        down: false,
    }
    ;(event.currentTarget as HTMLElement).releasePointerCapture?.(event.pointerId)
}

function clearStagePointer() {
    stagePointer.value = {
        ...stagePointer.value,
        active: false,
        down: false,
    }
}

function chapterOneInfluence(x: number, y: number, radius = 140) {
    if (!isOpeningLedgerScene.value)
        return 0

    const dx = x - stagePointer.value.x
    const dy = y - stagePointer.value.y
    const pointerDistance = Math.sqrt(dx * dx + dy * dy)
    const pointer = chapterOnePointerVisible.value ? clamp(1 - pointerDistance / radius, 0, 1) * pointerStrength.value : 0

    const px = x - stagePointer.value.pulseX
    const py = y - stagePointer.value.pulseY
    const pulseDistance = Math.sqrt(px * px + py * py)
    const pulse = clamp(1 - pulseDistance / (radius * 1.35), 0, 1) * pulseStrength.value

    return clamp(pointer + pulse, 0, 1)
}

function makeBellRegion(key: string, x: number, y: number, r: number) {
    const local = chapterOneInfluence(x, y, 210)
    const active = local > .08
    const beables = Array.from({ length: 18 }, (_, index) => {
        const angle = index * Math.PI * .62 + phase.value * (.12 + index * .004)
        const radius = 18 + ((index * 29) % 82)
        const localBeable = index % 4 !== 1
        return {
            key: `${key}-beable-${index}`,
            x: Math.cos(angle) * radius + Math.sin(index * 2.3) * local * 10,
            y: Math.sin(angle) * radius * .72 + Math.cos(index * 1.7) * local * 10,
            r: localBeable ? 3.2 + local * 2.4 : 2,
            opacity: localBeable ? .48 + effectiveCapacity.value * .32 + local * .2 : .18,
            local: localBeable,
        }
    })

    return {
        key,
        x,
        y,
        r: r + local * 10 + pulseStrength.value * 6,
        active,
        beables,
    }
}

function makeLedgerEdge(rowA: number, colA: number, rowB: number, colB: number, key: string) {
    const a = ledgerPoint(rowA, colA)
    const b = ledgerPoint(rowB, colB)
    const midX = (a.x + b.x) / 2
    const midY = (a.y + b.y) / 2
    const local = chapterOneInfluence(midX, midY, 170)
    const hot = local > .05 || Math.abs(midX - 462) < 100 && Math.abs(midY - 270) < 96

    return {
        key: `ledger-${key}`,
        path: `M ${a.x} ${a.y} L ${b.x} ${b.y}`,
        hot,
        width: hot ? 1.2 + local * 1.4 : .75,
        opacity: hot ? .22 + local * .32 + pulseStrength.value * .16 : .12,
    }
}

function ledgerPoint(row: number, col: number) {
    const baseX = 72 + col * 78
    const baseY = 112 + row * 52
    const jitterX = Math.sin(row * 2.1 + col * 1.3 + phase.value * .14) * 9
    const jitterY = Math.cos(row * 1.4 - col * 1.8 + phase.value * .16) * 8
    const centerX = activeSceneKey.value === 'ch-01-sampling' ? 456 : 462
    const centerY = 270
    const dx = baseX - centerX
    const dy = baseY - centerY
    const dist = Math.sqrt(dx * dx + dy * dy)
    const sink = clamp(1 - dist / 330, 0, 1)
    const interaction = chapterOneInfluence(baseX, baseY, 210)
    const pull = sink * (34 + pulseStrength.value * 34) + interaction * 28

    return {
        x: baseX + jitterX - dx * pull / 420,
        y: baseY + jitterY - dy * pull / 520 + sink * sink * 28,
    }
}

function buildWavePath(startX: number, endX: number, centerY: number, amplitude: number, frequency: number, offset = 0) {
    const steps = 34
    let path = ''

    for (let index = 0; index <= steps; index += 1) {
        const t = index / steps
        const x = startX + (endX - startX) * t
        const y = centerY
            + Math.sin(t * Math.PI * 2 * frequency + offset) * amplitude
            + Math.sin(t * Math.PI * 2 * (frequency * .37 + .5) - offset * .6) * amplitude * .22
        path += index === 0 ? `M ${x} ${y}` : ` L ${x} ${y}`
    }

    return path
}

function sampleSignalY(x: number) {
    const t = (x - 70) / 776
    const local = chapterOneInfluence(x, 270, 132)
    return 270
        + Math.sin(t * Math.PI * 2 * (2.1 + disturbance.value * 1.6) + phase.value * .7) * (54 + pulseStrength.value * 20)
        + Math.sin(t * Math.PI * 2 * .8 - phase.value * .45) * (18 + local * 22)
}

function percent(value: number) {
    return `${Math.round(value * 100)}%`
}

function clamp(value: number, min: number, max: number) {
    return Math.min(max, Math.max(min, value))
}

function wobble(seed: number, amount: number) {
    return Math.sin(phase.value + seed) * amount * disturbance.value
}

function orbitPath(cx: number, cy: number, rx: number, rotate: number) {
    return `M ${cx - rx} ${cy} A ${rx} ${Math.max(8, rx * .38)} ${rotate} 1 0 ${cx + rx} ${cy} A ${rx} ${Math.max(8, rx * .38)} ${rotate} 1 0 ${cx - rx} ${cy}`
}
</script>

<style scoped lang="scss">
.book-companion {
    min-height: 100vh;
    background:
        linear-gradient(180deg, rgba(17, 18, 15, .98), rgba(9, 10, 9, 1) 52%, rgba(16, 15, 13, 1)),
        #0e0f0c;
    color: #f5f5f1;
    padding: 28px;
}

.anchor-only {
    display: flex;
    flex-direction: column;
    gap: 14px;
    background:
        radial-gradient(circle at 22% 26%, rgba(100, 223, 223, .08), transparent 34%),
        radial-gradient(circle at 78% 54%, rgba(255, 209, 102, .07), transparent 36%),
        linear-gradient(180deg, #11120f, #070807 64%, #0f100d);
}

.anchor-only .rail-header,
.anchor-only .chapter-copy,
.anchor-only .control-panel,
.anchor-only .explain-panel,
.anchor-only .stage-heading,
.anchor-only .instrument-strip,
.anchor-only .svg-label,
.anchor-only .svg-note,
.anchor-only .svg-micro {
    display: none;
}

.anchor-only .chapter-rail {
    width: min(100%, 1280px);
    margin: 0 auto;
}

.anchor-only .chapter-grid {
    display: flex;
    max-height: none;
    overflow-x: auto;
    gap: 8px;
    padding: 2px 2px 10px;
    scrollbar-width: thin;
}

.anchor-only .chapter-button {
    justify-content: center;
    flex: 0 0 auto;
    min-width: 48px;
    min-height: 48px;
    padding: 5px;
    background: rgba(255, 255, 255, .035);
}

.anchor-only .chapter-button.active {
    box-shadow: 0 0 28px color-mix(in srgb, var(--accent) 22%, transparent);
}

.anchor-only .chapter-number {
    width: 38px;
    height: 38px;
    font-size: 13px;
}

.view-rail {
    display: flex;
    justify-content: center;
    gap: 8px;
    width: min(100%, 1280px);
    margin: -6px auto 0;
}

.view-button {
    display: grid;
    place-items: center;
    width: 46px;
    height: 34px;
    border: 1px solid rgba(255, 255, 255, .12);
    border-radius: 8px;
    background: rgba(255, 255, 255, .035);
    color: rgba(245, 245, 241, .64);
    font-size: 11px;
    font-weight: 900;
    transition: border-color .18s ease, background .18s ease, color .18s ease, transform .18s ease;
}

.view-button:hover,
.view-button.active {
    border-color: var(--accent2);
    background: rgba(255, 255, 255, .075);
    color: #fff;
}

.view-button.active {
    transform: translateY(-1px);
    box-shadow: 0 0 20px color-mix(in srgb, var(--accent2) 18%, transparent);
}

.anchor-only .sim-layout {
    display: block;
    width: min(100%, 1480px);
    max-width: 1480px;
    margin: 0 auto;
}

.anchor-only .stage-panel {
    border-color: rgba(255, 255, 255, .13);
    background:
        linear-gradient(180deg, rgba(255, 255, 255, .055), rgba(255, 255, 255, .025)),
        rgba(0, 0, 0, .16);
    box-shadow: 0 24px 80px rgba(0, 0, 0, .42);
}

.anchor-only .stage-frame {
    aspect-ratio: 16 / 9;
    border-top: 0;
    background: #000;
    cursor: crosshair;
    filter: contrast(1.18) saturate(.92);
    touch-action: none;
    user-select: none;
}

.anchor-only .axis-overlay {
    display: none;
}

.anchor-only .stage-frame svg {
    background: #000;
}

.ledger-plate-grain {
    mix-blend-mode: screen;
}

.chapter-rail {
    max-width: 1560px;
    margin: 0 auto 18px;
}

.rail-header,
.stage-heading,
.panel-title {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 16px;
}

.rail-header {
    margin-bottom: 16px;
}

.rail-meta {
    display: flex;
    align-items: center;
    justify-content: flex-end;
    flex-wrap: wrap;
    gap: 8px;
}

.eyebrow {
    margin: 0 0 6px;
    color: rgba(245, 245, 241, .58);
    font-size: 12px;
    font-weight: 700;
    text-transform: uppercase;
}

h1,
h2 {
    margin: 0;
    letter-spacing: 0;
}

h1 {
    font-size: clamp(28px, 4vw, 48px);
    line-height: 1.02;
}

h2 {
    font-size: clamp(22px, 2.6vw, 34px);
    line-height: 1.08;
}

.edition-chip {
    border: 1px solid rgba(255, 255, 255, .14);
    border-radius: 8px;
    color: rgba(245, 245, 241, .74);
    font-size: 12px;
    font-weight: 700;
    padding: 8px 10px;
    white-space: nowrap;
}

.chapter-grid {
    display: grid;
    grid-template-columns: repeat(6, minmax(0, 1fr));
    gap: 8px;
    max-height: 246px;
    overflow: auto;
    padding-right: 4px;
    scrollbar-color: var(--accent) rgba(255, 255, 255, .08);
}

.chapter-button {
    display: flex;
    align-items: center;
    gap: 10px;
    min-height: 68px;
    border: 1px solid rgba(255, 255, 255, .1);
    border-radius: 8px;
    background: rgba(255, 255, 255, .045);
    color: inherit;
    padding: 10px;
    text-align: left;
    transition: border-color .18s ease, background .18s ease, transform .18s ease;
}

.chapter-button:hover,
.chapter-button.active {
    border-color: var(--accent);
    background: rgba(255, 255, 255, .078);
}

.chapter-button.active {
    transform: translateY(-1px);
}

.chapter-number {
    display: grid;
    place-items: center;
    flex: 0 0 auto;
    width: 36px;
    height: 36px;
    border-radius: 8px;
    background: var(--accent);
    color: #0d0e0b;
    font-weight: 900;
}

.chapter-copy {
    display: grid;
    gap: 3px;
    min-width: 0;
}

.chapter-copy span {
    overflow: hidden;
    font-size: 13px;
    font-weight: 800;
    line-height: 1.2;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.chapter-copy small {
    overflow: hidden;
    color: rgba(245, 245, 241, .52);
    font-size: 11px;
    font-weight: 700;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.sim-layout {
    display: grid;
    grid-template-columns: minmax(220px, 280px) minmax(520px, 1fr) minmax(250px, 330px);
    gap: 14px;
    max-width: 1560px;
    margin: 0 auto;
}

.control-panel,
.explain-panel,
.stage-panel {
    border: 1px solid rgba(255, 255, 255, .1);
    border-radius: 8px;
    background: rgba(255, 255, 255, .052);
}

.control-panel,
.explain-panel {
    align-self: start;
    padding: 16px;
}

.stage-panel {
    overflow: hidden;
    min-width: 0;
}

.stage-heading {
    padding: 18px 18px 12px;
}

.instrument-strip {
    display: grid;
    grid-template-columns: 1.15fr 1fr .9fr;
    gap: 8px;
    border-top: 1px solid rgba(255, 255, 255, .08);
    padding: 0 18px 14px;
}

.instrument-strip div {
    display: grid;
    gap: 4px;
    border: 1px solid rgba(255, 255, 255, .09);
    border-radius: 8px;
    background: rgba(0, 0, 0, .18);
    padding: 10px;
}

.instrument-strip span {
    color: rgba(245, 245, 241, .5);
    font-size: 10px;
    font-weight: 900;
    text-transform: uppercase;
}

.instrument-strip strong {
    color: rgba(245, 245, 241, .9);
    font-size: 12px;
    line-height: 1.28;
}

.mode-icon {
    display: grid;
    place-items: center;
    width: 48px;
    height: 48px;
    border: 1px solid rgba(255, 255, 255, .14);
    border-radius: 8px;
    color: var(--accent);
    font-size: 28px;
}

.stage-frame {
    aspect-ratio: 920 / 540;
    border-top: 1px solid rgba(255, 255, 255, .08);
    background: #11120f;
}

.stage-frame svg {
    display: block;
    width: 100%;
    height: 100%;
}

.panel-title {
    justify-content: flex-start;
    margin-bottom: 16px;
    color: var(--accent);
    font-weight: 900;
}

.panel-title span:first-child {
    font-size: 20px;
}

.range-row {
    display: grid;
    grid-template-columns: 1fr;
    gap: 8px;
    margin-bottom: 18px;
    color: rgba(245, 245, 241, .72);
    font-size: 12px;
    font-weight: 800;
    text-transform: uppercase;
}

.range-row input {
    accent-color: var(--accent);
    width: 100%;
}

.range-row strong {
    color: #fff;
    font-size: 14px;
}

.readout-list {
    display: grid;
    gap: 8px;
    margin-top: 18px;
}

.readout-list div,
.claim-block {
    display: grid;
    gap: 5px;
    border: 1px solid rgba(255, 255, 255, .09);
    border-radius: 8px;
    background: rgba(0, 0, 0, .16);
    padding: 11px;
}

.readout-list span,
.claim-block span {
    color: rgba(245, 245, 241, .52);
    font-size: 11px;
    font-weight: 800;
    text-transform: uppercase;
}

.readout-list strong,
.claim-block strong {
    color: #fff;
    font-size: 14px;
    line-height: 1.35;
}

.explain-panel {
    display: grid;
    gap: 12px;
}

.explain-panel p {
    margin: 0;
    color: rgba(245, 245, 241, .76);
    font-size: 14px;
    line-height: 1.55;
}

.svg-label,
.svg-note {
    fill: rgba(245, 245, 241, .72);
    font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 18px;
    font-weight: 800;
    letter-spacing: 0;
}

.svg-note {
    fill: rgba(245, 245, 241, .82);
    font-size: 17px;
}

.svg-micro {
    fill: rgba(245, 245, 241, .38);
    font-family: ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    font-size: 12px;
    font-weight: 800;
    letter-spacing: 0;
    text-transform: uppercase;
}

@media (max-width: 1180px) {
    .chapter-grid {
        grid-template-columns: repeat(3, minmax(0, 1fr));
    }

    .sim-layout {
        grid-template-columns: 1fr;
    }

    .control-panel {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 12px;
    }

    .control-panel .panel-title,
    .readout-list {
        grid-column: 1 / -1;
    }

    .readout-list {
        grid-template-columns: repeat(4, minmax(0, 1fr));
        margin-top: 0;
    }

    .instrument-strip {
        grid-template-columns: 1fr;
    }
}

@media (max-width: 760px) {
    .book-companion {
        padding: 16px;
    }

    .rail-header {
        align-items: flex-start;
        flex-direction: column;
    }

    .chapter-grid,
    .control-panel,
    .readout-list {
        grid-template-columns: 1fr;
    }

    .stage-heading {
        align-items: flex-start;
        flex-direction: column;
    }

    .chapter-copy span,
    .chapter-copy small {
        white-space: normal;
    }
}
</style>
