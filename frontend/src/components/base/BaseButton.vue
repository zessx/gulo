<template>
  <button :class="color">
    <BaseIcon v-if="icon" :name="icon" />
    <p v-if="label">{{ label }}</p>
  </button>
</template>

<script>
export default {
  name: 'Button',
  props: {
    label: String,
    icon: String,
    color: String
  }
}
</script>

<style lang="scss" scoped>
button {
  display: flex;
  padding: var(--spacing-05);
  border-radius: 5px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  color: var(--white);
  background-color: var(--primary-50);
  font-weight: bold;
  border: none;
  line-height: 1.2em;
  white-space: nowrap;
  transition: background-color var(--speed-normal);

  i {
    height: 1.2em;

    + p {
      margin-left: var(--spacing-03);
    }
  }

  p {
    margin: 0;
    transform: translateY(0.07em);
  }

  &:hover,
  &:focus {
    outline: none;
    background-color: var(--primary-60);
  }

  &.full {
    width: 100%;
  }

  &.centered {
    justify-content: center;
  }

  &.vertical {
    flex-direction: column;
    align-items: center;
    justify-content: center;

    i + p {
      margin-top: var(--spacing-02);
      margin-left: 0;
    }
  }

  &.small {
    padding: var(--spacing-03);
  }

  &.secondary {
    color: var(--background-70);
    background-color: var(--background-30);

    i {
      color: var(--background-60);
    }

    &:hover,
    &:focus {
      background-color: var(--background-40);
    }
  }

  &.error {
    background-color: var(--error-50);

    &:hover,
    &:focus {
      background-color: var(--error-60);
    }
  }

  &.warning {
    background-color: var(--warning-50);

    &:hover,
    &:focus {
      background-color: var(--warning-60);
    }
  }

  &.success {
    background-color: var(--success-50);

    &:hover,
    &:focus {
      background-color: var(--success-60);
    }
  }

  &[disabled] {
    color: var(--background-50);
    background-color: var(--background-30);

    i {
      color: var(--background-50);
    }

    &:hover,
    &:focus {
      background-color: var(--background-30);
    }
  }
}
</style>
