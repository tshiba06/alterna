<template>
  <BaseCard
    title="SBI新生銀行"
    :total="total"
    :loading="loading"
    bgColor="#e8f1f9"
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
