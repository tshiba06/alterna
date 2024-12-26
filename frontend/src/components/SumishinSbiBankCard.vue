<template>
  <BaseCard title="住信SBI銀行" :total="total" bgColor="#0058A0" @click-update="handleClick" />
</template>

<script setup lang="ts">
import BaseCard from "components/BaseCard.vue";

defineProps<{
  total: number;
}>();

const handleClick = () => {
  console.log("click sumishin sbi");
};
</script>
