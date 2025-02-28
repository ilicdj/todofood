<script setup lang="ts">
import { ref } from 'vue'
import { useFoodList } from '@/stores/food'

const props = defineProps({
  meal: {
    type: Object,
    required: true,
  },
})
const showMore = ref(false)
const foodStore = useFoodList()

function handleShowMore() {
  showMore.value = !showMore.value
}

function handleDeleteMeal() {
  foodStore.deleteFood(props.meal.id)
}

</script>
<template>
  <div class="single-meal" @click="handleShowMore">
    <h2>
      {{ props.meal.meal_name }}
    </h2>
  </div>
  <div v-if="showMore" id="fullInformation">
    <p>Meal Name: <span>{{ props.meal.meal_name }}</span></p>
    <p>Ingredients: <span>{{ props.meal.ingredients }}</span></p>
    <p>Description: <span>{{ props.meal.description }}</span></p>
    <p>Time in minutes: <span>{{ props.meal.time_in_minutes }}</span></p>
    <p>Vegan: <span>{{ props.meal.is_vegan ? 'Yes' : 'No' }}</span></p>
    <p>Gluten Free: <span>{{ props.meal.is_gluten_free ? 'Yes' : 'No' }}</span></p>
    <div>
      <button @click="handleShowMore()">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="35"
          height="35"
          viewBox="0 0 52 52"
          fill="none"
        >
          <g clip-path="url(#clip0_56_6)">
            <path
              d="M26 26L41.1667 41.1667M26 26L10.8334 10.8334M26 26L10.8334 41.1667M26 26L41.1667 10.8334"
              stroke="#FFFCF8"
              stroke-width="2"
              stroke-linecap="round"
              stroke-linejoin="round"
            />
          </g>
          <defs>
            <clipPath id="clip0_56_6">
              <rect width="52" height="52" fill="white" />
            </clipPath>
          </defs>
        </svg>
      </button>
      <button @click="handleDeleteMeal()">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="35"
          height="35"
          viewBox="0 0 85 85"
          fill="none"
        >
          <path
            d="M42.5 12.3959C40.1517 12.3959 37.8996 13.3287 36.2391 14.9892C34.5787 16.6497 33.6458 18.9018 33.6458 21.25V21.6609C30.1608 22.0115 27.4691 22.5392 25.4433 23.0775C24.1324 23.4091 22.8507 23.8474 21.6112 24.388C21.1679 24.5898 20.7352 24.8144 20.315 25.0609L20.2866 25.075L20.276 25.0821L20.2725 25.0857C20.2725 25.0857 20.2689 25.0892 21.25 26.5625L20.2689 25.0892C19.8853 25.3512 19.6199 25.7534 19.53 26.2092C19.4402 26.665 19.533 27.1378 19.7886 27.5258C20.0441 27.9138 20.4419 28.1858 20.8961 28.2832C21.3504 28.3806 21.8247 28.2956 22.2169 28.0465L22.231 28.0359L22.3621 27.965C22.587 27.8447 22.8162 27.7325 23.0491 27.6286C23.7079 27.3346 24.781 26.9202 26.3535 26.5023C29.5056 25.663 34.6623 24.7917 42.5035 24.7917C50.3377 24.7917 55.4944 25.663 58.6464 26.5023C60.2189 26.9238 61.2956 27.3346 61.9508 27.6286C62.2292 27.7525 62.5022 27.8884 62.7689 28.0359L62.7831 28.0465C63.1753 28.2956 63.6496 28.3806 64.1038 28.2832C64.5581 28.1858 64.9558 27.9138 65.2114 27.5258C65.4669 27.1378 65.5598 26.665 65.4699 26.2092C65.3801 25.7534 65.1147 25.3512 64.731 25.0892L64.7239 25.0821L64.7133 25.075L64.685 25.0573C64.5743 24.9849 64.4596 24.9186 64.3414 24.859C64.0298 24.6913 63.712 24.5354 63.3887 24.3915C62.1492 23.8509 60.8676 23.4126 59.5566 23.0811C56.8637 22.3951 54.1212 21.9214 51.3541 21.6644V21.25C51.3541 18.9018 50.4213 16.6497 48.7608 14.9892C47.1003 13.3287 44.8483 12.3959 42.5 12.3959ZM47.8125 21.3917C46.1833 21.2973 44.4125 21.25 42.5 21.25C40.5875 21.25 38.8166 21.2973 37.1875 21.3917V21.25C37.1875 19.8411 37.7472 18.4898 38.7435 17.4935C39.7398 16.4972 41.091 15.9375 42.5 15.9375C43.9089 15.9375 45.2602 16.4972 46.2565 17.4935C47.2528 18.4898 47.8125 19.8411 47.8125 21.25V21.3917ZM22.7729 31.8927C23.2373 31.827 23.7088 31.9482 24.084 32.2297C24.4591 32.5113 24.7073 32.9301 24.7739 33.3944L28.351 58.4198C28.6591 60.6015 28.8823 62.1386 29.1479 63.3427C29.41 64.5186 29.6862 65.2375 30.051 65.8042C30.7849 66.948 31.8324 67.8566 33.0685 68.4215C33.6812 68.7013 34.4321 68.8748 35.6362 68.9669C36.8616 69.0625 38.4164 69.0625 40.6194 69.0625H45.5564C47.8585 69.0625 49.4841 69.0625 50.7627 68.9598C52.0164 68.8642 52.7956 68.6765 53.4189 68.379C54.6878 67.7773 55.7492 66.8121 56.4683 65.6059C56.8225 65.0109 57.0846 64.253 57.3006 63.0134C57.5237 61.7525 57.676 60.134 57.8956 57.8425L60.2154 33.4759C60.2375 33.2443 60.305 33.0193 60.414 32.8137C60.5231 32.6082 60.6715 32.4261 60.8509 32.278C61.0303 32.1298 61.2372 32.0185 61.4596 31.9502C61.6821 31.882 61.9158 31.8583 62.1474 31.8804C62.379 31.9024 62.604 31.9699 62.8095 32.079C63.0151 32.188 63.1971 32.3365 63.3453 32.5159C63.4934 32.6953 63.6048 32.9021 63.673 33.1246C63.7412 33.347 63.765 33.5807 63.7429 33.8123L61.416 58.2498C61.2035 60.4527 61.0371 62.2094 60.7891 63.6225C60.5377 65.0746 60.1764 66.3071 59.5142 67.4227C58.4348 69.2317 56.842 70.6789 54.9383 71.5807C53.766 72.1367 52.5052 72.3775 51.0354 72.4909C49.6046 72.6042 47.8408 72.6042 45.6273 72.6042H40.5521C38.4341 72.6042 36.7448 72.6042 35.3671 72.498C33.9539 72.3917 32.7391 72.165 31.5987 71.6444C29.7444 70.7966 28.1731 69.4331 27.0725 67.7167C26.396 66.6613 25.9994 65.4925 25.6912 64.1077C25.3532 62.4121 25.0744 60.7051 24.8554 58.99L21.2677 33.8973C21.2346 33.6671 21.2473 33.4326 21.3048 33.2073C21.3624 32.9819 21.4638 32.7701 21.6033 32.584C21.7427 32.3978 21.9175 32.241 22.1176 32.1224C22.3176 32.0038 22.5427 31.9257 22.7729 31.8927Z"
            fill="#FFFCF8"
          />
        </svg>
      </button>
    </div>
  </div>
</template>
<style scoped lang="scss">
@use '../assets/scss/variables';

.single-meal {
  h2 {
    font-family: variables.$font-heading;
    color: variables.$dark-green;
    font-size: 2rem;
    cursor: pointer;
  }
}
#fullInformation {
  position: absolute;
  top: 0;
  left: 0;
  height: 100vh;
  width: 100%;
  background-color: variables.$dark-green;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  gap: 1.25rem;
  padding: 0 1.25rem;
  text-align: center;
  p {
    font-family: variables.$font-heading;
    color: variables.$light;
    font-size: 1.5rem;
    display: flex;
    flex-direction: column;
    span{
      font-weight: bold;
    }
  }
  div {
    display: flex;
    gap: 1rem;
    button {
      font-family: variables.$font-heading;
      background-color: variables.$dark-green;
      color: variables.$dark-green;
      border: 1px solid white;
      border-radius: 50%;
      min-width: 45px;
      min-height: 45px;
      transition: transform 0.2s ease-in-out;
      cursor: pointer;
      &:active {
        transform: scale(0.9);
      }
      &:nth-child(2) {
        background-color: variables.$clay;
        color: variables.$dark-green;
      }
    }
  }
}
</style>
