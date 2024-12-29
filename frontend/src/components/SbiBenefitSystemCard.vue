<template>
  <BaseCard
    title="SBIベネフィットシステムズ"
    :total="total"
    bgColor="#2ea2ed"
    @click-update="handleClick"
  />
</template>

<script setup lang="ts">
import BaseCard from "components/BaseCard.vue";

defineProps<{
  total: number;
}>();

const handleClick = () => {
  console.log("click sbi benefit");
};
</script>
