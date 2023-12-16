package com.kis.cat.hacminin.ui.app

import android.os.Bundle
import androidx.fragment.app.Fragment
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import by.kirich1409.viewbindingdelegate.viewBinding
import com.kis.cat.hacminin.R
import com.kis.cat.hacminin.databinding.FragmentAppBinding


class AppFragment : Fragment(R.layout.fragment_app) {

    private val binding: FragmentAppBinding by viewBinding()

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)
    }
}