<template>
  <BaseCard
    title="三井住友カード"
    :total="total"
    :loading="loading"
    bgColor="#004736"  // A common color for SMBC Card, adjust if needed
    @click-update="handleClick"
  />
</template>

<script setup lang="ts">
import BaseCard from 'components/BaseCard.vue';

defineProps<{
  total: number;
  loading: boolean;
}>();

const emits = defineEmits<{
  (e: 'click-update'): void;
}>();

const handleClick = () => {
  emits('click-update');
};
</script>
