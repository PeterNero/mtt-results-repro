<template>
    <BadMemoryBookCompanion />
</template>

<script setup lang="ts">
import BadMemoryBookCompanion from '~/components/book/BadMemoryBookCompanion.vue'

definePageMeta({
    layout: 'life',
    hideNavBar: true,
})

useSeoMeta({
    title: 'The Universe Has a Bad Memory - Chapter Simulations',
    ogTitle: 'The Universe Has a Bad Memory - Chapter Simulations',
    twitterTitle: 'The Universe Has a Bad Memory - Chapter Simulations',
    description: 'A chapter-by-chapter companion simulation for The Universe Has a Bad Memory.',
    ogDescription: 'A chapter-by-chapter companion simulation for The Universe Has a Bad Memory.',
    twitterDescription: 'A chapter-by-chapter companion simulation for The Universe Has a Bad Memory.',
})
</script>
