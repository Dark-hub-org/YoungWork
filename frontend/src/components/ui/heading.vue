<template>
  <div class="heading">
    <div class="heading__breadcrumbs"></div>
    <breadcrumbs></breadcrumbs>
    <h1 class="heading__title">{{title}}</h1>
  </div>
</template>

<script>
import Vue from "vue";
import VueBreadcrumbs from 'vue-2-breadcrumbs';

Vue.use(VueBreadcrumbs);

export default {
  name: 'the-heading',
  props: {
    title: String,
  }
}
</script>

<style lang="scss" src="@/style/ui/heading.scss" scoped>

</style>
<style lang="scss">
@import "@/style/varibles";

@function calculate-offset($n) {
  @return 30px * $n;
}

.breadcrumb {
  display: flex;
  align-items: center;
  width: fit-content;
  border-radius: 20px;
  margin-bottom: 80px;

  &-item {
    position: relative;
    @for $i from 2 through 3 {
      &:nth-child(#{$i}) {
        right: calculate-offset($i - 1);
        z-index: $i + 1;
      }
    }
    &:first-child {
      z-index: 10;
    }
    &:last-child {
      z-index: 1;
    }
  }

  span, .router-link-active {
    padding: 8px 40px;
    border-radius: 20px;
    box-shadow: 0px 0px 5px 0px rgba(217, 217, 217, 0.78);
    background-color:$colorWhite;
    font-size: 16px;
    letter-spacing: -0.8px;
  }

  .router-link-active {
    color: $colorGreenM;
    transition: all .3s ease;
    &:hover {
      color: $colorGreenLight;
    }
  }
  span {
    color: $colorWhite;
    background-color: $colorOrangeM;
  }
}

@media(max-width: 1024px) {
  .breadcrumb {
    margin-bottom: 64px;
    span, .router-link-active {
      font-size: 14px;
      letter-spacing: -0.8px;
    }
  }
}
@media(max-width: 450px) {
  .breadcrumb {
    margin-bottom: 48px;
    span, .router-link-active {
      font-size: 12px;
      letter-spacing: -0.6px;
    }
  }

}
</style>