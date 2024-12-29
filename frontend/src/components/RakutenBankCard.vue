<template>
  <BaseCard
    title="楽天銀行"
    :total="total"
    :loading="loading"
    bgColor="#bf0000"
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
