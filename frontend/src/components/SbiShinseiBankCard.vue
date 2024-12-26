<template>
  <BaseCard title="SBI新生銀行" :total="total" bgColor="#e8f1f9" @click-update="handleClick" />
</template>

<script setup lang="ts">
import BaseCard from "components/BaseCard.vue";

defineProps<{
  total: number;
}>();

const handleClick = () => {
  console.log("click sbi shinsei");
};
</script>
