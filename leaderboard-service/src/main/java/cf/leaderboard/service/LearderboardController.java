package cf.leaderboard.service;

import java.util.ArrayList;
import java.util.List;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class LearderboardController {

    @GetMapping("/")
    public List<Leaderboard> getLeaderboard(){
        List<Leaderboard> list = new ArrayList<Leaderboard>();
        list.add(new Leaderboard(1, "Donkey Kong", 500));
        list.add(new Leaderboard(2, "Mario", 478));
        list.add(new Leaderboard(3, "Sonic", 469));
        list.add(new Leaderboard(4, "Link", 411));
        list.add(new Leaderboard(5, "Kirby", 388));
        list.add(new Leaderboard(6, "Peter Pan", 382));
        list.add(new Leaderboard(7, "Mickey Mouse", 325));

        return list;
    }

}
