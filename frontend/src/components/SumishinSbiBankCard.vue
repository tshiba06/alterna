<template>
  <BaseCard
    title="住信SBI銀行"
    :total="total"
    :loading="loading"
    bgColor="#0058A0"
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
