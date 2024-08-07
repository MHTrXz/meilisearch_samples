<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

class ArticleFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array
     */
    public function definition()
    {
        return [
            'title' => $this->faker->sentence(5),
            'teaser' => $this->faker->sentence(200),
            'published' => 1,
            'user_id' => rand(1, 2)
        ];
    }
}
