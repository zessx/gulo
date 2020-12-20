<template>
  <div class="tag" :class="active ? 'active' : undefined" :data-type="type">
    <p>{{ label }}</p>
    <Icon v-if="active" name="cross" />
  </div>
</template>

<script>
export default {
  name: 'Tag',
  props: {
    label: String,
    active: {
      type: Boolean,
      default: false
    },
    type: {
      type: String,
      default: 'white',
      validator: function (value) {
        return ['white', 'secondary'].indexOf(value) !== -1
      }
    }
  }
}
</script>

<style lang="scss" scoped>
.tag {
  display: flex;
  align-items: center;
  padding: var(--spacing-03);
  border-radius: 5px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  color: var(--background-70);
  background-color: var(--white);
  font-weight: bold;
  border: none;
  font-size: 1rem;
  line-height: 1em;
  white-space: nowrap;
  transition: background-color var(--speed-normal);
  height: calc(1em + 2 * var(--spacing-03));

  p {
    margin: 0;
    transform: translateY(0.07em);
  }

  i {
    height: 0.875em;
    width: 0.875em;
    margin-left: var(--spacing-03);
  }

  &:hover,
  &:focus {
    outline: none;
    background-color: var(--grey-10);
  }

  &.active {
    color: var(--primary-60);
    background-color: var(--primary-40);
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
}
</style>
