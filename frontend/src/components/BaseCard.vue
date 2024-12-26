<template>
  <div>
    <q-card>
      <q-card-actions class="justify-end" :style="{ backgroundColor: bgColor }">
        <q-btn flat round class="text-with-outline bg-white" @click="handleClick">更新</q-btn>
      </q-card-actions>
      <q-card-section>
        <div class="title">{{ title }}</div>
        <span class="text-h3">{{ total.toLocaleString() }}</span> 円
      </q-card-section>
    </q-card>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  total: number;
  title: string;
  bgColor: string;
}>();

const emits = defineEmits<{
  (e: "click-update"): void;
}>();

const handleClick = () => {
  emits("click-update");
};
</script>

<style scoped>
.title {
  font-size: 16px;
}
</style>
