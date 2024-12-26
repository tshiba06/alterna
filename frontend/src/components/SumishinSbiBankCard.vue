<template>
  <BaseCard title="住信SBI銀行" :total="total" bgColor="#0058A0" />
</template>

<script setup lang="ts">
import BaseCard from 'components/BaseCard.vue'

defineProps<{
  total: number
}>()
</script>
