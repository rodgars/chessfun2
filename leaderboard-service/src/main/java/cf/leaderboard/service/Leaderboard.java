package cf.leaderboard.service;

public class Leaderboard {
    private final long ranking;
    private final String userName;
    private final long score;

    public Leaderboard(long ranking, String userName, long score){
        this.ranking = ranking;
        this.userName = userName;
        this.score = score;
    }

    public long getRanking(){
        return this.ranking;
    }

    public String getUserName(){
        return this.userName;
    }

    public long getScore(){
        return this.score;
    }
}
