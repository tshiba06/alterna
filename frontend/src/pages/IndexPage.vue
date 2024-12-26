<template>
  <q-page class="row items-center justify-evenly">
    <BaseCard title="test" :total="1234" bgColor="white" />
    <RakutenBankCard :total="1234" />
  </q-page>
</template>

<script setup lang="ts">
import BaseCard from 'components/BaseCard.vue'
import RakutenBankCard from 'components/RakutenBankCard.vue'
</script>
