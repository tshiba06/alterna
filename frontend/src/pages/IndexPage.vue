<template>
  <q-page class="row items-center justify-evenly">
    <TotalCard :total="total" />
    <RakutenBankCard :total="totals.rakutenBank" />
    <SbiShinseiBankCard :total="totals.sbiShinseiBank" />
    <SumishinSbiBankCard :total="totals.sumishinSbiBank" />
  </q-page>
</template>

<script setup lang="ts">
import RakutenBankCard from "components/RakutenBankCard.vue";
import SbiShinseiBankCard from "components/SbiShinseiBankCard.vue";
import SumishinSbiBankCard from "components/SumishinSbiBankCard.vue";
import TotalCard from "src/components/TotalCard.vue";
import { getRakutenBankRepository } from "src/repositories/RakutenBankRepository";
import { getSbiShinseiBankRepository } from "src/repositories/SbiShinseiBankRepository";
import { getSumishinSbiBankRepository } from "src/repositories/SumishinSbiBankRepository";
import { computed, onMounted, reactive } from "vue";

const rakutenBankRepository = getRakutenBankRepository();
const sbiShinseiBankRepository = getSbiShinseiBankRepository();
const sumishinSbiBankRepository = getSumishinSbiBankRepository();

const total = computed(() => totals.rakutenBank + totals.sbiShinseiBank + totals.sumishinSbiBank);

const totals = reactive<{
  rakutenBank: number;
  sbiShinseiBank: number;
  sumishinSbiBank: number;
}>({
  rakutenBank: 0,
  sbiShinseiBank: 0,
  sumishinSbiBank: 0,
});

onMounted(async () => {
  try {
    const res = await rakutenBankRepository.getLatest();
    totals.rakutenBank = res.data.total;
  } catch (error) {
    console.error(error);
  }

  try {
    const res = await sbiShinseiBankRepository.getLatest();
    totals.sbiShinseiBank = res.data.total;
  } catch (error) {
    console.error(error);
  }

  try {
    const res = await sumishinSbiBankRepository.getLatest();
    totals.sumishinSbiBank = res.data.total;
  } catch (error) {
    console.error(error);
  }
});
</script>
