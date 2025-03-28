<script setup>
import TableFiltered from './components/TableFiltered.vue';
import TableAll from './components/TableAll.vue';
</script>

<template>
  <h1>fastapi-vue-data-processing</h1>
  <p>A .csv data processing and fullstack management project made by <a href="https://github.com/luccamilfont">Lucca Milfont.</a></p>
  <p>This app displays the most relevant companies based on amount of positive balance in all of its transactions and all companies from the data processed by the .csv data extraction scripts.</p>

  <br>

  <h2>Relevant companies</h2>
  <TableFiltered/> 

  <br>
  <br>

  <h2>All companies</h2>
  <TableAll/> 
</template>