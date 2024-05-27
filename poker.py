from treys import Deck, Evaluator, Card


def calculate_win_percentages(player_hands, community_cards, folded_hands):
    evaluator = Evaluator()

    player_hands_treys = []
    for hand in player_hands:
        converted_hand = []
        for card in hand:
            converted_hand.append(Card.new(card))
        player_hands_treys.append(converted_hand)

    community_cards_treys = []
    for card in community_cards:
        community_cards_treys.append(Card.new(card))

    # Generate the remaining deck
    used_cards = set()
    for hand in player_hands:
        for card in hand:
            used_cards.add(card)
    for card in community_cards:
        used_cards.add(card)

    for hand in folded_hands:
        for card in hand:
            used_cards.add(card)

    remaining_deck = []
    for card in Deck().cards:
        card_str = Card.int_to_str(card)
        if card_str not in used_cards:
            remaining_deck.append(card)

    win_counts = [0] * len(player_hands)
    tie_counts = [0] * len(player_hands)

    player_outs = [set() for _ in range(len(player_hands))]

    '''Actual calculation starts here'''
    numb_of_iterations = 0
    if len(community_cards_treys) == 3:
        for card1 in remaining_deck:
            for card2 in remaining_deck:
                if card1 == card2:
                    continue
                full_community = community_cards_treys + [card1, card2]
                scores = []
                for hand in player_hands_treys:
                    score = evaluator.evaluate(full_community, hand)
                    scores.append(score)

                min_score = min(scores)
                winners = []
                for i in range(len(scores)):
                    score = scores[i]
                    if score == min_score:
                        winners.append(i)

                if len(winners) == 1:
                    win_counts[winners[0]] += 1
                    player_outs[winners[0]].add(Card.int_to_str(card2))
                else:
                    for winner in winners:
                        tie_counts[winner] += 1
                        player_outs[winner].add(Card.int_to_str(card2))

                numb_of_iterations += 1

    elif len(community_cards_treys) == 4:
        for card in remaining_deck:

            full_community = community_cards_treys + [card]
            scores = []
            for hand in player_hands_treys:
                score = evaluator.evaluate(full_community, hand)
                scores.append(score)

            min_score = min(scores)
            winners = []
            for i in range(len(scores)):
                score = scores[i]
                if score == min_score:
                    winners.append(i)

            if len(winners) == 1:
                win_counts[winners[0]] += 1
            else:
                for winner in winners:
                    tie_counts[winner] += 1

            for i in winners:
                player_outs[i].add(Card.int_to_str(card))

            numb_of_iterations += 1

    elif len(community_cards_treys) == 5:
        full_community = community_cards_treys

        scores = []
        for hand in player_hands_treys:
            score = evaluator.evaluate(full_community, hand)
            scores.append(score)

        min_score = min(scores)
        winners = []
        for i in range(len(scores)):
            score = scores[i]
            if score == min_score:
                winners.append(i)

        if len(winners) == 1:
            win_counts[winners[0]] += 1
        else:
            for winner in winners:
                tie_counts[winner] += 1

        numb_of_iterations += 1

    win_percentages = [round(win / numb_of_iterations * 100) for win in win_counts]
    tie_percentages = [round(tie / numb_of_iterations * 100) for tie in tie_counts]

    return win_percentages, tie_percentages, player_outs
