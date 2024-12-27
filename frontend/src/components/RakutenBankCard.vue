<template>
  <BaseCard title="楽天銀行" :total="total" bgColor="#bf0000" @click-update="handleClick" />
</template>

<script setup lang="ts">
import BaseCard from "components/BaseCard.vue";
import { api } from "src/boot/axios";
import { onMounted, ref } from "vue";

const total = ref<number>(0);
onMounted(async () => {
  try {
    const res = await api.get("/banks/rakuten", {
      headers: {
        "Content-Type": "application/json",
      },
    });
    total.value = res.data.total;
  } catch (error) {
    console.error(error);
  }
});

const handleClick = () => {
  console.log("click rakuten");
};
</script>
