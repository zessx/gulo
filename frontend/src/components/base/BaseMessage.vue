<template>
  <div class="message" :class="color">
    <BaseIcon v-if="icon" :name="icon" />
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  name: 'Message',
  props: {
    message: String,
    icon: String,
    color: String
  }
}
</script>

<style lang="scss" scoped>
.message {
  display: flex;
  align-items: center;
  height: 3.5rem;
  padding: 0 var(--spacing-04);
  border-radius: 5px;
  color: var(--background-60);
  background-color: var(--background-30);
  font-weight: bold;
  border: none;
  line-height: 1.25em;
  white-space: nowrap;

  i {
    height: 1.25em;

    + p {
      margin-left: var(--spacing-03);
    }
  }

  p {
    margin: 0;
    transform: translateY(0.07em);
  }

  &.error {
    color: var(--error-50);
    background-color: var(--error-40);
  }

  &.warning {
    color: var(--warning-50);
    background-color: var(--warning-40);
  }

  &.success {
    color: var(--success-50);
    background-color: var(--success-40);
  }
}
</style>
