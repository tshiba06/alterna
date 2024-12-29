<template>
  <BaseCard
    title="SBIベネフィットシステムズ"
    :total="total"
    :loading="loading"
    bgColor="#2ea2ed"
    @click-update="handleClick"
  />
</template>

<script setup lang="ts">
import BaseCard from "components/BaseCard.vue";

defineProps<{
  total: number;
  loading: boolean;
}>();

const emits = defineEmits<{
  (e: "click-update"): void;
}>();

const handleClick = () => {
  emits("click-update");
};
</script>
