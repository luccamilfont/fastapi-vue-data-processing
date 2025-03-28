<template>
  <div>
    <vue-good-table
      :columns="columns"
      :rows="rows"/>
  </div>
</template>

<script>
const API_ENDPOINT = 'http://127.0.0.1:8000/operadora/all'
import { reactive } from 'vue'; 
import axios from 'axios'

const data = reactive({ 
  responses: "",
  keyWord: "",
});

const getData = async () => {
  let result = await axios.get(API_ENDPOINT, {params: {prompt: data.keyWord}}); 
  data.responses = result.data;
};

getData()

export default {
  name: 'my-component',
  data(){
    return {
      columns: [
        {
          label: 'Data',
          field: 'data',
          dateInputFormat: 'yyyy-MM-dd',
          dateOutputFormat: 'dd MMM yy'
        },
        {
          label: 'Reg_Ans',
          field: 'reg_ans',
          type: 'number',
        },
        {
          label: 'CD_CONTA_CONTABIL',
          field: 'cd_conta_contabil',
          type: 'number',
        },
        {
          label: 'Descrição',
          field: 'descricao',
          type: 'string',
        },
        {
          label: 'VL_SALDO_INICIAL',
          field: 'vl_saldo_inicial',
          type: 'decimal',
        },
        {
          label: 'VL_SALDO_FINAL',
          field: 'vl_saldo_final',
          type: 'decimal',
        },
      ],
      rows: [
        { data: "2025-03-28",  reg_ans: 422941,  cd_conta_contabil: 461719011,  descricao: "Alimentação ao Trabalhador",  vl_saldo_inicial: 7272.27,  vl_saldo_final: 9882.25},
      ],
    };
  },
};
</script>