<template>
  <div class="notices">
    <Message v-for="notice in notices"
      :key="notice.id"
      :icon="notice.icon"
      :type="notice.type"
      :message="notice.message" />
  </div>
</template>

<script>
import { mapState } from 'vuex'

export default {
  name: 'Notices',
  data: function () {
    return {
      notices: []
    }
  },
  created: function () {
    this.notices = this.$store.state.notices.all
    this.$store.commit('notices/clearNotices')
  }
}
</script>

<style lang="scss" scoped>
.recipe {
  display: flex;
  height: 6.25em;
  padding: var(--spacing-01);
  border-radius: 5px;
  box-shadow: 0 2px 4px 0 rgba(0, 0, 0, 0.1);
  background-color: var(--white);

  img {
    display: block;
    height: calc(6.25em - 2 * var(--spacing-01));
    width: calc(6.25em - 2 * var(--spacing-01));
    object-fit: cover;
    object-position: center center;
    margin-right: var(--spacing-03);
    border-radius: 3px;
    background-color: var(--grey-10);
  }

  > div {
    display: flex;
    flex-direction: column;
    flex-grow: 1;
    padding: var(--spacing-02);
  }

  h3 {
    margin: 0;
    font-size: 1.125em;
  }

  footer {
    display: flex;
    align-items: flex-end;
    margin-top: auto;

    .duration {

      + .portions {
        margin-left: var(--spacing-04);
      }
    }

    .duration,
    .portions {
      i {
        float: left;
        height: 1.25em;
        margin-right: var(--spacing-02);
        color: var(--background-40);
      }

      span {
        line-height: 1.35em;
      }
    }

    button {
      margin-left: auto;
    }
  }
}
</style>
