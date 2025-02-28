<script setup lang="ts">
import FoodList from './components/FoodList.vue';
import AddMealModal from './components/AddMealModal.vue'
</script>

<template>
  <div id="app-wrapper">
    <div id="left">
      <h1>Food Todo</h1>
      <AddMealModal />
    </div>
    <div>
      <FoodList />
    </div>
  </div>
</template>

<style scoped lang="scss">
@use './assets/scss/variables';

#app-wrapper {
  height: 100vh;
  width: 100%;
  background-color: variables.$light;
  padding: 1.25rem 0;
  display: flex;
  flex-direction: column;
  h1 {
    font-family: variables.$font-heading;
    text-align: center;
  }
}
@media (min-width: 768px) {
  #app-wrapper {
    padding: 1.25rem 2rem;
    flex-direction: row;
    align-items: center;
    justify-content: space-around;
    div#left {
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;
      gap: 1rem;
      h1 {
        text-align: start;
      }
    }
  }
  .btn-wrapper {
    text-align: start;
  }
}
</style>
