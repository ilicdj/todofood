<script setup lang="ts">
const props = defineProps({
  message: {
    type: String,
    required: true
  },
  type: {
    type: String,
    default: 'success'
  },
  show: {
    type: Boolean,
    default: false
  }
})
</script>
<template>
  <transition name="fade">
    <div v-if="show" :class="['alert', type]">
      <p>
        {{ message }}
      </p>
    </div>
  </transition>
</template>

<style scoped lang="scss">
.alert {
  position: fixed;
  top: 20px;
  left: 50%;
  transform: translateX(-50%);
  padding: 1rem 2rem;
  border-radius: 5px;
  z-index: 1000;
  
  p {
    color: white;
    text-align: center;
    margin: 0;
  }
  
  &.success {
    background-color: #4caf50;
  }
  
  &.error {
    background-color: #f44336;
  }
}

.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.3s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}
</style>