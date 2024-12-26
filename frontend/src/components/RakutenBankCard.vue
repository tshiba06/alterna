<template>
  <BaseCard title="楽天銀行" :total="total" bgColor="#bf0000" />
</template>

<script setup lang="ts">
import BaseCard from "components/BaseCard.vue";

defineProps<{
  total: number;
}>();
</script>
