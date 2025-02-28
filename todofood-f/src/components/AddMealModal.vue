<script setup lang="ts">
import { useFoodList } from '@/stores/food'
import type { FoodItem } from '@/types/FoodItem'
import { ref } from 'vue'
import MessageAlert from './MessageAlert.vue'

const foodStore = useFoodList()

// Form data
const isVisible = ref(false)
const mealNameModel = ref('')
const ingredientsModel = ref('')
const descriptionModel = ref('')
const timeInMinutesModel = ref()
const veganModel = ref(false)
const glutenFreeModel = ref(false)

// Message alert
const alertMessage = ref('')
const alertType = ref('success')
const showAlert = ref(false)

// Function to show alert message
function showMessage(message: string, type: string = 'success') {
  alertMessage.value = message
  alertType.value = type
  showAlert.value = true

  // Auto-hide the alert after 3 seconds
  setTimeout(() => {
    showAlert.value = false
  }, 3000)
}

function submitMeal() {
  if (
    !mealNameModel.value ||
    !ingredientsModel.value ||
    !descriptionModel.value ||
    !timeInMinutesModel.value
  ) {
    showMessage('Please fill in all fields', 'error')
    return
  }

  const newMeal: FoodItem = {
    meal_name: mealNameModel.value,
    ingredients: ingredientsModel.value,
    description: descriptionModel.value,
    time_in_minutes: timeInMinutesModel.value,
    is_vegan: veganModel.value,
    is_gluten_free: glutenFreeModel.value,
  }
  try {
    foodStore.addFood(newMeal)
    showMessage(`${mealNameModel.value} has been added successfully!`)
    isVisible.value = false

    // Reset form fields
    mealNameModel.value = ''
    ingredientsModel.value = ''
    descriptionModel.value = ''
    timeInMinutesModel.value = ''
    veganModel.value = false
    glutenFreeModel.value = false
  } catch (error) {
    showMessage(`Failed to add meal: ${error}`, 'error')
  }
}

function handleShowForm() {
  isVisible.value = !isVisible.value
}
</script>
<template>
  <!-- Alert message component -->
  <MessageAlert :message="alertMessage" :type="alertType" :show="showAlert" />
  <div class="btn-wrapper">
    <button @click="handleShowForm()" id="newMealBtn">+</button>
  </div>
  <div v-if="isVisible" id="form">
    <div>
      <label for="meal_name">Meal Name</label>
      <input v-model="mealNameModel" type="text" name="meal_name" id="meal_name" />
    </div>
    <div>
      <label for="ingredients">Ingredients</label>
      <input v-model="ingredientsModel" type="text" name="ingredients" id="ingredients" />
    </div>
    <div>
      <label for="description">Description</label>
      <textarea v-model="descriptionModel" name="description" id="description" rows="5"></textarea>
    </div>
    <div>
      <label for="time_in_minutes">Time<span>(in minutes)</span></label>
      <input v-model="timeInMinutesModel" type="text" name="time_in_minutes" id="time_in_minutes" />
    </div>
    <div>
      <label for="vegan">Vegan</label>
      <input v-model="veganModel" type="checkbox" name="is_vegan" id="vegan" />
    </div>
    <div>
      <label for="gluten_free">Gluten Free</label>
      <input v-model="glutenFreeModel" type="checkbox" name="gluten_free" id="gluten_free" />
    </div>
    <div id="form-btns">
      <button @click="submitMeal()">
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="35"
          height="35"
          viewBox="0 0 85 85"
          fill="none"
        >
          <path
            d="M30.1042 58.7421L16.6707 45.3086C16.0027 44.6635 15.1081 44.3065 14.1795 44.3145C13.2509 44.3226 12.3626 44.6951 11.7059 45.3517C11.0493 46.0084 10.6768 46.8967 10.6687 47.8253C10.6606 48.7539 11.0176 49.6486 11.6628 50.3165L27.6003 66.254C28.2644 66.918 29.1651 67.291 30.1042 67.291C31.0433 67.291 31.944 66.918 32.6082 66.254L71.5665 27.2957C72.2117 26.6277 72.5686 25.7331 72.5606 24.8045C72.5525 23.8759 72.18 22.9876 71.5234 22.3309C70.8667 21.6743 69.9784 21.3018 69.0498 21.2937C68.1212 21.2856 67.2266 21.6426 66.5586 22.2878L30.1042 58.7421Z"
            fill="#FFFCF8"
          />
        </svg>
      </button>
      <button @click="handleShowForm()">
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
    </div>
  </div>
</template>
<style scoped lang="scss">
@use '../assets/scss/variables';
#newMealBtn {
  font-family: variables.$font-heading;
  font-size: 2rem;
  background-color: variables.$dark-green;
  border: 0px;
  color: variables.$light;
  border-radius: 50%;
  min-width: 45px;
  min-height: 45px;
  margin-top: 1rem;
  transition: transform 0.2s ease-in-out;
  cursor: pointer;
  &:active {
    transform: scale(0.9);
  }
}
#form {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  background-color: variables.$light-green;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  padding: 4rem;
  gap: 1rem;
  border-radius: 10px;
  div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    gap: 0.2rem;
    label {
      font-family: variables.$font-heading;
      font-size: 1.5rem;
    }
    input[type='text'] {
      border: 0;
      outline: none;
      background-color: transparent;
      border-bottom: 1px solid variables.$clay;
      font-size: 1rem;
    }
    &:has(input[type='checkbox']) {
      flex-direction: row;
      align-items: center;
      gap: 0.4rem;
    }
    textarea {
      resize: none;
      width: 100%;
      background-color: transparent;
      border: 0;
      outline: none;
      border-bottom: 1px solid variables.$clay;
      font-size: 1rem;
    }
  }
  #form-btns {
    display: flex;
    flex-direction: row;
    justify-content: center;
    gap: 1rem;
    button {
      font-family: variables.$font-text;
      border: 0;
      outline: none;
      background-color: variables.$dark-green;
      border-radius: 50%;
      padding: 0.2rem 0.4rem;
      font-size: 1.25rem;
      cursor: pointer;
      &:nth-child(2){
        background-color: variables.$clay;
      }
      &:active {
        transform: scale(0.9);
      }
    }
  }
}
@media(min-width: 768px) {
  #newMealBtn {
    margin-top: 0;
  }
}
</style>
