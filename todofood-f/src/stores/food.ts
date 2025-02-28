import axios from 'axios'
import { defineStore } from 'pinia'
import type { FoodItem } from '@/types/FoodItem'

export const useFoodList = defineStore('food', {
  state: () => ({
    food: [] as FoodItem[],
  }),
  actions: {
    async getFood() {
      const response = await axios.get('http://127.0.0.1:5000/food')
      this.food = response.data
    },
    async addFood(newMeal: FoodItem) {
      const response = await axios.post('http://127.0.0.1:5000/food', newMeal)
      this.food.push(response.data)
    },
    async deleteFood(id: number) {
      await axios.delete(`http://127.0.0.1:5000/food/${id}`)
      this.food = this.food.filter(meal => meal.id !== id)
    }
  }
})
