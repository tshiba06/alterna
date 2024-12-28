<template>
  <BaseCard title="Total" :total="total" bgColor="" />
</template>

<script setup lang="ts">
import BaseCard from "components/BaseCard.vue";

defineProps<{
  total: number;
}>();
</script>
