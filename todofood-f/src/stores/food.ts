import axios from 'axios'
import { defineStore } from 'pinia'
import type { FoodItem } from '@/types/FoodItem'

export const useFoodList = defineStore('food', {
  state: () => ({
    food: [] as FoodItem[],
  }),
  actions: {
    async getFood() {
      const response = await axios.get('https://todofood.onrender.com/food')
      this.food = response.data
    },
    async addFood(newMeal: FoodItem) {
      const response = await axios.post('https://todofood.onrender.com/food', newMeal)
      this.food.push(response.data)
    },
    async deleteFood(id: number) {
      await axios.delete(`https://todofood.onrender.com/food/${id}`)
      this.food = this.food.filter(meal => meal.id !== id)
    }
  }
})
