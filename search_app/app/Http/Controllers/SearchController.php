<?php

namespace App\Http\Controllers;

use App\Models\Article;
use App\Models\User;
use Illuminate\Http\Request;

class SearchController extends Controller
{
    public function __invoke(Request $request)
    {
        $results = null;
        $users = User::all();

        if ($query = $request->get('query')) {

            if ($userId = $request->get('user_id')) {
                $results = Article::search($query)->options([
                    'filter' => 'user_id=' . $userId
                ])->paginate(5)
                ->withQueryString();
            } else {
                $results = Article::search($query)->paginate(5)
                    ->withQueryString();
            }

        }

        return view('search', [
            'results' => $results,
            'users' => $users,
        ]);
    }
}
