<template>
  <button :data-size="size" :data-type="type">
    <Icon v-if="icon" :name="icon" />
    <p v-if="label">{{ label }}</p>
  </button>
</template>

<script>
export default {
  name: 'Button',
  props: {
    label: String,
    icon: String,
    size: {
      type: String,
      default: 'medium',
      validator: function (value) {
        return ['small', 'medium', 'large'].indexOf(value) !== -1
      }
    },
    type: {
      type: String,
      default: 'primary',
      validator: function (value) {
        return ['primary', 'secondary', 'white', 'success', 'warning', 'error'].indexOf(value) !== -1
      }
    }
  }
}
</script>

<style lang="scss" scoped>
button {
  display: flex;
  align-items: center;
  padding: var(--spacing-03);
  border-radius: 5px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  color: var(--white);
  background-color: var(--primary-50);
  font-weight: bold;
  border: none;
  font-size: 1rem;
  line-height: 1em;
  white-space: nowrap;
  transition: background-color var(--speed-normal);
  height: calc(1em + 2 * var(--spacing-03));

  i {
    height: 1em;
    width: 1em;

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

  &[data-size="small"] {
    padding: var(--spacing-02);
    line-height: 0.75em;
    height: calc(0.75em + 2 * var(--spacing-02));

    i {
      height: 0.75em;
      width: 0.75em;
    }
  }

  &[data-size="large"] {
    padding: var(--spacing-04);
    line-height: 1.5em;
    font-size: 1.125rem;
    height: calc(1.5em + 2 * var(--spacing-04));

    i {
      height: 1.2em;
      width: 1.2em;
    }
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
    height: auto;

    i + p {
      margin-top: var(--spacing-01);
      margin-left: 0;
    }
  }

  &[data-type="secondary"] {
    color: var(--background-70);
    background-color: var(--background-30);
    box-shadow: none;

    i {
      color: var(--background-60);
    }

    &:hover,
    &:focus {
      background-color: var(--background-40);
    }
  }

  &[data-type="white"] {
    color: var(--background-70);
    background-color: var(--white);

    i {
      color: var(--background-60);
    }

    &:hover,
    &:focus {
      background-color: var(--grey-10);
    }
  }

  &[data-type="error"] {
    background-color: var(--error-50);

    &:hover,
    &:focus {
      background-color: var(--error-60);
    }
  }

  &[data-type="warning"] {
    background-color: var(--warning-50);

    &:hover,
    &:focus {
      background-color: var(--warning-60);
    }
  }

  &[data-type="success"] {
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
