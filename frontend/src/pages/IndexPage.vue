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
    <!-- Added MitsuisumitomoCardCard -->
    <div class="col-12 col-md-4 q-pa-md">
      <MitsuisumitomoCardCard
        :total="totals.smbcCard"
        :loading="loadings.smbcCard"
        @click-update="handleSmbcCardUpdate"
      />
    </div>
  </q-page>
</template>

<script setup lang="ts">
import RakutenBankCard from "components/RakutenBankCard.vue";
import SbiShinseiBankCard from "components/SbiShinseiBankCard.vue";
import SumishinSbiBankCard from "components/SumishinSbiBankCard.vue";
import SbiBenefitSystemCard from "src/components/SbiBenefitSystemCard.vue";
import MitsuisumitomoCardCard from "components/MitsuisumitomoCardCard.vue"; // Added import
import TotalCard from "src/components/TotalCard.vue";
import { getRakutenBankRepository } from "src/repositories/RakutenBankRepository";
import { getSbiBenefitSystemRepository } from "src/repositories/SbiBenefitSystemRepository";
import { getSbiShinseiBankRepository } from "src/repositories/SbiShinseiBankRepository";
import { getSumishinSbiBankRepository } from "src/repositories/SumishinSbiBankRepository";
import { getMitsuisumitomoCardRepository } from "src/repositories/MitsuisumitomoCardRepository"; // Added import
import { computed, onMounted, reactive } from "vue";

const rakutenBankRepository = getRakutenBankRepository();
const sbiShinseiBankRepository = getSbiShinseiBankRepository();
const sumishinSbiBankRepository = getSumishinSbiBankRepository();
const sbiBenefitSystemRepository = getSbiBenefitSystemRepository();
const smbcCardRepository = getMitsuisumitomoCardRepository(); // Added instantiation

const total = computed(
  () =>
    totals.rakutenBank +
    totals.sbiShinseiBank +
    totals.sumishinSbiBank +
    totals.sbiBenefitSystem +
    totals.smbcCard, // Added smbcCard to total
);

const mitsuisumitomo = new WebSocket("ws://localhost:18080/mitsuisumitomo_bank");
mitsuisumitomo.onopen = () => {
  console.log("Connected to mitsuisumitomo");
  mitsuisumitomo.send("Hello from frontend");
};

mitsuisumitomo.onmessage = (event) => {
  console.log(event.data);
};

mitsuisumitomo.onclose = () => {
  console.log("Disconnected from mitsuisumitomo");
};

mitsuisumitomo.onerror = (error) => {
  console.error("Error:", error);
};

const totals = reactive<{
  rakutenBank: number;
  sbiShinseiBank: number;
  sumishinSbiBank: number;
  sbiBenefitSystem: number;
  smbcCard: number; // Added smbcCard
}>({
  rakutenBank: 0,
  sbiShinseiBank: 0,
  sumishinSbiBank: 0,
  sbiBenefitSystem: 0,
  smbcCard: 0, // Added smbcCard
});

const isExistLoading = computed(() => Object.values(loadings).some((loading) => loading));

const loadings = reactive<{
  rakutenBank: boolean;
  sbiShinseiBank: boolean;
  sumishinSbiBank: boolean;
  sbiBenefitSystem: boolean;
  smbcCard: boolean; // Added smbcCard
}>({
  rakutenBank: false,
  sbiShinseiBank: false,
  sumishinSbiBank: false,
  sbiBenefitSystem: false,
  smbcCard: false, // Added smbcCard
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

  // Added SMBC Card initial fetch
  try {
    const res = await smbcCardRepository.getLatest();
    totals.smbcCard = res.data.total ?? 0;
  } catch (error) {
    console.error("Error fetching initial SMBC Card data:", error);
    totals.smbcCard = 0;
  }
});

const handleAllUpdate = async () => {
  try {
    await Promise.all([
      handleRakutenBankUpdate(),
      handleSbiShinseiBankUpdate(),
      handleSumishinSbiBankUpdate(),
      handleSbiBenefitSystemUpdate(),
      handleSmbcCardUpdate(), // Added SMBC Card update to all
    ]);
  } catch (error) {
    console.error("Error during updates:", error);
  }
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

// Updated SMBC Card update logic
const handleSmbcCardUpdate = async () => {
  loadings.smbcCard = true;
  try {
    const up = await smbcCardRepository.update(); // Calls POST /save
    if (up.status !== 200) {
      console.error("Failed to trigger SMBC Card data refresh");
      // Optionally set an error message for the user
    }
    // Always try to get the latest, even if update status wasn't 200,
    // as backend might have recovered or old data might still be useful.
    const res = await smbcCardRepository.getLatest();
    totals.smbcCard = res.data.total ?? 0; // Use nullish coalescing for safety
  } catch (error) {
    console.error("Error updating SMBC Card:", error);
    totals.smbcCard = 0; // Reset or keep old value on error
    // Optionally set an error message for the user
  }
  loadings.smbcCard = false;
};
</script>
