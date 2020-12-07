<template>
  <div class="message" :class="type">
    <BaseIcon v-if="icon" :name="icon" />
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  name: 'Message',
  props: {
    message: {
      type: String,
      required: true
    },
    icon: {
      type: String,
      default: 'info'
    },
    type: {
      type: String,
      default: 'info',
      validator: function (value) {
        return ['info', 'success', 'warning', 'error'].indexOf(value) !== -1
      }
    }
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
    flex-shrink: 0;

    + p {
      margin-left: var(--spacing-03);
    }
  }

  p {
    margin: 0;
    word-break: break-word;
    white-space: break-spaces;
    transform: translateY(0.07em);
  }

  &.centered {
    justify-content: center;
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
