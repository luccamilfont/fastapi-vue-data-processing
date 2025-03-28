<script setup>
import { ref } from 'vue'

const count = ref(0)
</script>

<template>
  <div>
    <vue-good-table
      :columns="columns"
      :rows="rows"
      :pagination-options="{
          enabled: true,
          perPage: 3,
          mode: 'records'
      }"/>
  </div>
</template>

<script>
const OPERADORA_ALL_ENDPOINT = 'http://127.0.0.1:8000/operadora/relevant'
import axios from 'axios'

export default {
  data: function(){
    return{
      columns: [
        { label: 'Logradouro', field: 'logradouro', type: 'string' },
        { label: 'Telefone', field: 'telefone', type: 'string' },
        { label: 'Número', field: 'numero', type: 'string' },
        { label: 'Fax', field: 'fax', type: 'string' },
        { label: 'Complemento', field: 'complemento', type: 'string' },
        { label: 'Endereço Eletrônico', field: 'endereco_eletronico', type: 'string' },
        { label: 'Reg ANS', field: 'reg_ans', type: 'number' },
        { label: 'Bairro', field: 'bairro', type: 'string' },
        { label: 'Representante', field: 'representante', type: 'string' },
        { label: 'ID', field: 'id', type: 'number' },
        { label: 'CNPJ', field: 'cnpj', type: 'string' },
        { label: 'Cidade', field: 'cidade', type: 'string' },
        { label: 'Cargo Representante', field: 'cargo_representante', type: 'string' },
        { label: 'Razão Social', field: 'razao_social', type: 'string' },
        { label: 'UF', field: 'uf', type: 'string' },
        { label: 'Região de Comercialização', field: 'regiao_de_comercializacao', type: 'number' },
        { label: 'Nome Fantasia', field: 'nome_fantasia', type: 'string' },
        { label: 'CEP', field: 'cep', type: 'number' },
        { label: 'Data Registro ANS', field: 'data_registro_ans', type: 'string' },
        { label: 'Modalidade', field: 'modalidade', type: 'string' },
        { label: 'DDD', field: 'ddd', type: 'number' },
      ],
      rows: []
    };
  },
  created(){
    axios.get(OPERADORA_ALL_ENDPOINT)
    .then((response) => {
        this.rows = response.data;
    })
    .catch((error) => {
      console.log(error);
    });
  },
};
</script>