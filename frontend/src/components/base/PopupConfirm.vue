<template>
  <div class="popup">
    <div class="box">
      <h3>{{ title }}</h3>
      <div class="buttons">
        <Button size="large" type="secondary"
          :label="$t('confirm.cancel')"
          v-on:click.native="cancel" />
        <Button size="large"
          :icon="icon"
          :type="type"
          :label="label"
          v-on:click.native="confirm" />
      </div>
    </div>
    <div class="overlay" v-on:click="cancel"></div>
  </div>
</template>

<script>
export default {
  name: 'PopupConfirm',
  props: {
    title: {
      type: String,
      required: true
    },
    icon: {
      type: String,
      required: true
    },
    type: {
      type: String,
      required: true
    },
    label: {
      type: String,
      required: true
    }
  },
  methods: {
    cancel: function () {
      this.$emit('cancel')
    },
    confirm: function () {
      this.$emit('confirm')
    }
  }
}
</script>

<style lang="scss" scoped>
.popup {
  display: flex;
  align-items: center;
  justify-content: center;
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  z-index: var(--depth-popup);

  .box {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    position: relative;
    z-index: 2;
    margin: var(--spacing-06);
    padding: var(--spacing-06) var(--spacing-07);
    background: var(--white);
    border-radius: 5px;
    text-align: center;

    h3 {
      font-size: 1.3rem;
      margin: 0 0 var(--spacing-08);
    }

    .buttons {
      display: flex;

      button + button {
        margin-left: var(--spacing-03);
      }
    }
  }

  .overlay {
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: 1;
    background-color: var(--background-70);
    opacity: 0.6;
  }
}
</style>
