<template>
  <q-page class="row items-center justify-evenly">
    <BaseCard title="test" :total="1234" bgColor="white" />
    <RakutenBankCard />
    <SbiShinseiBankCard :total="1234" />
    <SumishinSbiBankCard :total="1234" />
  </q-page>
</template>

<script setup lang="ts">
import BaseCard from "components/BaseCard.vue";
import RakutenBankCard from "components/RakutenBankCard.vue";
import SbiShinseiBankCard from "components/SbiShinseiBankCard.vue";
import SumishinSbiBankCard from "components/SumishinSbiBankCard.vue";
</script>
