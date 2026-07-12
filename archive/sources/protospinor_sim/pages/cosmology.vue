<template>
    <UniverseKernel />
</template>

<script setup lang="ts">
import UniverseKernel from '~/components/cosmology/UniverseKernel.vue'

definePageMeta({
    layout: 'life',
    hideNavBar: true,
})

useSeoMeta({
    title: 'Universe Forge',
    ogTitle: 'Universe Forge',
    twitterTitle: 'Universe Forge',
    description: 'Run a coarse-grained universe simulation where H/He gas collapses into stars, fusion builds elements, feedback spreads metals, and planet systems emerge.',
    ogDescription: 'Run a coarse-grained universe simulation where H/He gas collapses into stars, fusion builds elements, feedback spreads metals, and planet systems emerge.',
    twitterDescription: 'Run a coarse-grained universe simulation where H/He gas collapses into stars, fusion builds elements, feedback spreads metals, and planet systems emerge.',
})
</script>
