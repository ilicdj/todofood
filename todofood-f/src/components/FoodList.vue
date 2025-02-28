<script setup>
import { useFoodList } from '@/stores/food'
import { storeToRefs } from 'pinia'
import { onMounted } from 'vue'
import SingleMeal from './SingleMeal.vue'

const foodStore = useFoodList()
const { food } = storeToRefs(foodStore)

onMounted(() => {
  foodStore.getFood()
})
</script>
<template>
  <div id="all-meals">
    <SingleMeal v-for="meal in food" :meal="meal" />
  </div>
</template>
<style scoped lang="scss">
@use '../assets/scss/variables';
#all-meals {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  margin-top: 2rem;
  padding: 0 1rem;

  @media (min-width: 768px) {
    max-height: 70vh;
    overflow-y: auto;
    overscroll-behavior: contain;
  }
}
</style>
