<template>
  <q-page class="row items-center justify-evenly">
    <TotalCard :total="total" :loading="isExistLoading" @click-update="handleAllUpdate" />
    <RakutenBankCard
      :total="totals.rakutenBank"
      :loading="loadings.rakutenBank"
      @click-update="handleRakutenBankUpdate"
    />
    <SbiShinseiBankCard
      :total="totals.sbiShinseiBank"
      :loading="loadings.sbiShinseiBank"
      @click-update="handleSbiShinseiBankUpdate"
    />
    <SumishinSbiBankCard
      :total="totals.sumishinSbiBank"
      :loading="loadings.sumishinSbiBank"
      @click-update="handleSumishinSbiBankUpdate"
    />
    <SbiBenefitSystemCard
      :total="totals.sbiBenefitSystem"
      :loading="loadings.sbiBenefitSystem"
      @click-update="handleSbiBenefitSystemUpdate"
    />
  </q-page>
</template>

<script setup lang="ts">
import RakutenBankCard from "components/RakutenBankCard.vue";
import SbiShinseiBankCard from "components/SbiShinseiBankCard.vue";
import SumishinSbiBankCard from "components/SumishinSbiBankCard.vue";
import SbiBenefitSystemCard from "src/components/SbiBenefitSystemCard.vue";
import TotalCard from "src/components/TotalCard.vue";
import { getRakutenBankRepository } from "src/repositories/RakutenBankRepository";
import { getSbiBenefitSystemRepository } from "src/repositories/SbiBenefitSystemRepository";
import { getSbiShinseiBankRepository } from "src/repositories/SbiShinseiBankRepository";
import { getSumishinSbiBankRepository } from "src/repositories/SumishinSbiBankRepository";
import { computed, onMounted, reactive } from "vue";

const rakutenBankRepository = getRakutenBankRepository();
const sbiShinseiBankRepository = getSbiShinseiBankRepository();
const sumishinSbiBankRepository = getSumishinSbiBankRepository();
const sbiBenefitSystemRepository = getSbiBenefitSystemRepository();

const total = computed(
  () =>
    totals.rakutenBank + totals.sbiShinseiBank + totals.sumishinSbiBank + totals.sbiBenefitSystem,
);

const totals = reactive<{
  rakutenBank: number;
  sbiShinseiBank: number;
  sumishinSbiBank: number;
  sbiBenefitSystem: number;
}>({
  rakutenBank: 0,
  sbiShinseiBank: 0,
  sumishinSbiBank: 0,
  sbiBenefitSystem: 0,
});

const isExistLoading = computed(() => Object.values(loadings).some((loading) => loading));

const loadings = reactive<{
  rakutenBank: boolean;
  sbiShinseiBank: boolean;
  sumishinSbiBank: boolean;
  sbiBenefitSystem: boolean;
}>({
  rakutenBank: false,
  sbiShinseiBank: false,
  sumishinSbiBank: false,
  sbiBenefitSystem: false,
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

  try {
    const res = await sbiBenefitSystemRepository.getLatest();
    totals.sbiBenefitSystem = res.data.total;
  } catch (error) {
    console.error(error);
  }
});

const handleAllUpdate = async () => {
  await handleRakutenBankUpdate();
  await handleSbiShinseiBankUpdate();
  await handleSumishinSbiBankUpdate();
  await handleSbiBenefitSystemUpdate();
};

const handleRakutenBankUpdate = async () => {
  loadings.rakutenBank = true;
  try {
    const up = await rakutenBankRepository.update();
    if (up.status !== 200) {
      console.error("Failed to update");
      return;
    }
    const res = await rakutenBankRepository.getLatest();
    totals.rakutenBank = res.data.total;
  } catch (error) {
    console.error(error);
  }
  loadings.rakutenBank = false;
};

const handleSbiShinseiBankUpdate = async () => {
  loadings.sbiShinseiBank = true;
  try {
    const up = await sbiShinseiBankRepository.update();
    if (up.status !== 200) {
      console.error("Failed to update");
      return;
    }
    const res = await sbiShinseiBankRepository.getLatest();
    totals.sbiShinseiBank = res.data.total;
  } catch (error) {
    console.error(error);
  }
  loadings.sbiShinseiBank = false;
};

const handleSumishinSbiBankUpdate = async () => {
  loadings.sumishinSbiBank = true;
  try {
    const up = await sumishinSbiBankRepository.update();
    if (up.status !== 200) {
      console.error("Failed to update");
      return;
    }
    const res = await sumishinSbiBankRepository.getLatest();
    totals.sumishinSbiBank = res.data.total;
  } catch (error) {
    console.error(error);
  }
  loadings.sumishinSbiBank = false;
};

const handleSbiBenefitSystemUpdate = async () => {
  loadings.sbiBenefitSystem = true;
  try {
    const up = await sbiBenefitSystemRepository.update();
    if (up.status !== 200) {
      console.error("Failed to update");
      return;
    }
    const res = await sbiBenefitSystemRepository.getLatest();
    totals.sbiBenefitSystem = res.data.total;
  } catch (error) {
    console.error(error);
  }
  loadings.sbiBenefitSystem = false;
};
</script>
