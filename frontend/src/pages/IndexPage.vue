<template>
  <q-page class="row items-center justify-evenly">
    <BaseCard title="test" :total="1234" bgColor="white" />
    <RakutenBankCard :total="totals.rakutenBank" />
    <SbiShinseiBankCard :total="1234" />
    <SumishinSbiBankCard :total="1234" />
  </q-page>
</template>

<script setup lang="ts">
import BaseCard from "components/BaseCard.vue";
import RakutenBankCard from "components/RakutenBankCard.vue";
import SbiShinseiBankCard from "components/SbiShinseiBankCard.vue";
import SumishinSbiBankCard from "components/SumishinSbiBankCard.vue";
import { getRakutenBankRepository } from "src/repository/RakutenBankRepository";
import { onMounted, reactive } from "vue";

const rakutenBankRepository = getRakutenBankRepository();

const totals = reactive<{
  rakutenBank: number;
}>({
  rakutenBank: 0,
});

onMounted(async () => {
  try {
    const res = await rakutenBankRepository.getLatest();
    totals.rakutenBank = res.data.total;
  } catch (error) {
    console.error(error);
  }
});
</script>
