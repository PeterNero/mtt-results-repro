<template>
    <div flex-1 flex flex-col items-center>
        <section container class="mt-24 sm:mt-36 mb-16 sm:mb-32">
            <div flex class="px-0 xl:px-16 2xl:px-24 flex-col sm:flex-row">
                <div class="mr-0 sm:mr-4 md:mr-6 mb-4 sm-mb-0 flex justify-center items-start md-items-center">
                    <div class="i-custom:icon text-7xl sm:text-9xl md:text-[9.5rem]"></div>
                </div>
                <div class="text-center sm:text-start">
                    <h1 class="text-4xl sm:text-5xl" font-bold text="#2A9D8F">
                        Sandbox Science
                    </h1>
                    <h2 class="text-lg sm:text-2xl" font-bold mt-3>Unlock the mysteries of science through immersive and interactive simulations.</h2>
                    <p mt-4 class="text-sm sm:text-base">
                        Explore Game of Life, Particle Life, and other captivating scientific simulations. Dive into hands-on
                        learning and discover complex concepts with interactive visual experiences.
                    </p>
                </div>
            </div>
        </section>
        <section container>
            <div grid gap-4 grid-cols-1 class="sm:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-7">
                <NuxtLink to="/particle-life" bg="gray-900 hover:gray-800"
                          class="relative overflow-hidden rounded-lg border border-gray-800 shadow-lg p-6 sm:p-5 md:p-6 pt-3 sm:pt-4 md:pt-4">
                    <div flex items-center mb-2>
                        <span class="text-2xl md:text-3xl" font-bold mr-2>⚛</span>
                        <h3 class="text-lg md:text-xl font-semibold">Particle Life</h3>
                    </div>
                    <p class="text-sm md:text-base">Observe the fascinating interactions and emergent behaviors of particles in a dynamic and interactive environment.</p>
                    <div class="absolute right-0 top-0 h-16 w-16">
                        <div class="shadow-lg absolute transform rotate-45 bg-[#00b84d] bg-opacity-70 text-center text-sm text-white font-semibold py-1 right-[-38px] top-[13px] w-[128px]">
                            BETA
                        </div>
                    </div>
                </NuxtLink>
                <NuxtLink to="/dot-war" bg="gray-900 hover:gray-800"
                          class="relative overflow-hidden rounded-lg border border-gray-800 shadow-lg p-6 sm:p-5 md:p-6 pt-3 sm:pt-4 md:pt-4">
                    <div flex items-center mb-2>
                        <span class="i-tabler-swords text-2xl md:text-3xl mr-2 text-red-300"></span>
                        <h3 class="text-lg md:text-xl font-semibold">Dot War</h3>
                    </div>
                    <p class="text-sm md:text-base">Simulate tribes of dots that forage, scout, fight, build spawn places, fortresses, and towers, then share memories.</p>
                    <div class="absolute right-0 top-0 h-16 w-16">
                        <div class="shadow-lg absolute transform rotate-45 bg-[#dc2626] bg-opacity-70 text-center text-sm text-white font-semibold py-1 right-[-38px] top-[13px] w-[128px]">
                            SIM
                        </div>
                    </div>
                </NuxtLink>
                <NuxtLink to="/proto-spinor" bg="gray-900 hover:gray-800"
                          class="relative overflow-hidden rounded-lg border border-gray-800 shadow-lg p-6 sm:p-5 md:p-6 pt-3 sm:pt-4 md:pt-4">
                    <div flex items-center mb-2>
                        <span class="i-tabler-atom-2 text-2xl md:text-3xl mr-2 text-emerald-300"></span>
                        <h3 class="text-lg md:text-xl font-semibold">Proto-Spinor</h3>
                    </div>
                    <p class="text-sm md:text-base">Explore circle phase, lens transport, nil basin capture, identity anchors, and cancellation modes in a live particle kernel.</p>
                    <div class="absolute right-0 top-0 h-16 w-16">
                        <div class="shadow-lg absolute transform rotate-45 bg-[#2a9d8f] bg-opacity-70 text-center text-sm text-white font-semibold py-1 right-[-38px] top-[13px] w-[128px]">
                            LAB
                        </div>
                    </div>
                </NuxtLink>
                <NuxtLink to="/proto-spinor-3d" bg="gray-900 hover:gray-800"
                          class="relative overflow-hidden rounded-lg border border-gray-800 shadow-lg p-6 sm:p-5 md:p-6 pt-3 sm:pt-4 md:pt-4">
                    <div flex items-center mb-2>
                        <span class="i-tabler-sphere text-2xl md:text-3xl mr-2 text-cyan-300"></span>
                        <h3 class="text-lg md:text-xl font-semibold">Proto-Spinor 3D</h3>
                    </div>
                    <p class="text-sm md:text-base">Orbit a 3D kernel with carrier constraints, quark triplets, atom capture, photon radiation, and an explicit MTT-to-SM bridge.</p>
                    <div class="absolute right-0 top-0 h-16 w-16">
                        <div class="shadow-lg absolute transform rotate-45 bg-[#2878ff] bg-opacity-70 text-center text-sm text-white font-semibold py-1 right-[-38px] top-[13px] w-[128px]">
                            3D
                        </div>
                    </div>
                </NuxtLink>
                <NuxtLink to="/proto-spinor-projection" bg="gray-900 hover:gray-800"
                          class="relative overflow-hidden rounded-lg border border-gray-800 shadow-lg p-6 sm:p-5 md:p-6 pt-3 sm:pt-4 md:pt-4">
                    <div flex items-center mb-2>
                        <span class="i-tabler-layers-intersect text-2xl md:text-3xl mr-2 text-lime-300"></span>
                        <h3 class="text-lg md:text-xl font-semibold">Proto-Spinor Projection</h3>
                    </div>
                    <p class="text-sm md:text-base">View one proto-spinor as a physical shadow of an inner nil, circle, lens, and double-cover state.</p>
                    <div class="absolute right-0 top-0 h-16 w-16">
                        <div class="shadow-lg absolute transform rotate-45 bg-[#5fc66d] bg-opacity-70 text-center text-sm text-white font-semibold py-1 right-[-38px] top-[13px] w-[128px]">
                            MTT
                        </div>
                    </div>
                </NuxtLink>
                <NuxtLink to="/bad-memory-book" bg="gray-900 hover:gray-800"
                          class="relative overflow-hidden rounded-lg border border-gray-800 shadow-lg p-6 sm:p-5 md:p-6 pt-3 sm:pt-4 md:pt-4">
                    <div flex items-center mb-2>
                        <span class="i-tabler-book-2 text-2xl md:text-3xl mr-2 text-amber-200"></span>
                        <h3 class="text-lg md:text-xl font-semibold">Bad Memory Book</h3>
                    </div>
                    <p class="text-sm md:text-base">Select chapters from the book and view tailored simulations of admissibility, particles, records, proto-spinors, and cosmology.</p>
                    <div class="absolute right-0 top-0 h-16 w-16">
                        <div class="shadow-lg absolute transform rotate-45 bg-[#bb7a25] bg-opacity-70 text-center text-sm text-white font-semibold py-1 right-[-38px] top-[13px] w-[128px]">
                            BOOK
                        </div>
                    </div>
                </NuxtLink>
                <NuxtLink to="/cosmology" bg="gray-900 hover:gray-800"
                          class="relative overflow-hidden rounded-lg border border-gray-800 shadow-lg p-6 sm:p-5 md:p-6 pt-3 sm:pt-4 md:pt-4">
                    <div flex items-center mb-2>
                        <span class="i-tabler-world-star text-2xl md:text-3xl mr-2 text-amber-200"></span>
                        <h3 class="text-lg md:text-xl font-semibold">Universe Forge</h3>
                    </div>
                    <p class="text-sm md:text-base">Simulate H/He gas, dark matter collapse, star birth, fusion, supernova enrichment, black holes, and planet systems.</p>
                    <div class="absolute right-0 top-0 h-16 w-16">
                        <div class="shadow-lg absolute transform rotate-45 bg-[#d58a2a] bg-opacity-70 text-center text-sm text-white font-semibold py-1 right-[-38px] top-[13px] w-[128px]">
                            COSMO
                        </div>
                    </div>
                </NuxtLink>
                <NuxtLink to="/game-of-life" bg="gray-900 hover:gray-800"
                          class="relative overflow-hidden rounded-lg border border-gray-800 shadow-lg p-6 sm:p-5 md:p-6 pt-3 sm:pt-4 md:pt-4">
                    <div flex items-center mb-2>
                        <span class="text-2xl md:text-3xl" font-bold mr-1>🧬</span>
                        <h3 class="text-lg md:text-xl font-semibold">Game Of Life</h3>
                    </div>
                    <p class="text-sm md:text-base">Explore the intriguing patterns and behaviors of cellular automata in this classic simulation by John Conway.</p>
                    <div class="absolute right-0 top-0 h-16 w-16">
                        <div class="shadow-lg absolute transform rotate-45 bg-[#e76f51] bg-opacity-70 text-center text-sm text-white font-semibold py-1 right-[-38px] top-[13px] w-[128px]">
                            ALPHA
                        </div>
                    </div>
                </NuxtLink>
                <NuxtLink to="/hash-life" bg="gray-900 hover:gray-800"
                          class="relative overflow-hidden rounded-lg border border-gray-800 shadow-lg p-6 sm:p-5 md:p-6 pt-3 sm:pt-4 md:pt-4">
                    <div flex items-center mb-2>
                        <span class="text-2xl md:text-3xl" font-bold mr-2>🚀</span>
                        <h3 class="text-lg md:text-xl font-semibold">Hash Life</h3>
                    </div>
                    <p class="text-sm md:text-base">Experience the optimized version of the Game of Life, enabling faster and more efficient simulation of complex patterns.</p>
                    <div class="absolute right-0 top-0 h-16 w-16">
                        <div class="shadow-lg absolute transform rotate-45 bg-[#5b2e48] bg-opacity-70 text-center text-sm text-white font-semibold py-1 right-[-38px] top-[13px] w-[128px]">
                            WIP
                        </div>
                    </div>
                </NuxtLink>
            </div>
        </section>
        <section my-12 flex-1 flex flex-col justify-end>
            <div w-full flex>
                <NuxtLink to="https://discord.com/invite/z5yuzkFpCA" title="Discord" aria-label="Discord" target="_blank" flex items-center py-0 mx-2>
                    <button type="button" name="Discord" aria-label="Discord" text="zinc-3 hover:zinc-1" flex>
                        <span i-carbon-logo-discord text-5xl></span>
                    </button>
                </NuxtLink>
                <NuxtLink to="https://github.com/DicSo92/SandboxScience" title="Github" aria-label="Github" target="_blank" flex items-center py-0 mx-2>
                    <button type="button" name="Github" aria-label="Github" text="zinc-3 hover:zinc-1" flex>
                        <span i-carbon-logo-github text-5xl></span>
                    </button>
                </NuxtLink>
            </div>
        </section>
    </div>
</template>

<script setup lang="ts">
definePageMeta({
    layout: 'life'
})
</script>

<style scoped lang="scss">

</style>
