<script setup>
import Table from './components/Table.vue';
const API_ENDPOINT ="http://127.0.0.1:8000/operadora/all"
</script>

<template>
  <h1>fastapi-vue-data-processing</h1>
  <p>A .csv data processing and fullstack management project</p>
  <Table :msg="API_ENDPOINT"/> 
</template>